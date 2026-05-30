import sqlite3
import pandas as pd

# =====================================
# DATABASE CONNECTION
# =====================================

conn = sqlite3.connect(
    r"D:\DS_Projects\P1_DATA_STOCK\stock_market.db"
)

# =====================================
# VOLATILITY ANALYSIS
# =====================================

volatility_df = pd.read_csv(
    r"D:\DS_Projects\P1_DATA_STOCK\data\Volatility_Analysis.csv"
)

volatility_df.to_sql(
    "volatility_analysis",
    conn,
    if_exists="replace",
    index=False
)

# =====================================
# CUMULATIVE RETURN
# =====================================

cumulative_df = pd.read_csv(
    r"D:\DS_Projects\P1_DATA_STOCK\data\Cumulative_Return_Analysis.csv"
)

cumulative_df.to_sql(
    "cumulative_return",
    conn,
    if_exists="replace",
    index=False
)

# =====================================
# SECTOR PERFORMANCE
# =====================================

sector_df = pd.read_csv(
    r"D:\DS_Projects\P1_DATA_STOCK\data\Sector_Performance.csv"
)

sector_df.to_sql(
    "sector_performance",
    conn,
    if_exists="replace",
    index=False
)

# =====================================
# MONTHLY GAINERS LOSERS
# =====================================

monthly_df = pd.read_csv(
    r"D:\DS_Projects\P1_DATA_STOCK\data\Monthly_Gainers_Losers.csv"
)

monthly_df.to_sql(
    "monthly_gainers_losers",
    conn,
    if_exists="replace",
    index=False
)

# =====================================
# STOCK CORRELATION
# =====================================

correlation_df = pd.read_csv(
    r"D:\DS_Projects\P1_DATA_STOCK\data\Stock_Correlation.csv"
)

correlation_df.to_sql(
    "stock_correlation",
    conn,
    if_exists="replace",
    index=False
)

# =====================================
# CLOSE DATABASE
# =====================================

conn.close()

print("\nDatabase Created Successfully")