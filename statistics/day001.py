import numpy as np

lengths = [10.1, 9.9, 10.0, 10.2, 10.1, 9.8, 10.0, 9.9, 10.1, 10.0]
mean = np.mean(lengths)
std_dev = np.std(lengths)

print(f"平均长度：{mean:.2f} mm")
print(f"标准差：{std_dev:.2f} mm")