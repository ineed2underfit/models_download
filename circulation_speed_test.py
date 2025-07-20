import requests
import time

proxies = {
    "http": "http://127.0.0.1:7897",
    "https": "http://127.0.0.1:7897"
}

url = "https://huggingface.co"

for i in range(5):
    try:
        r = requests.get(url, proxies=proxies, timeout=10)
        print(f"[{i+1}] 代理连通成功！状态码: {r.status_code}")
    except Exception as e:
        print(f"[{i+1}] 代理无法连接: {e}")
    time.sleep(2)