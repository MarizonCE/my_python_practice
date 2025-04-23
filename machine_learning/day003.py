from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 加载数据
data = load_iris()
X,y = data.data,data.target

# 先划分训练+临时验证测试集（80%+20%）
X_train,X_temp,y_train,y_temp = train_test_split(X,y,test_size=0.2,random_state=42)

# 再把临时集分成验证集和测试集（各10%）
X_val,X_test,y_val,y_test = train_test_split(X_temp,y_temp,test_size=0.5,random_state=42)

print(f"训练集大小：{len(X_train)}")
print(f"验证集大小：{len(X_val)}")
print(f"测试集大小：{len(X_test)}")

print(X_val)