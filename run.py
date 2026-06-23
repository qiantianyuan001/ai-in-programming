# CLI对话版deepseek
# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

# 配置
api_key=os.environ.get('DEEPSEEK_API_KEY')   # API Key
base_url="https://api.deepseek.com"             # API URL
model = "deepseek-v4-flash"                     # 模型名称
system_prompt = "你是一个AI助手，请用中文回答用户的问题。"  # 基础设定
# config
create_config = {
    # "reasoning_effort":"high",
    # "extra_body":{"thinking": {"type": "enabled"}}
}

# 初始化
client = OpenAI(
    api_key=api_key,
    base_url=base_url
    )
messages = [
    {"role": "system", "content": system_prompt},
    ]

# 开始对话
for i in range(10): 
    content_input = input(">> ")
    if content_input == "exit":
        break
    messages.append({"role": "user", "content": content_input})
    # 调用模型
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        **create_config,
    )
    messages.append(response.choices[0].message)
    print(response.choices[0].message.content)