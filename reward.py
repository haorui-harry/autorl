import gym
import openai


def get_reward_function_code(env_desc):
    state_vars = env_desc['state']
    goal = env_desc['goal']

    prompt = f"""
    Based on the following environment description:
    State variables: {state_vars}
    Goal: {goal}

    Please provide a Python function named 'calculate_reward' that takes 'next_state' (a list or array with {len(state_vars)} elements), 'done', and 'terminated' as inputs, and returns a float reward value.
    The function should encourage the specified goal.
    Example format:
    def calculate_reward(next_state, done, terminated):
        # Your code here
        return reward
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.5
    )

    # 返回生成的函数代码
    return response.choices[0].text.strip()
