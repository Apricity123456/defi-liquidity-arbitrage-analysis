import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# 读取数据
df = pd.read_csv("../data/uniswap_liquidity_analysis.csv")
df["date"] = pd.to_datetime(df["date"])

# 绘制 TVL 变化趋势
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["total_liquidity_added"], label="Liquidity Added", linestyle="-", marker="o")
plt.plot(df["date"], df["total_liquidity_removed"], label="Liquidity Removed", linestyle="--", marker="x")
plt.xlabel("Date")
plt.ylabel("Liquidity (ETH)")
plt.title("Uniswap v3 Liquidity Change Trend")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
#  保存 TVL 变化图
plt.savefig("../image/tvl_trend.png")
plt.close()

# 绘制交易量趋势
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["total_trading_volume"], label="Trading Volume", linestyle="-", marker="s")
plt.xlabel("Date")
plt.ylabel("Volume (ETH)")
plt.title("Uniswap v3 Trading Volume Trend")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
#  保存交易量变化图
plt.savefig("../image/trading_volume_trend.png")
plt.close()
#绘制 资金利用率 随时间变化
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["utilization_rate"], label="Utilization Rate", linestyle="-", marker="o")
plt.xlabel("Date")
plt.ylabel("Utilization Rate (%)")
plt.title("Liquidity Utilization Rate Trend")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))

plt.savefig("../image/utilization_rate_trend.png")
plt.close()


print(" 图表已保存到 image/ 目录下：tvl_trend.png, trading_volume_trend.png,utilization_rate_trend.png")
