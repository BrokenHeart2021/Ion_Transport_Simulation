import random

def estimate_sputtering_rate(num_particles, num_collisions):
    particles_deposited = 0

    for _ in range(num_collisions):
        # 模拟碰撞
        if random.random() < 0.1:  # 假设碰撞的概率为0.1，可根据实际情况调整
            particles_deposited += 1

    sputtering_rate = particles_deposited / num_particles
    return sputtering_rate

# 设置模拟参数
num_particles = 100000  # 原始溅射粒子数量
num_collisions = 1000000  # 碰撞次数

# 估算溅射原子的沉淀速率
sputtering_rate = estimate_sputtering_rate(num_particles, num_collisions)
print("估算的溅射原子沉淀速率:", sputtering_rate)
