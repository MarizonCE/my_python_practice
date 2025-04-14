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


def fitness(x):
    return 1 / (x ** 2 + 1)  # 加多一个1可以避免除数为 0


def selection(pop,fitnesses):
    total_fit = sum(fitnesses)
    probs = [f / total_fit for f in fitnesses]
    


def main():
    population = create_population()  # 初始化种群
    print(population)
    for generation in range(MAX_GENERATION):  # 遍历每一代
        # 解码并计算适应度
        x_vals = [decode(ind) for ind in population]
        fits = [fitness(x) for x in x_vals]

        # 输出当前最好个体
        best_idx = fits.index(max(fits))
        print(f"Gen {generation}: Best x = {x_vals[best_idx]:.4f},f(x) = {1 / fits[best_idx] - 1:.4f}")

        # 选择
        selected = selection(population, fits)


if __name__ == "__main__":
    main()
