import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
df = pd.read_csv("../data/uniswap_data.csv")
df["date"] = pd.to_datetime(df["date"])

# 计算 TVL 和交易量变化率
df["TVL_Change"] = df["totalValueLockedUSD"].pct_change() * 100
df["Volume_Change"] = df["volumeUSD"].pct_change() * 100
df.fillna(0, inplace=True)

# 绘制 TVL 变化趋势
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["totalValueLockedUSD"], label="TVL (USD)", marker="o", linestyle="-")
plt.xlabel("Date")
plt.ylabel("Total Value Locked (USD)")
plt.title("TVL Trend in Uniswap v3 ETH/USDT Pool")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()

# 交易量 vs TVL 相关性
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["totalValueLockedUSD"], y=df["volumeUSD"])
plt.xlabel("TVL (USD)")
plt.ylabel("Trading Volume (USD)")
plt.title("Trading Volume vs. TVL Correlation")
plt.grid()
plt.show()

# 计算 TVL 和交易量的相关性
correlation = df["totalValueLockedUSD"].corr(df["volumeUSD"])
print(f"📊 TVL 与交易量的相关性：{correlation:.2f}")
