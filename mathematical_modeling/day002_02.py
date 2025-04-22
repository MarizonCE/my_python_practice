from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd

# 构造简单数据集（模拟7天数据）
data = {
    'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'temperature': [22, 25, 24, 23, 20, 18, 19],  # 摄氏度
    'weather': ['sunny', 'cloudy', 'rainy', 'sunny', 'rainy', 'sunny', 'cloudy'],
    'wind_speed': [10, 12, 20, 8, 18, 7, 11],  # km/h
    'is_workday': [1, 1, 1, 1, 1, 0, 0],  # 是否工作日
    'bike_count': [320, 300, 180, 350, 200, 400, 310]  # 实际租赁数量
}

df = pd.DataFrame(data)

# 特征变量
X = df[['temperature', 'wind_speed', 'weather', 'is_workday']]
y = df['bike_count']

# 使用one-hot对weather进行编码
# sunny,cloudy,rainy -> 会变成三列 [1,0,0],[0,1,0],[0,0,1]
# ColumnTransformer 可以只对某些列做预处理，其他保持不变
preprocessor = ColumnTransformer(
    transformers=[
        ('weather_ohe', OneHotEncoder(), ['weather'])
    ],
    remainder='passthrough'  # 其他变量保持原样
)

# 建模管道：预处理+回归模型，形成一个完整的流程
model = Pipeline(steps=[
    ('preprocess', preprocessor),  # 预处理
    ('regressor', LinearRegression())  # 线性回归建模
])

# 拟合模型
model.fit(X, y)

# 预测结果
y_pred = model.predict(X)
print("\n预测结果：")
for real, pred in zip(y, y_pred):
    print(f"实际：{real:.0f}，预测：{pred:.1f}")
