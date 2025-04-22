class System:
    def __init__(self, useful=1, harmful=1, cost=1):
        self.useful = useful
        self.harmful = harmful
        self.cost = cost

    def ideality(self):
        return self.useful / (self.harmful + self.cost)


# 初代系统
v1 = System(useful=1, harmful=2, cost=3)
# 进化后的系统
v2 = System(useful=4, harmful=1, cost=2)

print("初代理想性：",v1.ideality())
print("升级后理想性",v2.ideality())

