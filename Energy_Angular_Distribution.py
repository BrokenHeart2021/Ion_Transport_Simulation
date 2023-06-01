import random
import numpy as np
import matplotlib.pyplot as plt

def simulate_sputter_distribution(num_particles, energy_mean, energy_std, angle_mean, angle_std):
    energies = np.random.normal(energy_mean, energy_std, num_particles)
    angles = np.random.normal(angle_mean, angle_std, num_particles)

    return energies, angles

# 设置模拟参数
num_particles = 100000  # 溅射原子数量
energy_mean = 100  # 能量均值
energy_std = 20  # 能量标准差
angle_mean = 45  # 角度均值
angle_std = 10  # 角度标准差

# 模拟溅射原子到达基面的能量和角度分布
energies, angles = simulate_sputter_distribution(num_particles, energy_mean, energy_std, angle_mean, angle_std)

# 绘制能量分布直方图
plt.hist(energies, bins=50, density=True, alpha=0.7)
plt.xlabel('Energy')
plt.ylabel('Probability')
plt.title('Energy Distribution')
plt.show()

# 绘制角度分布直方图
plt.hist(angles, bins=50, density=True, alpha=0.7)
plt.xlabel('Angle')
plt.ylabel('Probability')
plt.title('Angle Distribution')
plt.show()
