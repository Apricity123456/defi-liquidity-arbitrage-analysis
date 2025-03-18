import pandas as pd

# 读取 CSV 文件
df = pd.read_csv("../data/uniswap_data.csv")

# 转换时间格式
df["date"] = pd.to_datetime(df["date"])

# 先将字符串类型的数据转换为 float
df["total_liquidity_added"] = pd.to_numeric(df["total_liquidity_added"], errors="coerce") / 1e18
df["total_liquidity_removed"] = pd.to_numeric(df["total_liquidity_removed"], errors="coerce") / 1e18
df["total_trading_volume"] = pd.to_numeric(df["total_trading_volume"], errors="coerce") / 1e18
#过滤掉极端值
df = df[df["total_liquidity_added"] < 1e10]  # 过滤掉异常流动性数据
df = df[df["total_trading_volume"] < 1e10]  # 过滤掉异常交易量数据
df = df[df["total_liquidity_removed"] < 1e10]
# 保存处理后的数据
df.to_csv("../data/uniswap_liquidity_data_cleaned.csv", index=False)

print(" 数据清理完成，已保存到 data/uniswap_liquidity_data_cleaned.csv")
