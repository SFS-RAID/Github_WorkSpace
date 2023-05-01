from gamecode import plane_cls as pln

myplane = pln.Fighter("Su30", 1, armour=2000, gundmg=200)
enemy = pln.Fighter("F18", 2, armour=1800, gundmg=400)

print(f"enemy's health is {enemy.armour}")
cmd= input("Input: ")
if cmd == "attack":
    myplane.appdmg(enemy, myplane.gundmg)
    print(f"enemy's health is {enemy.armour}")