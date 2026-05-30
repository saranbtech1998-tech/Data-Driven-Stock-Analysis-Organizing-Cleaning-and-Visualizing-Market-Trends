import os
import pandas as pd
from pyproj import pj_list

input_folder = r"D:\DS_Projects\P1_DATA_STOCK\data\Extracted_Files"
all_data = []

stock_performance = []
for file in os.listdir(input_folder):

    # Check csv file
    if file.endswith(".csv"):

        # File path
        file_path = os.path.join(input_folder, file)

        # Read csv
        df = pd.read_csv(file_path)

        # Convert date
        df["date"] = pd.to_datetime(df["date"])

        # Sort date
        df = df.sort_values("date")


        df["Daily_Return"] = df["close"].pct_change()

        
        df["Cumulative_Return"] = (
            1 + df["Daily_Return"]
        ).cumprod() - 1

        # Stock name
        ticker_name = file.replace(".csv", "")

        # Add ticker column
        df["Ticker"] = ticker_name

        # Final return value
        final_return = df["Cumulative_Return"].iloc[-1]

        # Store performance
        stock_performance.append({
            "Ticker": ticker_name,
            "Return": final_return
        })

        # Keep only needed columns
        df = df[[
            "date",
            "Ticker",
            "Cumulative_Return"
        ]]

        # Add data
        all_data.append(df)


performance_df = pd.DataFrame(stock_performance)

top5 = performance_df.sort_values(
    by="Return",
    ascending=False
).head(5)

# Top 5 ticker names
top5_list = top5["Ticker"].tolist()


final_df = pd.concat(all_data)

# Keep only Top 5 stocks
final_df = final_df[
    final_df["Ticker"].isin(pj_list)
]
output_file = r"D:\DS_Projects\P1_DATA_STOCK\data\Cumulative_Return_Analysis.csv"

final_df.to_csv(output_file, index=False)


print("\nTop 5 Performing Stocks\n")

print(top5)

print("\nCSV File Created Successfully")