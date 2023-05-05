import time
time.sleep(3)
error = ""

val = {"0" : 0,
       "1" : 1,
       "2" : 2,
       "3" : 3,
       "4" : 4,
       "5" : 5,
       "6" : 6,
       "7" : 7,
       "8" : 8,
       "9" : 9,
       "A" : 10,
       "B" : 11,
       "C" : 12,
       "D" : 13,
       "E" : 14,
       "F" : 15}

def rgb(first, second, third):
    global error
    validvalues = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                   "A", "B", "C", "D", "E", "F"]
    #error handling
    for value in [first, second, third]:
        if value[0] not in validvalues or value[1] not in validvalues:
            error = "Invalid Characters, only 0-9 and A-F are accepted"
            raise Exception

    red = val[first[0]] * 16 + val[first[1]]
    green = val[second[0]] * 16 + val[second[1]]
    blue = val[third[0]] * 16 + val[third[1]]
    return [red, green, blue]
            

print("\nHex to RGB converter\n")

while input != "quit":
    try:
        code = input("Enter a Hex code:")
        code = code.upper()
        if code == "quit" or code == "exit" or code == "q":
            print("Successfully exited program")
            break
        elif len(code) != 6:
            error = "Length of code must be 6!"
            raise Exception
        else:
            #0-2 is first 2, ex - 1,2 in 123456
            firstpart = code[0:2]
            #2-4 is 3rd and 4th
            secondpart = code[2:4]
            thirdpart = code[4:6]
            values = rgb(firstpart, secondpart, thirdpart)
            print(f"R: {values[0]}, G: {values[1]},B: {values[2]}\n")
    except:
        print(f"\n{UserWarning}: {error}\n\n")
