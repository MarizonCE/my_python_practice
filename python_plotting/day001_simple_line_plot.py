import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据
time = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # 时间（小时）
temperature = [22, 23, 21, 20, 19, 18, 17, 16, 15]  # 温度（摄氏度）

# 创建折线图
plt.plot(time, temperature, label='温度随时间变化')

# 添加标题和标签
plt.title('温度随时间变化')
plt.xlabel('时间（小时）')
plt.ylabel('温度（℃）')

# 显示图例
plt.legend()

# 显示图形
plt.show()
