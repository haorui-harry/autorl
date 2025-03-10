class UniversalGymWrapper(gym.Wrapper):
    """通用的 Gym 环境包装器，使用 LLM 生成的奖励函数"""
    def __init__(self, env_name: str, reward_code: str):
        super().__init__(gym.make(env_name))
        self.original_reward = 0.0
        self.custom_reward = 0.0
        
        # 动态执行生成的奖励代码
        exec(reward_code, globals())
        self.reward_function = locals()['custom_reward']

    def step(self, action):
        obs, original_reward, done, info = self.env.step(action)
        self.original_reward = original_reward
        self.custom_reward = self.reward_function(obs)
        info['original_reward'] = original_reward
        return obs, self.custom_reward, done, info

# 使用示例
if __name__ == "__main__":
    ENV_NAME = 'LunarLander-v2'  # 可替换为其他环境
    TASK_DESCRIPTION = "训练一个智能体以成功着陆，最大化着陆的稳定性。"
    
    # 获取环境描述
    env_desc = get_env_description(ENV_NAME)
    if env_desc is None:
        print("无法获取环境描述，程序退出")
        exit()
    print(f"环境描述: {env_desc}")
    
    # 生成奖励函数
    reward_code = generate_reward_function(env_desc)
    print("\n生成的奖励函数：")
    print(reward_code)
    
    # 初始化环境
    env = UniversalGymWrapper(ENV_NAME, reward_code)
    
    # 生成算法代码
    algorithm_code = generate_algorithm_code(env_desc, TASK_DESCRIPTION)
    print("\n生成的算法代码：")
    print(algorithm_code)
    
    # 执行生成的算法代码
    try:
        exec(algorithm_code, globals())
        # 假设生成的代码中有一个名为 'train_agent' 的函数
        train_agent(env)
    except Exception as e:
        print(f"错误：无法执行算法代码 - {e}")
    
    env.close()