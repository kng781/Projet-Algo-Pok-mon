class Pokemon:

    name = ""
    hp = 0
    max_hp = 100
    attack_power = 0

    def __init__(self, name, max_hp, attack_power):
        self.name = name
        self.hp = max_hp
        self.max_hp = max_hp
        self.attack_power = attack_power

    def se_presenter(self):
        print("I am", self.name) 

    def set_target(self, target: "Pokemon"):
        self.target = target

    def take_damage(self, damage):
        self.hp -= damage
        
    def attack_target(self, target):
        target.take_damage(40)  

    def heal(self):
        amount = 40
        self.hp = min(self.hp + amount, self.max_hp)

    def is_defeated(self):
          return self.hp <= 0

    def get_attack(self):
        return self.attack_power
    




        
                      
    


        