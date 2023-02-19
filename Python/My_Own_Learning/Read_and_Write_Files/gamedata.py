
name = input("Type your name: ")
uin = input("Type the amount of money you have: ")

with open('mydata.txt', 'w') as file:
  file.writelines(['Money = ' + uin + '\n', 'name = ' + name])
with open('mydata.txt', 'r') as file:
  contents = file.readlines()
  moneyline = contents[0].split(" ")
  money = moneyline[-1]
  nameline = contents[1].split(" ")
  name = nameline[-1]
v = "You have ₹" + money + "😊"
print(f'\nYour name is {name}')
print(v)
