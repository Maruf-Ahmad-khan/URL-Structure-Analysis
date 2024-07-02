import pandas as pd
from urllib.parse import urlparse, parse_qs

class Solution:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def Read_data(self) -> pd.DataFrame:
        return self.df.head()

    def Shape_data(self) -> tuple:
        return self.df.shape

    def Missing_Values(self) -> pd.Series:
        return self.df.isnull().sum()

    def Columns_List(self) -> list:
        return self.df.columns.tolist()

    def Relevent_columns(self) -> pd.DataFrame:
        return self.df[['robotstxt_last_modified', 'robotstxt_url', 'download_date']]

    def Modify_Dates(self) -> pd.DataFrame:
        self.df['Modified_Date'] = pd.to_datetime(self.df['robotstxt_last_modified'], errors='coerce').dt.date
        self.df['Modified_Time'] = pd.to_datetime(self.df['robotstxt_last_modified'], errors='coerce').dt.time
        self.df['Download_Date'] = pd.to_datetime(self.df['download_date'], errors='coerce').dt.date
        self.df['Download_Time'] = pd.to_datetime(self.df['download_date'], errors='coerce').dt.time
        drop_cols = self.df.drop(columns=['robotstxt_last_modified', 'download_date'])
        select_cols = drop_cols[['robotstxt_url', 'Modified_Date', 'Modified_Time', 'Download_Date', 'Download_Time']]
        return select_cols

    def split_url(self) -> pd.DataFrame:
        def parse_url(url):
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)

            url_components = {
                'scheme': parsed_url.scheme,
                'netloc': parsed_url.netloc,
                'path': parsed_url.path
            }

            for key, value in query_params.items():
                url_components[key] = value[0] if value else None

            return url_components

        url_components_df = self.df['robotstxt_url'].apply(parse_url).apply(pd.Series)
        self.df = pd.concat([self.df, url_components_df], axis=1)
        return self.df

    def save_to_csv(self, file_path: str) -> None:
        self.df.to_csv(file_path, index=False)
