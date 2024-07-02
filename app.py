class Solution:
     import pandas as pd
     def __init__(self, df:int)->None:
          self.df = df
          
     def Read_data(self)->int:
          return self.df.head()
     
     def Shape_data(self)->int:
          return self.df.shape
     
     def Missing_Values(self)->int:
          return self.df.isnull().sum()
     
     def Columns_List(self)->int:
          return self.df.columns.tolist()
     
     def Relevent_columns(self)->int:
          return self.df[['robotstxt_last_modified','robotstxt_url', 'download_date']]
     
     def Modify_Dates(self)->pd.DataFrame:
          import pandas as pd
          self.df['Modified_Date'] = pd.to_datetime(self.df['robotstxt_last_modified'], errors='coerce').dt.date
          self.df['Modified_Time'] = pd.to_datetime(self.df['robotstxt_last_modified'], errors='coerce').dt.time
          self.df['Download_Date'] = pd.to_datetime(self.df['download_date'], errors='coerce').dt.date
          self.df['Download_Time'] = pd.to_datetime(self.df['download_date'], errors='coerce').dt.time
          Drop_cols = self.df.drop(columns = ['robotstxt_last_modified', 'download_date'])
          Select_Cols = Drop_cols[['robotstxt_url','Modified_Date','Modified_Time','Download_Date', 'Download_Time']]
          return Select_Cols
          
          
     def split_url(self) -> pd.DataFrame:
          import pandas as pd
          from urllib.parse import urlparse, parse_qs
          def parse_url(url):
               parsed_url = urlparse(url)
               query_params = parse_qs(parsed_url.query)

            # Create a dictionary to store URL components
               url_components = {
                'scheme': parsed_url.scheme,
                'netloc': parsed_url.netloc,
                'path': parsed_url.path
            }

            # Flatten the query parameters and add to the dictionary
               for key, value in query_params.items():
                url_components[key] = value[0] if value else None

               return url_components

        # Apply the parse_url function to the 'robotstxt_url' column
          url_components_df = self.df['robotstxt_url'].apply(parse_url).apply(pd.Series)

        # Concatenate the original DataFrame with the new components DataFrame
          self.df = pd.concat([self.df, url_components_df], axis=1)
          return self.df
