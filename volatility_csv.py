import os
import pandas as pd

input_folder = r"D:\DS_Projects\P1_DATA_STOCK\data\Extracted_Files"

volatility_list = []

for file in os.listdir(input_folder):

    if file.endswith(".csv"):

        file_path = os.path.join(input_folder, file)

        # Read CSV
        df = pd.read_csv(file_path)

        # Convert date
        df["date"] = pd.to_datetime(df["date"])

        # Sort by date
        df = df.sort_values("date")

        # Calculate Daily Return
        df["Daily_Return"] = df["close"].pct_change()

        # Calculate Volatility
        volatility = df["Daily_Return"].std()

        # Remove .csv
        ticker_name = file.replace(".csv", "")

        # Store result
        volatility_list.append({
            "Ticker": ticker_name,
            "Volatility": volatility
        })

# CREATE FINAL DATAFRAME
volatility_df = pd.DataFrame(volatility_list)

# SORT DATA
volatility_df = volatility_df.sort_values(
    by="Volatility",
    ascending=False
)

output_file = r"D:\DS_Projects\P1_DATA_STOCK\data\Volatility_Analysis.csv"

volatility_df.to_csv(output_file, index=False)

print("\nVolatility Analysis Completed\n")

print(volatility_df.head(10))