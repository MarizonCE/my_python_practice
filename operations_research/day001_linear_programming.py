from scipy.optimize import linprog

# 因为linprog默认是最小化目标函数，需取负号，转化为最小化问题
# max z = 8x + 6y 转化为 min z' = -8x - 6y, 到输出结果再取 min z' 的负数
c = [-8, -6]

# A为系数矩阵，b为右边的常数
A = [[2, 1],
     [1, 2]]
b = [100, 80]

# 每个变量的范围：x 和 y 都要 ≥ 0
x_bounds = (0, None)
y_bounds = (0, None)

# 求解线性规划
# method='highs' 是目前推荐的高性能求解器
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# 输出结果
if res.success:
     x,y = res.x
     print(f"最优解：生产A = {x:.2f}个，B = {y:.2f}个")
     print(f"最大利润：{(-res.fun):.2f}元")
else:
     print("没有找到最优解")
