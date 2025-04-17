import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Rastrigin函数
def rastrigin(X):
    return 20 + X[0]**2 + X[1]**2 - 10 * (np.cos(2 * np.pi * X[0]) + np.cos(2 * np.pi * X[1]))

# 初始化种群：根据 x 分段，y 分不同区间
def init_population(pop_size, bounds):
    pop = []

    for _ in range(pop_size):
        zone = np.random.choice(['left', 'right', 'other'])
        if zone == 'left':
            x = np.random.uniform(-4, -2.5)
            y = np.random.uniform(-5.12, 0)
        elif zone == 'right':
            x = np.random.uniform(2.5, 4)
            y = np.random.uniform(0, 5.12)
        else:
            x = np.random.uniform(-5.12, 5.12)
            y = np.random.uniform(-5.12, -2)
        pop.append([x, y])

    return np.array(pop)


# 适应度函数
def fitness(pop):
    return -np.array([rastrigin(ind) for ind in pop])

# 选择
def select(pop, fit):
    normalized_fit = fit - fit.min() + 1e-6
    probs = normalized_fit / normalized_fit.sum()
    probs = probs ** 0.5
    probs /= probs.sum()
    idx = np.random.choice(len(pop), size=len(pop), p=probs)
    return pop[idx]

# 交叉
def crossover(parents, crossover_rate=0.8):
    offspring = []
    for i in range(0, len(parents), 2):
        p1, p2 = parents[i], parents[(i + 1) % len(parents)]
        if np.random.rand() < crossover_rate:
            alpha = np.random.rand()
            child1 = alpha * p1 + (1 - alpha) * p2
            child2 = (1 - alpha) * p1 + alpha * p2
            offspring.extend([child1, child2])
        else:
            offspring.extend([p1, p2])
    return np.array(offspring)

# 动态变异
def mutate(pop, mutation_rate=0.1, bounds=(-5.12, 5.12), gen=0, total_gen=50):
    scale = 2.0 * (1 - gen / total_gen)
    for ind in pop:
        if np.random.rand() < mutation_rate:
            ind += np.random.uniform(-scale, scale, size=2)
            ind[:] = np.clip(ind, bounds[0], bounds[1])
    return pop

# GA参数
POP_SIZE = 100
N_GENERATIONS = 50
BOUNDS = (-10.24, 10.24)

# 初始化
population = init_population(POP_SIZE, BOUNDS)

# 迭代进化
for gen in range(N_GENERATIONS):
    fit = fitness(population)
    population = select(population, fit)
    population = crossover(population)
    population = mutate(population, gen=gen, total_gen=N_GENERATIONS)

# 可视化
X, Y = population[:, 0], population[:, 1]
mean_x, mean_y = np.mean(X), np.mean(Y)

x_grid = np.linspace(BOUNDS[0], BOUNDS[1], 400)
y_grid = np.linspace(BOUNDS[0], BOUNDS[1], 400)
X_grid, Y_grid = np.meshgrid(x_grid, y_grid)
Z = rastrigin([X_grid, Y_grid])

x_grid = np.linspace(-3, 3, 400)
y_grid = np.linspace(-3, 3, 400)
X_grid, Y_grid = np.meshgrid(x_grid, y_grid)
Z = rastrigin([X_grid, Y_grid])

plt.figure(figsize=(8, 6))
plt.contourf(X_grid, Y_grid, Z, levels=50, cmap='viridis')
plt.colorbar(label='Rastrigin函数值')

# 可选：筛选显示区域内的个体
mask = (X >= -3) & (X <= 3) & (Y >= -3) & (Y <= 3)
X, Y = X[mask], Y[mask]

plt.scatter(X, Y, c='red', edgecolors='k', s=60, label='最终个体分布')
plt.scatter(0, 0, marker='*', s=240, c='yellow', edgecolors='k', label='全局最优点 (0,0)')
plt.scatter(mean_x, mean_y, s=80, c='white', edgecolors='black', label='收敛中心')
circle = plt.Circle((mean_x, mean_y), 0.5, color='white', fill=False, linestyle='--', linewidth=2)
plt.gca().add_patch(circle)

plt.xlim(-3, 3)
plt.ylim(-3, 3)

plt.text(mean_x + 0.6, mean_y + 0.6, '陷入局部最优区域', fontsize=12, color='white')

plt.title("遗传算法陷入局部最优的示意图", fontsize=14)
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.tight_layout()
plt.show()

