from huggingface_hub import snapshot_download
import os

# 设置系统代理（可选：如果你未设置系统环境变量）
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7897"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7897"

model_path = snapshot_download(
    repo_id="Qwen/Qwen3-14B-AWQ",
    cache_dir="E:/large_language_models",
    force_download=False,        # 不重复下载
    resume_download=True,        # 自动断点续传
    proxies={
        "http": "http://127.0.0.1:7897",
        "https": "http://127.0.0.1:7897"
    }
)
print(f"✅ 模型下载完成: {model_path}")
