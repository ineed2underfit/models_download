import os
from huggingface_hub import snapshot_download

print("⚙️ 正在连接 Hugging Face 服务器，请耐心等待...")

model_path = snapshot_download(
    # repo_id="Qwen/Qwen3-14B-AWQ",                # 模型地址
    repo_id="Qwen/Qwen2.5-Coder-14B-Instruct-GPTQ-Int8",                # 模型地址
    cache_dir="E:/large_language_models",    # 本地保存路径
    resume_download=True,                    # 支持断点续传
    force_download=False,  # 必须为 False
    # proxies={                                # 设置代理
    #     "http": "http://127.0.0.1:7897",
    #     "https": "http://127.0.0.1:7897"
    # },
    mirror="https://mirrors.tuna.tsinghua.edu.cn/hugging-face-mirror"  # 镜像源
)
print(f"✅ 模型已下载至: {model_path}")
