import pandas as pd


df = pd.read_csv("../data/uniswap_liquidity_data_cleaned.csv")
df["date"] = pd.to_datetime(df["date"])


df["liquidity_change"] = df["total_liquidity_added"] - df["total_liquidity_removed"]
df["liquidity_change_rate"] = df["liquidity_change"].pct_change() * 100  # 计算变化率


df["TVL_change_rate"] = df["total_liquidity_added"].pct_change() * 100
df["TVL_change_rate"] = df["TVL_change_rate"].fillna(0)  # 处理 NaN 值


df["fee_revenue"] = df["total_trading_volume"] * 0.003  # 交易量 * 0.3%


df["utilization_rate"] = (df["total_trading_volume"] / df["total_liquidity_added"]) * 100
df["utilization_rate"] = df["utilization_rate"].replace([float("inf"), -float("inf")], 0).fillna(0)  # 处理 NaN 和 Inf


df["TVL_change_rate_norm"] = (df["TVL_change_rate"] - df["TVL_change_rate"].min()) / (df["TVL_change_rate"].max() - df["TVL_change_rate"].min())
df["utilization_rate_norm"] = (df["utilization_rate"] - df["utilization_rate"].min()) / (df["utilization_rate"].max() - df["utilization_rate"].min())
df["fee_revenue_norm"] = (df["fee_revenue"] - df["fee_revenue"].min()) / (df["fee_revenue"].max() - df["fee_revenue"].min())


df["health_score"] = (df["TVL_change_rate_norm"] * 0.3) + (df["utilization_rate_norm"] * 0.5) + (df["fee_revenue_norm"] * 0.2)
df["health_score"] = df["health_score"].rank(pct=True) * 100  # 归一化到 0-100


df.drop(columns=["TVL_change_rate_norm", "utilization_rate_norm", "fee_revenue_norm"], inplace=True)

df.to_csv("../data/uniswap_liquidity_analysis.csv", index=False)

print(" 流动性分析完成，已保存到 data/uniswap_liquidity_analysis.csv")
