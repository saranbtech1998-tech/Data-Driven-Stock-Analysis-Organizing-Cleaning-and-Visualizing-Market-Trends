import os
import pandas as pd

input_folder = r"D:\DS_Projects\P1_DATA_STOCK\data\Extracted_Files"
sector_file = r"D:\DS_Projects\P1_DATA_STOCK\data\Sector_Data.csv"

# Read sector csv
sector_df = pd.read_csv(sector_file)

# Keep required columns
sector_df = sector_df[["sector", "Symbol"]]

# Rename columns
sector_df.columns = ["Sector", "Ticker"]

# Extract actual ticker name
sector_df["Ticker"] = sector_df["Ticker"].str.split(":").str[-1].str.strip()

stock_list = []

for file in os.listdir(input_folder):

    if file.endswith(".csv"):

        # File path
        file_path = os.path.join(input_folder, file)

        # Read stock csv
        df = pd.read_csv(file_path)

        # Sort by date
        df = df.sort_values("date")

        # First close price
        first_price = df["close"].iloc[0]

        # Last close price
        last_price = df["close"].iloc[-1]

        # Yearly Return
        yearly_return = (
            (last_price - first_price)
            / first_price
        )

        # Stock name
        ticker_name = file.replace(".csv", "")

        # Add data
        stock_list.append({
            "Ticker": ticker_name,
            "Yearly_Return": yearly_return
        })

return_df = pd.DataFrame(stock_list)

merged_df = pd.merge(
    return_df,
    sector_df,
    on="Ticker",
    how="left"
)

sector_performance = merged_df.groupby(
    "Sector"
)["Yearly_Return"].mean().reset_index()

sector_performance = sector_performance.sort_values(
    by="Yearly_Return",
    ascending=False
)
output_file = r"D:\DS_Projects\P1_DATA_STOCK\data\Sector_Performance.csv"

sector_performance.to_csv(output_file, index=False)

print("\nSector Performance Completed\n")

print(sector_performance)