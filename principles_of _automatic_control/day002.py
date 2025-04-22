import matplotlib.pyplot as plt

# 模拟时间
time = range(50)

# 设定目标温度
target_temp = 26

# 开环控制：不考虑当前温度，固定加热功率
open_loop_temp = []
temp = 20
for t in time:
    temp += 0.5  # 每次加0.5度
    open_loop_temp.append(temp)

# 闭环系统：根据与目标的误差动态调整加热量
closed_loop_temp = []
temp = 20
for t in time:
    error = target_temp - temp
    temp += 0.2 * error  # 加热量与误差成比例
    closed_loop_temp.append(temp)

# 绘图比较
plt.plot(time, open_loop_temp, label="Open-loop")
plt.plot(time, closed_loop_temp, label="Closed-loop")
plt.axhline(y=26, color='gray', linestyle='--', label="Target Temp")
plt.xlabel("Time")
plt.ylabel("Temperature(℃)")
plt.title("Open-loop vs Closed-loop Control")
plt.legend()
plt.grid(True)
plt.show()
