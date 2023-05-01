import random

class Plane:
    planelist = []

    def __init__(self, name, id, speed=800, armour=1000, maxweight=50000, fuel=1000):
        self.name = name
        self.id = id
        self.speed = speed
        self.armour = armour
        self.maxweight = maxweight
        self.fuel = fuel
        Plane.planelist.append(self)


class CargoPlane(Plane):
    def __init__(self, name, id, speed=800, armour=1000, maxweight=50000, range=1000, volume=1000, cargo=[]):
        super().__init__(name, id, speed, armour, maxweight, range)
        self.volume = volume
        self.cargo = cargo


class FuelTanker(Plane):
    def __init__(self, name, id, speed=800, armour=1000, maxweight=50000, range=1000, cargofuel=10000):
        super().__init__(name, id, speed, armour, maxweight, range)
        self.cargofuel = cargofuel
    
    def add_fuel(self, plane_obj, fuel):
        plane_obj.fuel += fuel


class Fighter(Plane):
    def __init__(self, name, id, speed=800, armour=1000, slots=6, gundmg=50, weapons=[]) -> None:
        if len(weapons) > slots:
            raise ValueError("Number of weapons cannot be more than the number of slots.")
                                    
        super().__init__(name, id, speed, armour)
        self.slots = slots
        self.gundmg = gundmg
        self.weapons = weapons
    
    def appdmg(self, target, damage):
        target.armour -= damage