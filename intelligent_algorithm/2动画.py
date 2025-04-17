import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# -------------------- 参数设置 --------------------
LOWER_BOUND = -500
UPPER_BOUND = 500
DIM = 2
POP_SIZE = 50
MAX_GEN = 50
CROSS_RATE = 0.8
MUTATION_RATE = 0.05
INTERVAL = 100  # 每帧间隔 ms


# -------------------- Schwefel函数 --------------------
def schwefel(X):
    return 418.9829 * DIM - np.sum(X * np.sin(np.sqrt(np.abs(X))), axis=1)


# -------------------- 初始化种群 + OBL --------------------
def init_population_obl(pop_size):
    pop = np.random.uniform(LOWER_BOUND, UPPER_BOUND, (pop_size, DIM))
    opp_pop = LOWER_BOUND + UPPER_BOUND - pop
    combined = np.vstack((pop, opp_pop))
    fitness = schwefel(combined)
    best_indices = np.argsort(fitness)[:pop_size]
    return combined[best_indices]


# -------------------- GA操作 --------------------
def select(pop):
    fitness = schwefel(pop)
    probs = 1 / (fitness + 1e-6)
    probs /= np.sum(probs)
    indices = np.random.choice(np.arange(len(pop)), size=len(pop), p=probs)
    return pop[indices]


def crossover(parent1, parent2):
    if np.random.rand() < CROSS_RATE:
        mask = np.random.rand(DIM) < 0.5
        child = np.where(mask, parent1, parent2)
        return child
    return parent1.copy()


def mutate(child, use_obl=True):
    for i in range(DIM):
        if np.random.rand() < MUTATION_RATE:
            if use_obl and np.random.rand() < 0.5:
                child[i] = LOWER_BOUND + UPPER_BOUND - child[i]
            else:
                child[i] = np.random.uniform(LOWER_BOUND, UPPER_BOUND)
            child[i] = np.clip(child[i], LOWER_BOUND, UPPER_BOUND)
    return child


# -------------------- GA主循环 + 历史记录 --------------------
def run_ga_obl_schwefel():
    history = []
    pop = init_population_obl(POP_SIZE)
    history.append(pop.copy())
    for gen in range(MAX_GEN):
        pop = select(pop)
        new_pop = []
        for i in range(0, POP_SIZE, 2):
            p1 = pop[i]
            p2 = pop[(i + 1) % POP_SIZE]
            c1 = mutate(crossover(p1, p2), use_obl=True)
            c2 = mutate(crossover(p2, p1), use_obl=True)
            new_pop.extend([c1, c2])
        pop = np.array(new_pop)[:POP_SIZE]
        history.append(pop.copy())
    return history


# -------------------- 自定义慢放帧序列 --------------------
def generate_slow_frames(total_gens, slow_gens=10, slow_factor=3):
    frames = []
    for i in range(total_gens):
        if i < slow_gens:
            frames.extend([i] * slow_factor)
        else:
            frames.append(i)
    return frames


# -------------------- 动画绘图设置 --------------------
history = run_ga_obl_schwefel()
frames = generate_slow_frames(len(history), slow_gens=10, slow_factor=3)

fig, ax = plt.subplots(figsize=(6, 6))
x = np.linspace(LOWER_BOUND, UPPER_BOUND, 300)
y = np.linspace(LOWER_BOUND, UPPER_BOUND, 300)
X, Y = np.meshgrid(x, y)
Z = schwefel(np.c_[X.ravel(), Y.ravel()]).reshape(X.shape)
ax.contourf(X, Y, Z, levels=100, cmap='plasma')
ax.set_xlim(LOWER_BOUND, UPPER_BOUND)
ax.set_ylim(LOWER_BOUND, UPPER_BOUND)
ax.set_xlabel("x")
ax.set_ylabel("y")
scatter = ax.scatter([], [], c='red', s=50, edgecolors='black')


# -------------------- 更新函数 --------------------
def update(frame_idx):
    current_pop = history[frame_idx]
    scatter.set_offsets(current_pop)
    best_fitness = schwefel(current_pop).min()
    ax.set_title(f"第 {frame_idx} 代 / 共 {MAX_GEN} 代    最优适应度: {best_fitness:.2f}", fontsize=14)
    return scatter,


# -------------------- 创建动画 --------------------
ani = animation.FuncAnimation(
    fig, update, frames=frames, interval=INTERVAL, blit=True, repeat_delay=1000
)

# 保存动画为GIF（推荐）
ani.save("schwefel_obl_ga.gif", writer="pillow", fps=10)

plt.show()
