

class player:
    playerlist = []

    def __init__(self, name, country=None, money=0, aircraftinv=[], wpninv=[]) -> None:
        self.name = name
        self.country = country
        self._money = money
        self.airinv = aircraftinv
        self.weaponinv = wpninv
        player.playerlist.append(self)
    
    
    def setmoney(self, value):
        self._money = value
    
    def addmoney(self, value):
        self._money += value
    
    def money(self):
        return self._money