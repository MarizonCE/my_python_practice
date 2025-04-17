import random

# 参数设置
POP_SIZE = 20  # 种群大小 20 个
GENES = 10  # 染色体长度 10 位二进制
CROSS_RATE = 0.8  # 交叉概率 80%
MUTATION_RATE = 0.01  # 变异概率 1%
MAX_GENERATION = 50  # 最大迭代次数 50 次


def create_population():
    # 随机创建 POP_SIZE 个个体,每个个体由 GENES 位二进制组成
    return [[random.randint(0, 1) for _ in range(GENES)] for _ in range(POP_SIZE)]


def decode(individual: list):
    # 将个体的染色体解码映射为 -10~10
    binary_str = ''.join(map(str, individual))
    decimal = int(binary_str, 2)
    return -10 + decimal * 20 / (2 ** GENES - 1)


def fitness(x: int):
    # 计算适应度
    return 1 / (x ** 2 + 1)  # 加多一个1可以避免除数为 0


def selection(pop: list, fitnesses: list):
    # 选择操作
    total_fit = sum(fitnesses)
    probs = [f / total_fit for f in fitnesses]  # 每个个体被选中的概率，其中所有元素加起来等于1
    return random.choices(pop, weights=probs, k=POP_SIZE)  # 从pop中通过weights加权抽取k个元素作为新父母


def crossover(parent1, parent2):
    # 交叉操作
    if random.random() < CROSS_RATE:  # random.random()返回的是[0.0,1.0)之间的浮点数
        point = random.randint(1, GENES - 1)  # 随机选择一个交叉点
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]  # 每个父母的染色体分成两半，然后分别交叉另一半
    else:
        return parent1[:], parent2[:]  # 不交叉就直接复制原样


def mutate(individual):
    # 变异操作
    return [bit if random.random() > MUTATION_RATE else 1 - bit for bit in individual]


def main():
    population = create_population()  # 初始化种群--[[1,1,0,1,0,0,0,1,...],[...],...]
    for generation in range(MAX_GENERATION):  # 遍历每一代--generation=1,2,...
        x_vals = [decode(ind) for ind in population]  # 解码映射到-10~10--[-9.993, 3.141,...]
        fits = [fitness(x) for x in x_vals]  # 计算适应度，越大越越好--[0.999,2.718,...]

        # 找出当前种群中最好的个体
        best_idx = fits.index(max(fits))
        print(f"Gen {generation}: Best x = {x_vals[best_idx]:.4f},f(x) = {1 / fits[best_idx] - 1:.4f}")

        # 选择下一代的“父母”
        selected = selection(population, fits)  # --[[1,1,0,0,0,1,...],[...],...]

        # 生成新一代种群
        new_population = []
        for i in range(0, POP_SIZE, 2):  # 每次配对两个父母
            p1, p2 = selected[i], selected[i + 1]  # p1 = [1,0,0,0,...],p2 = [1,1,0,1,...]
            c1, c2 = crossover(p1, p2)  # 交叉生成两个孩子
            new_population.extend([mutate(c1), mutate(c2)])

        population = new_population


if __name__ == "__main__":
    main()
