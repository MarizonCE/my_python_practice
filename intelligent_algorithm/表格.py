import numpy as np

# 参数设置
dim = 30
pop_size = 100
max_gen = 750
cross_prob = 0.8
basic_mut_prob = 0.02
mut_prob = 0.025
bound = [-500, 500]

def schwefel_fitness(x):
    return 418.9829 * dim - np.sum(x * np.sin(np.sqrt(np.abs(x))), axis=1)

def init_population(pop_size, dim, bound):
    return np.random.uniform(bound[0], bound[1], (pop_size, dim))

def opposition_population(pop, bound):
    return bound[0] + bound[1] - pop

def roulette_selection(pop, fitness):
    epsilon = 1e-10
    weight = 1.0 / (fitness + epsilon)
    prob = weight / np.sum(weight)
    selected_indices = np.random.choice(np.arange(pop.shape[0]), size=pop.shape[0], replace=True, p=prob)
    return pop[selected_indices]

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

def mutation(offspring, prob, bound):
    for i in range(offspring.shape[0]):
        if np.random.rand() < prob:
            idx = np.random.randint(0, dim)
            offspring[i, idx] = np.random.uniform(bound[0], bound[1])
    return offspring

def run_ga(mode="basic"):
    pop = init_population(pop_size, dim, bound)
    fitness = schwefel_fitness(pop)

    for gen in range(max_gen):
        if gen == 0 and mode == "obl_mut":
            opp_pop = opposition_population(pop, bound)
            opp_fitness = schwefel_fitness(opp_pop)
            pop = np.vstack((pop, opp_pop))
            fitness = np.hstack((fitness, opp_fitness))
            idx = np.argsort(fitness)[:pop_size]
            pop = pop[idx]
            fitness = fitness[idx]

        parents = roulette_selection(pop, fitness)
        offspring = crossover(parents, cross_prob)

        if mode == "basic":
            offspring = mutation(offspring, basic_mut_prob, bound)
        elif mode == "obl_mut":
            offspring = mutation(offspring, mut_prob, bound)
            opp_offspring = opposition_population(offspring, bound)
            offspring = np.vstack((offspring, opp_offspring))

        combined = np.vstack((pop, offspring))
        combined_fitness = schwefel_fitness(combined)
        idx = np.argsort(combined_fitness)[:pop_size]
        pop = combined[idx]
        fitness = combined_fitness[idx]

    return np.min(fitness)

# 对两个算法进行20次实验并记录最优适应度
results_basic = [run_ga("basic") for _ in range(20)]
results_obl   = [run_ga("obl_mut") for _ in range(20)]

# 计算统计量
def summarize(results):
    avg = np.mean(results)
    std = np.std(results)
    best = np.min(results)
    worst = np.max(results)
    return [avg, std, best, worst]

summary_basic = summarize(results_basic)
summary_obl   = summarize(results_obl)

# 输出结果
print("基本遗传算法统计结果：")
print(summary_basic)
print("OBL遗传算法统计结果：")
print(summary_obl)
