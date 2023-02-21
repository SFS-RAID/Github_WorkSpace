class Cat():
    def __init__(self, name, age=0, cuteness=50):
        self.name = name
        self.age = age
        self.cuteness = cuteness

My_Cat = Cat('Farhan\'s_Cat', 4, 100)

def Find_Cuteness(The_Cat):
    if The_Cat.cuteness >= 75:
        return f'{The_Cat.name} is very cute'
    elif The_Cat.cuteness >= 50 and The_Cat.cuteness < 70:
        return f'{The_Cat.name} is pretty'
    elif The_Cat.cuteness < 50 and The_Cat.cuteness > 25:
        return f'{The_Cat.name} is average'
    else:
        return f'{The_Cat.name} is ugly'

Fariha_Cat = Cat('Fariha\'s_Cat', 1, 14)

print(Find_Cuteness(My_Cat))
print(Find_Cuteness(Fariha_Cat))