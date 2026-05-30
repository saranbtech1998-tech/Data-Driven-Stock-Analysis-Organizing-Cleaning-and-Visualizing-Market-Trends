import streamlit as st
import pandas as pd
import sqlite3

# =====================================
# PAGE TITLE
# =====================================

st.title("Stock Market Dashboard")

# =====================================
# DATABASE CONNECTION
# =====================================

conn = sqlite3.connect(
    r"D:\DS_Projects\P1_DATA_STOCK\stock_market.db"
)

# =====================================
# SIDEBAR MENU
# =====================================

menu = st.sidebar.selectbox(
    "Select Analysis",
    [
        "Volatility Analysis",
        "Sector Performance",
        "Monthly Gainers Losers"
    ]
)

# =====================================
# VOLATILITY ANALYSIS
# =====================================

if menu == "Volatility Analysis":

    query = """
    SELECT *
    FROM volatility_analysis
    ORDER BY Volatility DESC
    LIMIT 10
    """

    df = pd.read_sql(query, conn)

    st.subheader("Top 10 Volatile Stocks")

    st.dataframe(df)

    st.bar_chart(
        data=df,
        x="Ticker",
        y="Volatility"
    )

# =====================================
# SECTOR PERFORMANCE
# =====================================

elif menu == "Sector Performance":

    query = """
    SELECT *
    FROM sector_performance
    ORDER BY Yearly_Return DESC
    """

    df = pd.read_sql(query, conn)

    st.subheader("Sector-wise Performance")

    st.dataframe(df)

    st.bar_chart(
        data=df,
        x="Sector",
        y="Yearly_Return"
    )

# =====================================
# MONTHLY GAINERS LOSERS
# =====================================

elif menu == "Monthly Gainers Losers":

    query = """
    SELECT *
    FROM monthly_gainers_losers
    """

    df = pd.read_sql(query, conn)

    st.subheader("Monthly Gainers and Losers")

    st.dataframe(df)

    st.bar_chart(
        data=df,
        x="Ticker",
        y="Monthly_Return"
    )

# =====================================
# CLOSE CONNECTION
# =====================================

conn.close()