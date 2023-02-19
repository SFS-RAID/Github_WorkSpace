def findmax(list):
    maxnum = 0
    for number in list:
        if number > maxnum:
            maxnum = number
    return maxnum