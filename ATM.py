class ATM:
    balance = 1000
    chance = 3
    restart = "y"
    print("Hey, welcome my bank ")
    while chance >= 0:
        print("Enter your pin : ")
        id = input()
        if id == '1234':
            while restart not in ('n', 'N', 'No', 'NO', 'no'):
                print ("Welcome ")
                print("choice any one ")
                print("1. Check account balance \t "
                      "2. Withdraw funds \t"
                      "3. Deposit Money \t "
                      "4. SMS account details \t"
                      "5. exit")
                choice = int(input("choice : "))

                if choice == 1:
                    print("Your account balance is : ", balance)
                    print("Go back (y/n): ")
                    restart = input()
                    if restart == ('n', 'N', 'No', 'NO', 'no'):
                        print("thank you")
                        break

                elif choice == 2:
                    print("Enter withdraw money: ")
                    withdraw = int(input())
                    balance = balance - withdraw
                    print("you withdraw money: ", withdraw)
                    print(" now your balance is : ", balance)
                    print ("Go back (y/n): " )
                    restart = input()
                    if restart in ('n', 'N', 'No', 'NO', 'no'):
                        print("thank you")
                        break

                elif choice == 3:
                    print(" how much deposit money :")
                    deposit = int(input())
                    balance = balance + deposit
                    print("Your balance is : ", balance)
                    print("Go back (y/n): ")
                    restart = input()
                    if restart in ('n', 'N', 'No', 'NO', 'no'):
                        print("thank you")
                        break

                elif choice == 4:
                    print("Enter your valid mobile number ")
                    number = input()
                    if number == "123456789":
                        print("SMS sent, check sms ")
                    else:
                        print("this is not valid number")
                    print("Go back (y/n")
                if restart in ('n', 'N', 'No', 'NO', 'no'):
                    print("Thank You")
                    break


                elif choice == 5:
                    print("thank you for coming, have a nice day")
                    break
                else:
                    print("please, enter a valid choice :")
                    restart = 'y'
        elif id != '1234':
            print("please, enter valid pin: ")
            chance = chance - 1
            if chance == 0:
                print("Sorry, No more tries ")
                break
        elif restart == 'n':
            break


