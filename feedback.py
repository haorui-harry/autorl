prompt = f"""
旧的奖励函数：
{old_reward_code}

实验结果：
- 平均奖励：{metrics['average_reward']}
- 最大奖励：{metrics['max_reward']}
- 成功率：{metrics['success_rate']}

请分析旧的奖励函数和实验结果，提出改进建议，并生成一个新的奖励函数。
新奖励函数应：
1. 解决旧函数可能存在的问题（例如过于简单或缺乏引导）。
2. 提升智能体的表现。
3. 提供Python代码，函数签名为 def new_reward(obs: np.ndarray) -> float:
"""



import openai
with open('old_reward.py', 'r') as file:
    old_reward_code = file.read()
# 设置API密钥
openai.api_key = 'your-api-key'  # 请替换为您的实际API密钥

# 调用LLM API
response = openai.Completion.create(
    engine="text-davinci-003",  # 或其他可用模型
    prompt=prompt,
    max_tokens=500,
    temperature=0.5
)

# 提取生成的新奖励函数代码
new_reward_code = response.choices[0].text.strip()
print("生成的新奖励函数：")
print(new_reward_code)

with open('new_reward.py', 'w') as file:
    file.write(new_reward_code)