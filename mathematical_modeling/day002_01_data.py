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
print(df)
