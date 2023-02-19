import random

class dice():
    def roll(self):
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        return num1, num2
    

dice1 = dice()
print(dice1.roll())