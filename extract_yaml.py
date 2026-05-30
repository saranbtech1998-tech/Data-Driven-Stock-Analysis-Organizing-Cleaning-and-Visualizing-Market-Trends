import os
import yaml
import pandas as pd


input_folder = r"D:\DS_Projects\P1_DATA_STOCK\data"
output_folder = r"D:\DS_Projects\P1_DATA_STOCK\data\Extracted_Files"
os.makedirs(output_folder, exist_ok=True)
all_data = {}


for root, dirs, files in os.walk(input_folder):

    for file in files:

        if file.endswith(".yaml") or file.endswith(".yml"):
            file_path = os.path.join(root, file)
            print("Reading:", file_path)
            with open(file_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                for record in data:
                    ticker = record["Ticker"]
                    if ticker not in all_data:
                        all_data[ticker] = []                  
                    all_data[ticker].append(record)
for ticker in all_data:
    df = pd.DataFrame(all_data[ticker])
    output_file = os.path.join(
        output_folder,
        ticker + ".csv"
    )
    df.to_csv(output_file, index=False)
    print("Created:", output_file)
print("\nALL FILES CREATED SUCCESSFULLY")