import requests
import pandas as pd

# ✅ 你的 API Key（请替换为你的真实 API Key）
API_KEY = "b5IQq67mMdVlam0dvquk8SlEX2M1w21i"

# ✅ 你的查询 ID（请替换为你的 Query ID）
QUERY_ID = "4766410"

# ✅ Dune API 端点
url = f"https://api.dune.com/api/v1/query/{QUERY_ID}/results"

# ✅ 设置请求头
headers = {
    "x-dune-api-key": API_KEY
}

# ✅ 发送 GET 请求
response = requests.get(url, headers=headers)

# ✅ 处理响应
if response.status_code == 200:
    data = response.json()

    # ✅ 提取 rows 数据（查询结果）
    rows = data["result"]["rows"]

    # ✅ 转换为 Pandas DataFrame
    df = pd.DataFrame(rows)

    # ✅ 存储 CSV 文件
    csv_path = "../data/uniswap_data.csv"
    df.to_csv(csv_path, index=False, encoding="utf-8")

    print(f"✅ 数据已成功保存到 {csv_path}")
else:
    print(f"❌ 请求失败: {response.status_code}, {response.text}")
