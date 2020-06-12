import random
import getpass
print("___Guessing The Number_____")
name = input("What's Your Name :")
restart = 'y'
while restart in ('y', 'Y'):
      guess1 = int(getpass.getpass(prompt="Guess any number(HIDE) : "))
      guess2 = int(getpass.getpass(prompt="Guess same number for friend(HIDE) : "))
      print("Total is : ", guess1 + guess2)
      print("_____________   Now Game is Start   _______________")
      print("I add any random number between 1 to 20 :")
      guess3 = random.randint(1, 20)
      print("I add number is :", guess3)
      guess4 = guess1+guess2+guess3
      print("Now Total is: ", guess4)
      guess5 = guess4/2
      print(" After Divide By 2: ", guess5)
      guess6 = guess3 / 2
      guess7 = guess5 - guess6
      print("After that i subtract the random number divide by 2")
      print("Your Guess Number is : ", guess7)
      restart = input("play again(y/n): ")
      if restart in ('n', 'N'):
           print("Thank you")
           break
      else:
          restart = 'y'







