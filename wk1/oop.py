class Ninja:
    def __init__(self, name, hp = 100, strength = 10):
        self.name = name
        self.health = hp
        self.strength = strength

    def check_health(self):
        print(self.name, self.health, self.strength)
        return self
    
    def attack(self, target):
        target.health -= self.strength
        print(f"{self.name} attacks {target.name} and deals {self.strength} damage!")
        print(target.name, "has", target.health, "hp left!")
        return self



Leo = Ninja("Leo", 20)
Raph = Ninja("Raph")

Leo.attack(Raph).check_health()
# Leo.check_health()
# Raph.check_health()

