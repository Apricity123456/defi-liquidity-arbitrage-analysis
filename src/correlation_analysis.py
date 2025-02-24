import pandas as pd

# 读取数据
df = pd.read_csv("../data/uniswap_liquidity_analysis.csv")
df["date"] = pd.to_datetime(df["date"])


# 计算交易量 & TVL 的相关性
correlation = df["total_trading_volume"].corr(df["total_liquidity_added"])
print(f"Liquidity & Trading Volume Correlation: {correlation:.2f}")
# 计算交易量 & 流动性之间的相关性
correlation = df["total_trading_volume"].corr(df["liquidity_change"])
print(f"Liquidity & Trading Volume Correlation: {correlation:.2f}")
