from app import Solution
import pandas as pd
df = pd.read_csv(r'C:\Users\mk744\OneDrive - Poornima University\Desktop\URL Structure Analysis\autotrader_robots.csv')
sol = Solution(df)
ans = sol.Read_data()
print(ans, '\n')

Sol = Solution(df)
Ans = Sol.Shape_data()
print("Rows and Columns are!")
print(Ans, '\n')

Miss = Solution(df)
miss = Miss.Missing_Values()
print("Missing values are!")
print(miss, '\n')


Cols = Solution(df)
Columns = Cols.Columns_List()
print("Columns in list are !")
print(Columns, '\n')

Rels = Solution(df)
Rel_Cols = Rels.Relevent_columns()
print("Required Columns are !")
print(Rel_Cols, '\n')

Drop_cols = Solution(df)
Cols_drop = Drop_cols.Modify_Dates()
print("The modified data's are!")
print(Cols_drop,'\n')

processor = Solution(df)
result_df = processor.split_url()
print("After Preprocessing !")
print(result_df)
