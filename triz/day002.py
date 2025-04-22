class TechSystem:
    def __init__(self,strength,weight):
        self.strength = strength
        self.weight = weight

    def improve_strength(self):
        self.strength += 1
        self.weight += 2  # 改进强度的代价是变重

    def status(self):
        return f"Strength:{self.strength},Weight:{self.weight}"

sys = TechSystem(strength=5,weight=3)
print("改进前：",sys.status())
sys.improve_strength()
print("改进后：",sys.status())