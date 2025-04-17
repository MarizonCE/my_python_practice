import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义 Rastrigin 函数
def rastrigin(X, Y):
    A = 10
    return A * 2 + (X**2 - A * np.cos(2 * np.pi * X)) + (Y**2 - A * np.cos(2 * np.pi * Y))

# 创建网格坐标
x = np.linspace(-5.12, 5.12, 400)
y = np.linspace(-5.12, 5.12, 400)
X, Y = np.meshgrid(x, y)
Z = rastrigin(X, Y)

# 创建图形，分为两个子图
fig = plt.figure(figsize=(14, 6))

# ---------- 子图1：3D 图 ----------
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
surf = ax1.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none', alpha=0.9)
ax1.set_title('Rastrigin函数（3D）', fontsize=14)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('f(X, Y)')
ax1.view_init(elev=25, azim=135)
ax1.set_zlim(0, 80)
ax1.scatter(0, 0, rastrigin(0, 0), color='cyan', s=50, label='全局最优解点')
ax1.legend()

# ---------- 子图2：俯视等高线图 ----------
ax2 = fig.add_subplot(1, 2, 2)
contour = ax2.contourf(X, Y, Z, levels=50, cmap='inferno')
ax2.set_title('Rastrigin函数 - 上方视角', fontsize=14)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.plot(0, 0, 'c*', markersize=10, label='Global Minimum')
ax2.legend()
fig.colorbar(contour, ax=ax2, shrink=0.8)

plt.tight_layout()
plt.show()
