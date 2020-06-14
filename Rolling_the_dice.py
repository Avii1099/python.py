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
    time.sleep(2)
    print("Your value is: ")
    for i in range(0, n):
        result = random.randint(minimum, maximum)
        print("{}  : {}".format(name[i], result))
    roll_again = input("Rolling again (y/n): ")
    if roll_again in ('n', 'N'):
        print("Thank You")
        break
    else:
        roll_again = 'y'












