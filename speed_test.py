import requests
proxies = {
    "http": "http://127.0.0.1:7897",
    "https": "http://127.0.0.1:7897"
}

try:
    resp = requests.get("https://huggingface.co", proxies=proxies, timeout=10)
    print(f"状态码: {resp.status_code}，连接成功！")
except Exception as e:
    print(f"连接失败: {e}")
