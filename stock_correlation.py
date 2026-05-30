import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

input_folder = r"D:\DS_Projects\P1_DATA_STOCK\data\Extracted_Files"
all_stocks = pd.DataFrame()

for file in os.listdir(input_folder):

    if file.endswith(".csv"):

        # File path
        file_path = os.path.join(input_folder, file)

        # Read csv
        df = pd.read_csv(file_path)

        # Convert date
        df["date"] = pd.to_datetime(df["date"])

        # Sort by date
        df = df.sort_values("date")

        # Stock name
        ticker_name = file.replace(".csv", "")

        # Keep required columns
        df = df[["date", "close"]]

        # Rename close column
        df.rename(
            columns={"close": ticker_name},
            inplace=True
        )

        # Merge all stocks
        if all_stocks.empty:

            all_stocks = df

        else:

            all_stocks = pd.merge(
                all_stocks,
                df,
                on="date",
                how="outer"
            )

price_data = all_stocks.drop(columns=["date"])

correlation_matrix = price_data.corr()

output_file = r"D:\DS_Projects\P1_DATA_STOCK\data\Stock_Correlation.csv"

correlation_matrix.to_csv(output_file)

plt.figure(figsize=(15, 10))

sns.heatmap(
    correlation_matrix,
    cmap="coolwarm"
)

plt.title("Stock Price Correlation Heatmap")
plt.savefig(
    r"D:\DS_Projects\P1_DATA_STOCK\data\Correlation_Heatmap.png"
)

plt.show()

print("\nStock Correlation Completed")
