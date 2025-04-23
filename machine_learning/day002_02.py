from sklearn.cluster import KMeans
import numpy as np

# 假设每个人的数据是[年龄, 月消费金额]
X = np.array([[15, 300], [40, 800], [22, 200], [35, 900]])

# 聚成两类
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

# 每个数据点的类别
print("聚类标签：",kmeans.labels_)
