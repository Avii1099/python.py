import random
import time

roll_again = 'y'
minimum = 1
maximum = 6
n = int(input("How many player : "))
name = []
for i in range(1, n+1):
    name1 = input("Player Name : ")
    name.append(name1)
while roll_again in ('y', 'Y'):
    print("Rolling the dice........")
    time.sleep(1)
    print("Your value is: ")
    for i in range(0, n):
        result = random.randint(minimum, maximum)
        print("{}  : {}".format(name[i], result))
        input()
        if result == 1:
            print("-----")
            print("'   '")
            print("' 0 '")
            print("'   '")
            print("-----")
        if result == 2:
            print("------")
            print("'    '")
            print("' 00 '")
            print("'    '")
            print("------")
        if result == 3:
            print("-------")
            print("'  0  '")
            print("'  0  '")
            print("'  0  '")
            print("-------")
        if result == 4:
            print("------")
            print("' 00  '")
            print("' 00 '")
            print("------")
        if result == 5:
            print("------")
            print("' 0 0 '")
            print("'  0 '")
            print("' 0 0 '")
            print("------")
        if result==6:
            print("------")
            print("' 0 0 '")
            print("' 0 0 '")
            print("' 0 0 '")
            print("------")
    roll_again = input("Rolling again (y/n): ")
    if roll_again in ('n', 'N'):
        print("Thank You")
        break
    else:
        roll_again = 'y'












