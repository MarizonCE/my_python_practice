import random
from typing import List


def fitness(x: float) -> float:
    """
    适应度函数，目标是最小化 x^2。
    """
    return x ** 2


def initialize_population(size: int, lower_bound: float, upper_bound: float) -> List[float]:
    """
    初始化种群，生成给定范围内的随机个体。
    """
    return [random.uniform(lower_bound, upper_bound) for _ in range(size)]


def select(population: List[float], num_selected: int) -> List[float]:
    """
    选择适应度最小的个体。
    """
    return sorted(population, key=fitness, reverse=False)[:num_selected]


def crossover(parents: List[float], num_children: int) -> List[float]:
    """
    交叉操作，随机从父代中配对生成子代。
    """
    children = []
    while len(children) < num_children:
        p1, p2 = random.sample(parents, 2)
        child = (p1 + p2) / 2
        children.append(child)
    return children


def mutate(individuals: List[float], mutation_rate: float, mutation_strength: float,
           lower_bound: float, upper_bound: float) -> List[float]:
    """
    变异操作，以一定概率对个体加上随机扰动。
    """
    for i in range(len(individuals)):
        if random.random() < mutation_rate:
            individuals[i] += random.uniform(-mutation_strength, mutation_strength)
            individuals[i] = min(max(individuals[i], lower_bound), upper_bound)
    return individuals


def genetic_algorithm(
        population_size: int = 10,
        num_generations: int = 10,
        selection_ratio: float = 0.5,
        mutation_rate: float = 0.2,
        mutation_strength: float = 1.0,
        lower_bound: float = -10.0,
        upper_bound: float = 10.0
) -> None:
    """
    简单遗传算法主函数。
    """
    population = initialize_population(population_size, lower_bound, upper_bound)
    num_selected = int(population_size * selection_ratio)

    for _ in range(num_generations):
        # 评估适应度并选择
        selected = select(population, num_selected)

        # 交叉和变异
        children = crossover(selected, population_size - num_selected)
        children = mutate(children, mutation_rate, mutation_strength, lower_bound, upper_bound)

        # 更新种群
        population = selected + children

    # 输出最优个体
    best = min(population, key=fitness)  # fitness的之前定义的函数，也可以这样使用
    print(f"最优解：{best:.4f}, 适应度：{fitness(best):.4f}")


if __name__ == "__main__":
    genetic_algorithm()
