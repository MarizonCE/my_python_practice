import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# --------------------- 参数设置 ---------------------
LOWER_BOUND = -500
UPPER_BOUND = 500
DIM = 2
POP_SIZE = 50
MAX_GEN = 50
CROSS_RATE = 0.6
MUTATION_RATE = 0.25
INTERVAL = 100


# --------------------- Schwefel函数定义 ---------------------
def schwefel(X):
    return 418.9829 * DIM - np.sum(X * np.sin(np.sqrt(np.abs(X))), axis=1)


# --------------------- 初始化种群（避开最优区域） ---------------------
def init_population(pop_size):
    pop = np.random.uniform(LOWER_BOUND, UPPER_BOUND, (pop_size, DIM))
    mask = np.linalg.norm(pop - 420.9687, axis=1) < 50
    while np.any(mask):
        pop[mask] = np.random.uniform(LOWER_BOUND, UPPER_BOUND, (np.sum(mask), DIM))
        mask = np.linalg.norm(pop - 420.9687, axis=1) < 50
    return pop


# --------------------- GA 算子 ---------------------
def select(pop):
    fitness = schwefel(pop)
    probs = np.exp(-fitness / 1000)
    probs /= np.sum(probs)
    indices = np.random.choice(np.arange(len(pop)), size=len(pop), p=probs)
    return pop[indices]


def crossover(parent1, parent2):
    if np.random.rand() < CROSS_RATE:
        point = np.random.randint(1, DIM)
        child = np.concatenate((parent1[:point], parent2[point:]))
        return child
    return parent1.copy()


def mutate(child):
    for i in range(DIM):
        if np.random.rand() < MUTATION_RATE:
            child[i] += np.random.uniform(-50, 50)
            child[i] = np.clip(child[i], LOWER_BOUND, UPPER_BOUND)
    return child


# --------------------- GA 主循环 ---------------------
def run_ga():
    history = []
    best_history = []
    pop = init_population(POP_SIZE)
    for gen in range(MAX_GEN):
        history.append(pop.copy())
        fitness = schwefel(pop)
        best = pop[np.argmin(fitness)]
        best_history.append(best)
        pop = select(pop)
        new_pop = []
        for i in range(0, POP_SIZE, 2):
            parent1 = pop[i]
            parent2 = pop[(i + 1) % POP_SIZE]
            child1 = mutate(crossover(parent1, parent2))
            child2 = mutate(crossover(parent2, parent1))
            new_pop.extend([child1, child2])
        pop = np.array(new_pop)[:POP_SIZE]
    return history, best_history


# --------------------- 生成动画帧索引（例如 [0,0,0,1,1,1,...]） ---------------------
def generate_frame_indices(total_gens, slow_gens=10, slow_factor=3):
    indices = []
    for i in range(total_gens):
        repeat = slow_factor if i < slow_gens else 1
        indices.extend([i] * repeat)
    return indices


# --------------------- 绘图准备 ---------------------
history, best_history = run_ga()
frame_indices = generate_frame_indices(len(history), slow_gens=10, slow_factor=3)

fig, ax = plt.subplots(figsize=(6, 6))
x = np.linspace(LOWER_BOUND, UPPER_BOUND, 200)
y = np.linspace(LOWER_BOUND, UPPER_BOUND, 200)
X, Y = np.meshgrid(x, y)
Z = schwefel(np.c_[X.ravel(), Y.ravel()]).reshape(X.shape)
ax.contourf(X, Y, Z, levels=50, cmap='viridis')
ax.set_xlim(LOWER_BOUND, UPPER_BOUND)
ax.set_ylim(LOWER_BOUND, UPPER_BOUND)
ax.set_xlabel("x")
ax.set_ylabel("y")

scatter = ax.scatter([], [], c='blue', s=50, edgecolors='black')
best_dot, = ax.plot([], [], 'ro', markersize=8)
trajectory_line, = ax.plot([], [], 'r--', linewidth=1)

# 记录轨迹
trajectory_x = []
trajectory_y = []


# --------------------- 更新动画帧 ---------------------
def update(frame_idx):
    gen_idx = frame_indices[frame_idx]
    current_pop = history[gen_idx]
    current_best = best_history[gen_idx]
    scatter.set_offsets(current_pop)
    best_dot.set_data([current_best[0]], [current_best[1]])

    # 更新轨迹
    trajectory_x.append(current_best[0])
    trajectory_y.append(current_best[1])
    trajectory_line.set_data(trajectory_x, trajectory_y)

    fitness = schwefel(current_pop)
    ax.set_title(f"第 {gen_idx + 1}/{MAX_GEN} 代   最优适应度: {fitness.min():.2f}", fontsize=14)
    return scatter, best_dot, trajectory_line


# --------------------- 创建动画 ---------------------
ani = animation.FuncAnimation(
    fig, update, frames=len(frame_indices), interval=INTERVAL, blit=True, repeat=False
)

# 如需保存为GIF或MP4，取消注释以下代码
ani.save("schwefel_ga_animation.gif", writer="pillow", fps=10)
# ani.save("schwefel_ga_animation.mp4", writer="ffmpeg", fps=10)

plt.show()
