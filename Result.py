from Demo import Solution
import pandas as pd

# Load the DataFrame
df = pd.read_csv(r'C:\Users\mk744\OneDrive - Poornima University\Desktop\URL Structure Analysis\autotrader_robots.csv')

# Initialize Solution instance
sol = Solution(df)

# Perform various operations
ans = sol.Read_data()
print(ans, '\n')

Ans = sol.Shape_data()
print("Rows and Columns are!")
print(Ans, '\n')

miss = sol.Missing_Values()
print("Missing values are!")
print(miss, '\n')

Columns = sol.Columns_List()
print("Columns in list are !")
print(Columns, '\n')

Rel_Cols = sol.Relevent_columns()
print("Required Columns are !")
print(Rel_Cols, '\n')

Cols_drop = sol.Modify_Dates()
print("The modified data's are!")
print(Cols_drop, '\n')

result_df = sol.split_url()
print("After Preprocessing !")
print(result_df, '\n')

# Save the result to a CSV file
output_file_path = r'C:\Users\mk744\OneDrive - Poornima University\Desktop\URL Structure Analysis\processed_autotrader_robots.csv'
sol.save_to_csv(output_file_path)
print(f"The processed DataFrame has been saved to {output_file_path}")
