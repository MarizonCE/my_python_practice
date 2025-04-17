import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 算法名称
algorithms = ['基本遗传算法', 'OBL 遗传算法']

# 平均值和标准差
means = np.array([363.14, 272.64])
stds = np.array([91.29, 88.02])

# x轴位置
x = np.arange(len(algorithms))
width = 0.6  # 柱宽

# 创建图形窗口
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制条形图，添加误差棒
bars = ax.bar(x, means, width, yerr=stds, capsize=10,
              color=['#6BAED6', '#74C476', '#FD8D3C'],
              edgecolor='black', error_kw=dict(ecolor='black', lw=2))

# 设置标题和坐标轴
ax.set_title('不同算法的平均适应度及标准差', fontsize=14)
ax.set_ylabel('Fitness 值（越低越好）', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(algorithms, fontsize=11)
ax.set_ylim(0, max(means + stds)*1.1)  # 留出空间显示误差棒

# 添加数据标签（显示平均值 ± 标准差）
for i in range(len(x)):
    ax.text(x[i], means[i] + stds[i] + 0.5, f'{means[i]:.2f}±{stds[i]:.2f}',
            ha='center', va='bottom', fontsize=10)

# 添加网格线
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
