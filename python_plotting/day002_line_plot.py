import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 时间轴
time = list(range(9))  # 0~8点

# 设备A和设备B的温度显示
temp_A = [22, 23, 21, 20, 21, 22, 23, 24, 23]
temp_B = [20, 21, 20, 19, 18, 17, 17, 18, 19]

# 绘制两条折线
plt.plot(time, temp_A, label='Device A', color='blue', linestyle='-')  # color设置折线的颜色，linestyle设置折线的线型，'-'为实线
plt.plot(time, temp_B, label='Device B', color='red', linestyle='--')  # '--'为虚线

# 添加标题和轴标签
plt.title('两台设备的温度对比')
plt.xlabel('时间（小时）')
plt.ylabel('温度（℃）')

# 图例和网格线
plt.legend()
plt.grid(True)

# 显示图形
plt.show()
