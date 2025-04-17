import numpy as np
import matplotlib.pyplot as plt


# Rastrigin函数定义
def rastrigin(X):
    A = 10
    return A * len(X) + sum([(x ** 2 - A * np.cos(2 * np.pi * x)) for x in X])


# 个体初始化
def init_population(pop_size, dim, bound):
    return np.random.uniform(bound[0], bound[1], (pop_size, dim))


# OBL初始化（对称点计算）
def obl_initialization(pop, bound):
    return bound[0] + bound[1] - pop


# 选择操作：轮盘赌
def selection(pop, fitness):
    probs = (1 / (1 + fitness))
    probs /= probs.sum()
    idx = np.random.choice(len(pop), size=len(pop), p=probs)
    return pop[idx]


# 交叉操作：均匀交叉
def crossover(parents, crossover_rate):
    offspring = []
    for i in range(0, len(parents), 2):
        if i + 1 < len(parents) and np.random.rand() < crossover_rate:
            mask = np.random.rand(parents.shape[1]) > 0.5
            child1 = np.where(mask, parents[i], parents[i + 1])
            child2 = np.where(mask, parents[i + 1], parents[i])
            offspring.extend([child1, child2])
        else:
            offspring.extend([parents[i], parents[i + 1]])
    return np.array(offspring)


# 变异操作
def mutation(pop, mutation_rate, bound):
    for i in range(len(pop)):
        if np.random.rand() < mutation_rate:
            dim = np.random.randint(0, pop.shape[1])
            pop[i][dim] = np.random.uniform(bound[0], bound[1])
    return pop


# 反向学习变异
def obl_mutation(pop, bound, mutation_rate):
    for i in range(len(pop)):
        if np.random.rand() < mutation_rate:
            pop[i] = bound[0] + bound[1] - pop[i]
    return pop


# 遗传算法主函数
def run_ga(mode='baseline', pop_size=50, dim=10, generations=100, bound=(-5.12, 5.12),
           crossover_rate=0.9, mutation_rate=0.1):
    # 初始种群
    pop = init_population(pop_size, dim, bound)

    if mode == 'obl_init' or mode == 'obl_all':
        # 添加反向个体
        pop_obl = obl_initialization(pop, bound)
        pop = np.vstack((pop, pop_obl))
        # 选择前pop_size个最优
        fitness = np.array([rastrigin(ind) for ind in pop])
        pop = pop[np.argsort(fitness)[:pop_size]]

    best_fitness_per_gen = []
    for _ in range(generations):
        fitness = np.array([rastrigin(ind) for ind in pop])
        best_fitness_per_gen.append(np.min(fitness))
        parents = selection(pop, fitness)
        offspring = crossover(parents, crossover_rate)

        if mode == 'obl_all':
            offspring = obl_mutation(offspring, bound, mutation_rate)
        else:
            offspring = mutation(offspring, mutation_rate, bound)

        pop = offspring

    # 最后返回最优值
    final_fitness = np.min([rastrigin(ind) for ind in pop])
    return final_fitness, best_fitness_per_gen


# 多次运行实验
def run_experiments(mode, runs=10):
    results = []
    all_history = []
    for _ in range(runs):
        final_fit, history = run_ga(mode=mode)
        results.append(final_fit)
        all_history.append(history)
    return np.array(results), np.array(all_history)


# 运行三组实验
results_baseline, _ = run_experiments('baseline')
results_obl_init, _ = run_experiments('obl_init')
results_obl_all, _ = run_experiments('obl_all')


# 计算统计量
def get_stats(arr):
    return {
        'mean': np.mean(arr),
        'std': np.std(arr),
        'min': np.min(arr),
        'max': np.max(arr)
    }


stats_baseline = get_stats(results_baseline)
stats_obl_init = get_stats(results_obl_init)
stats_obl_all = get_stats(results_obl_all)

print(stats_baseline, stats_obl_init, stats_obl_all)
