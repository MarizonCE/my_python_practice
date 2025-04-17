import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Schwefel函数定义
def schwefel(X, Y):
    return 418.9829 * 2 - (X * np.sin(np.sqrt(np.abs(X))) + Y * np.sin(np.sqrt(np.abs(Y))))

# 选取合适的绘图范围（让最优点在中心）：[-500, 500]
x = np.linspace(-500, 500, 500)
y = np.linspace(-500, 500, 500)
X, Y = np.meshgrid(x, y)
Z = schwefel(X, Y)

# 生成图像
fig = plt.figure(figsize=(14, 6))

# 3D 图
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
surf = ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', rstride=10, cstride=10, alpha=0.9)
ax1.set_title('Schwefel 函数（3D图）', fontsize=14)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('f(X,Y)')
fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=10)

# 等高线图
ax2 = fig.add_subplot(1, 2, 2)
contour = ax2.contourf(X, Y, Z, levels=50, cmap='viridis')
ax2.set_title('Schwefel 函数（等高线图）', fontsize=14)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
fig.colorbar(contour, ax=ax2)

# 最优点位置标记（420.9687, 420.9687）
opt_x, opt_y = 420.9687, 420.9687
ax1.scatter(opt_x, opt_y, schwefel(opt_x, opt_y), color='red', s=50, label='全局最优点')
ax1.legend()
ax2.plot(opt_x, opt_y, 'ro', markersize=5, label='全局最优点')
ax2.legend()

plt.tight_layout()
plt.show()
