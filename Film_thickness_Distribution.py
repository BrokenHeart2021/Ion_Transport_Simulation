import random
import numpy as np
import matplotlib.pyplot as plt

def simulate_film_thickness(num_particles, mean_thickness, thickness_std):
    film_thicknesses = np.random.normal(mean_thickness, thickness_std, num_particles)
    return film_thicknesses

# 设置模拟参数
num_particles = 100000  # 溅射原子数量
mean_thickness = 100  # 成膜厚度均值
thickness_std = 10  # 成膜厚度标准差

# 模拟溅射原子的成膜厚度均匀性
film_thicknesses = simulate_film_thickness(num_particles, mean_thickness, thickness_std)

# 绘制成膜厚度分布直方图
plt.hist(film_thicknesses, bins=50, density=True, alpha=0.7)
plt.xlabel('Film Thickness')
plt.ylabel('Probability')
plt.title('Film Thickness Distribution')
plt.show()
