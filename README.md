# defi-liquidity-arbitrage-analysis
#  DeFi Liquidity & Arbitrage Analysis 

##  项目介绍
本项目分析了去中心化交易所（DEX）Uniswap v3 的资金池流动性，并探讨了 Uniswap 与 SushiSwap 之间的套利机会。

- **版本 1**：流动性分析（TVL、交易量、资金池变化趋势）
- **版本 2**：套利分析（实时价格监测、价格差套利空间计算）

##  数据来源
- **The Graph API**：获取 Uniswap v3 的资金池数据
- **Dune Analytics SQL**：获取 DeFi 交易量和 TVL 变化
- **SushiSwap API**：获取实时市场价格，计算套利空间

##  技术栈
- **Python**: `pandas`, `matplotlib`, `requests`, `web3.py`
- **SQL**: `Dune Analytics`
- **Blockchain API**: `Uniswap v3 Graph API`, `SushiSwap API`

##  项目内容
### **1️资金池流动性分析**
📌 `notebooks/01_liquidity_analysis.ipynb`
- Uniswap v3 TVL 变化趋势
- 交易量 vs TVL 相关性分析
- 资金流入流出趋势

### **2️ DEX 套利分析**
📌 `notebooks/02_arbitrage_analysis.ipynb`
- Uniswap vs SushiSwap 价格对比
- 计算套利空间（百分比差值）
- 套利窗口趋势分析（何时最适合套利？）

##  运行代码
```bash
# 安装依赖
pip install -r requirements.txt

# 运行数据抓取脚本
python src/fetch_data.py


