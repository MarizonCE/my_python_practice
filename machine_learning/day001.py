from sklearn.linear_model import LinearRegression
import numpy as np

# 训练数据（房子面积和价格）
X = np.array([[30], [50], [70], [90]])  # 面积（平方米）
y = np.array([100, 150, 200, 250])  # 价格（万元）

# 建立模型
model = LinearRegression()
model.fit(X,y)

# 预测一个新房子的价格
predicted_price = model.predict([[60],[80]])
print(f"预测的价格为：{predicted_price[0]:.2f}万元和{predicted_price[1]:.2f}万元")

