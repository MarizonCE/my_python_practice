from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import numpy as np

# 加载鸢尾花数据（前两个类别）
data = load_iris()
X = data.data[data.target != 2]
y = data.target[data.target != 2]

# 建模
model = LogisticRegression()
model.fit(X,y)

# 预测
print("预测结果：",model.predict(np.array([[5,5,5,5],[1,1,1,1]])))