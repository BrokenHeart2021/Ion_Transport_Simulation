import random
import math
import matplotlib.pyplot as plt

def simulate_ion_transport(num_ions, num_steps, step_size):
    ion_positions = []

    for _ in range(num_ions):
        x = 0
        y = 0

        for _ in range(num_steps):
            # 随机选择运动的角度
            angle = random.uniform(0, 2 * math.pi)

            # 计算步长
            dx = step_size * math.cos(angle)
            dy = step_size * math.sin(angle)

            # 更新离子的位置
            x += dx
            y += dy

            # 模拟碰撞过程
            if random.random() < 0.1:  # 碰撞的概率为0.1，可根据实际情况调整
                # 碰撞后改变离子的方向
                angle = random.uniform(0, 2 * math.pi)
                dx = step_size * math.cos(angle)
                dy = step_size * math.sin(angle)
                x += dx
                y += dy

        ion_positions.append((x, y))

    return ion_positions

# 设置模拟参数
num_ions = 100  # 离子数量
num_steps = 1000  # 步数
step_size = 1  # 步长

# 模拟离子传输与碰撞的过程
positions = simulate_ion_transport(num_ions, num_steps, step_size)

# 绘制离子传输轨迹
for pos in positions:
    x, y = pos
    plt.plot(x, y, 'o')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ion Transport')
plt.show()
