import json
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import base64

class RLExperimentSimulator:
    def __init__(self):
        self.episode_data = {
            'states': [],
            'rewards': [],
            'logs': [],
            'env_images': []
        }
        
    def generate_sample_data(self, num_episodes=200):
        """生成模拟实验数据"""
        # 生成奖励曲线数据
        self.episode_data['rewards'] = [
            np.clip(50 + 5*ep + np.random.normal(0, 30 if ep<50 else 10), 0, 500)
            for ep in range(num_episodes)
        ]
        
        # 生成状态数据示例
        self.episode_data['states'].append({
            'cart_position': 0.02,
            'cart_velocity': -0.15,
            'pole_angle': 0.03,
            'pole_angular_velocity': 0.10
        })
        
        # 生成日志条目
        self.episode_data['logs'].extend([
            {'episode': 50, 'reward': 150, 'loss': 0.045, 'lr': 0.001},
            {'episode': 150, 'reward': 200, 'loss': 0.012, 'lr': 0.001}
        ])
        
        # 生成模拟环境截图（实际应用中替换为真实图像）
        self._generate_env_visualization()
        
    def _generate_env_visualization(self):
        """生成模拟环境可视化（实际应用可替换为真实渲染）"""
        fig, ax = plt.subplots(figsize=(4,3))
        ax.text(0.5, 0.5, "模拟环境：小车左倾\n杆角度≈5°", ha='center')
        ax.axis('off')
        fig.savefig('env_snapshot.png', bbox_inches='tight')
        plt.close()
        with open("env_snapshot.png", "rb") as image_file:
            self.episode_data['env_images'].append(base64.b64encode(image_file.read()).decode())
        
    def send_to_analysis_api(self):
        """模拟发送数据到多模态分析API"""
        analysis_result = {
            'reward_analysis': {
                'issue': "奖励未达到最大值（500），后期稳定在200左右",
                'causes': [
                    "学习率可能过低（0.001）",
                    "探索策略衰减过快"
                ]
            },
            'state_analysis': {
                'issue': "保守控制策略（角速度偏低）",
                'causes': [
                    "奖励函数侧重短期平衡",
                    "策略网络陷入局部最优"
                ]
            },
            'env_analysis': {
                'issue': "动作模式单一（持续左倾调整）", 
                'causes': [
                    "动作空间探索不足",
                    "初始状态多样性不足"
                ]
            },
            'suggestions': [
                "逐步衰减学习率（0.01 -> 0.0001）",
                "增加探索噪声（如Ornstein-Uhlenbeck过程）",
                "在奖励函数中加入位置偏移惩罚",
                "将训练回合增加至500+"
            ]
        }
        return analysis_result

# 使用示例 ---------------------------------------------------
if __name__ == "__main__":
    # 初始化实验模拟器
    simulator = RLExperimentSimulator()
    simulator.generate_sample_data()
    
    print("=== 发送多模态实验数据到分析API ===")
    print(f"状态数据示例：{simulator.episode_data['states'][0]}")
    print(f"日志条目：{json.dumps(simulator.episode_data['logs'], indent=2)}")
    print("环境截图已编码：", len(simulator.episode_data['env_images'][0]), "字符")
    
    print("\n=== 接收API分析结果 ===")
    analysis = simulator.send_to_analysis_api()
    
    print("\n[奖励曲线分析]")
    print(f"问题：{analysis['reward_analysis']['issue']}")
    print("可能原因：" + "\n       ".join(analysis['reward_analysis']['causes']))
    
    print("\n[状态数据分析]")
    print(f"问题：{analysis['state_analysis']['issue']}")
    print("可能原因：" + "\n       ".join(analysis['state_analysis']['causes']))
    
    print("\n[环境可视化分析]")
    print(f"问题：{analysis['env_analysis']['issue']}")
    print("可能原因：" + "\n       ".join(analysis['env_analysis']['causes']))
    
    print("\n[改进建议]")
    for i, suggestion in enumerate(analysis['suggestions'], 1):
        print(f"{i}. {suggestion}")
