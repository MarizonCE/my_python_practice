import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 搜索边界
a, b = -5, 5
n = 5  # 个体数量

# 随机个体
np.random.seed(0)
x = np.random.uniform(a, b, size=(n, 2))
x_opp = a + b - x  # OBL公式

# 绘图
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(a, b)
ax.set_ylim(a, b)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_title("个体与反向个体位置示意（2D）")

# 原始个体与反向个体
ax.scatter(x[:, 0], x[:, 1], c='red', label='个体 x')
ax.scatter(x_opp[:, 0], x_opp[:, 1], c='blue', label='反向个体 $x_{opp}$')

# 连线
for i in range(n):
    ax.plot([x[i, 0], x_opp[i, 0]], [x[i, 1], x_opp[i, 1]], 'gray', linestyle='dotted')

ax.legend()
plt.grid(True)
plt.show()
