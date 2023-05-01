from gamecode import plane_cls, players

plane = plane_cls.CargoPlane("C17", 2)
jet = plane_cls.Fighter("F18", 6)
su = plane_cls.Fighter("Su-57", 4)

player = players.player("Steve", money=500, aircraftinv=[plane, jet, su])
x = ""
for name in player.airinv:
    x += x.join([name.name + ", "])

x = x[0 : -2]
print(x)

print(player.money)