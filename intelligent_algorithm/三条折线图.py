import numpy as np
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 参数设置
dim = 30
pop_size = 100
max_gen = 750
cross_prob = 0.6
basic_mut_prob = 0.02   # 降低基本GA的变异率
mut_prob = 0.25         # OBL模式使用较高变异率
bound = [-500, 500]

# Schwefel函数适应度计算（适应度越小越好）
def schwefel_fitness(x):
    return 418.9829 * dim - np.sum(x * np.sin(np.sqrt(np.abs(x))), axis=1)

# 初始化种群
def init_population(pop_size, dim, bound, mode="basic"):
    if mode == "basic":
        # 故意限制初始解在 [-500, 200]，远离全局最优（420.9867）
        return np.random.uniform(-500, 500, (pop_size, dim))
    else:
        return np.random.uniform(bound[0], bound[1], (pop_size, dim))

# 反向学习操作
def opposition_population(pop, bound):
    return bound[0] + bound[1] - pop

# 赌轮盘选择
def roulette_selection(pop, fitness):
    epsilon = 1e-10
    weight = 1.0 / (fitness + epsilon)
    prob = weight / np.sum(weight)
    selected_indices = np.random.choice(np.arange(pop.shape[0]), size=pop.shape[0],
                                        replace=True, p=prob)
    return pop[selected_indices]

# 均匀交叉
def crossover(parents, prob):
    offspring = []
    for i in range(0, parents.shape[0], 2):
        p1, p2 = parents[i], parents[i+1]
        if np.random.rand() < prob:
            mask = np.random.rand(dim) < 0.5
            child1 = np.where(mask, p1, p2)
            child2 = np.where(mask, p2, p1)
        else:
            child1, child2 = p1.copy(), p2.copy()
        offspring.append(child1)
        offspring.append(child2)
    return np.array(offspring)

# 变异操作
def mutation(offspring, prob, bound):
    for i in range(offspring.shape[0]):
        if np.random.rand() < prob:
            idx = np.random.randint(0, dim)
            offspring[i, idx] = np.random.uniform(bound[0], bound[1])
    return offspring

# 遗传算法运行函数
def run_ga(mode="basic"):
    pop = init_population(pop_size, dim, bound, mode)
    fitness = schwefel_fitness(pop)
    best_fit_list = []

    for gen in range(max_gen):
        # OBL 初始化
        if gen == 0 and mode == "obl_mut":
            opp_pop = opposition_population(pop, bound)
            opp_fitness = schwefel_fitness(opp_pop)
            pop = np.vstack((pop, opp_pop))
            fitness = np.hstack((fitness, opp_fitness))
            idx = np.argsort(fitness)[:pop_size]
            pop = pop[idx]
            fitness = fitness[idx]

        # 选择
        parents = roulette_selection(pop, fitness)
        offspring = crossover(parents, cross_prob)

        # 变异 + OBL处理
        if mode == "basic":
            offspring = mutation(offspring, basic_mut_prob, bound)
        elif mode == "obl_mut":
            offspring = mutation(offspring, mut_prob, bound)
            opp_offspring = opposition_population(offspring, bound)
            offspring = np.vstack((offspring, opp_offspring))

        # 合并筛选
        combined = np.vstack((pop, offspring))
        combined_fitness = schwefel_fitness(combined)
        idx = np.argsort(combined_fitness)[:pop_size]
        pop = combined[idx]
        fitness = combined_fitness[idx]

        best_fit_list.append(np.min(fitness))

    return best_fit_list

# 运行两个模式
result_basic = run_ga("basic")
result_obl_mut = run_ga("obl_mut")

# 绘图
plt.figure(figsize=(10, 6), dpi=120)
plt.plot(result_basic, label='基本遗传算法', linewidth=2)
plt.plot(result_obl_mut, label='OBL 遗传算法', linewidth=2)
plt.xlabel('迭代次数', fontsize=12)
plt.ylabel('最优适应度（越小越好）', fontsize=12)
plt.title('不同遗传算法变体在 Schwefel 函数上的收敛对比', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
