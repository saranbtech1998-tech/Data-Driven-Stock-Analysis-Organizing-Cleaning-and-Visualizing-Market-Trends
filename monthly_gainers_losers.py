import os
import pandas as pd

input_folder = r"D:\DS_Projects\P1_DATA_STOCK\data\Extracted_Files"
all_monthly_data = []


for file in os.listdir(input_folder):

    if file.endswith(".csv"):

        # File path
        file_path = os.path.join(input_folder, file)

        # Read csv
        df = pd.read_csv(file_path)

        # Convert date
        df["date"] = pd.to_datetime(df["date"])

        # Create month column
        df["Month"] = df["date"].dt.strftime("%Y-%m")

        # Stock name
        ticker_name = file.replace(".csv", "")

    
        monthly_data = df.groupby("Month").agg({
            "close": ["first", "last"]
        })

        monthly_data.columns = [
            "First_Price",
            "Last_Price"
        ]

        monthly_data = monthly_data.reset_index()

        # Monthly Return
        monthly_data["Monthly_Return"] = (
            (monthly_data["Last_Price"]
            - monthly_data["First_Price"])
            / monthly_data["First_Price"]
        )

        # Add ticker
        monthly_data["Ticker"] = ticker_name

        # Keep required columns
        monthly_data = monthly_data[[
            "Month",
            "Ticker",
            "Monthly_Return"
        ]]

        # Add data
        all_monthly_data.append(monthly_data)

final_df = pd.concat(all_monthly_data)

result_list = []

months = final_df["Month"].unique()

for month in months:

    month_df = final_df[
        final_df["Month"] == month
    ]

    # Top 5 Gainers
    top_gainers = month_df.sort_values(
        by="Monthly_Return",
        ascending=False
    ).head(5)

    top_gainers["Type"] = "Gainer"

    # Top 5 Losers
    top_losers = month_df.sort_values(
        by="Monthly_Return",
        ascending=True
    ).head(5)

    top_losers["Type"] = "Loser"

    # Add result
    result_list.append(top_gainers)
    result_list.append(top_losers)

result_df = pd.concat(result_list)

output_file = r"D:\DS_Projects\P1_DATA_STOCK\data\Monthly_Gainers_Losers.csv"

result_df.to_csv(output_file, index=False)

print("\nMonthly Gainers and Losers Completed")