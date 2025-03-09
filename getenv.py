import gym
import openai



def get_env_description(env_name):
    prompt = f"""
    Please provide a description of the Gym environment '{env_name}' in the following format:
    {{
        'state': ['variable1', 'variable2', ...],
        'action': ['action1', 'action2', ...],
        'goal': 'brief goal description'
    }}
    For example, for 'CartPole-v1', it would be:
    {{
        'state': ['cart_position', 'cart_velocity', 'pole_angle', 'pole_velocity'],
        'action': ['left', 'right'],
        'goal': 'keep the pole upright and the cart near the center'
    }}
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.5
    )

    # 提取生成的描述并转换为字典
    desc_text = response.choices[0].text.strip()
    try:
        env_desc = eval(desc_text)
        return env_desc
    except Exception as e:
        print(f"错误：无法解析环境描述 - {e}")
        return None




