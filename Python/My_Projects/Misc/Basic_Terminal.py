print("Hello User!")
running = True
prompt = ">"
output = ""
comlist = "Echo - outputs whatever you type\nexit - Exits the App"

while running == True:
  ui = input(prompt)
  #ui = ui.lower()
  cmds = ui.split(" ")
  cmds[0] = cmds[0].lower()
  if cmds[0] == "echo":
    cmds.pop(0)
    for i in cmds:
      output += (i + " ")
    print(output)
    output = ""
  elif cmds[0] == "help":
    print(comlist)
  elif cmds[0] == "exit":
    print("Program Exited!")
    running = False
  else:
    print("Invalid Input")
