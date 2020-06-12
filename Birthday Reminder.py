dict = {}
while True:
    print("_____BIRTHDAY APP_____")
    print("Choice any option:")
    print("1. Show Birthday")
    print('2. Add to Birthday list')
    print("3. Exit")

    choice = int(input(" Enter : "))

    if choice == 1:
        if len(dict.keys())==0:
            print("Nothing to Show ")
        else:
            name = input("Enter name to look for birthday: ")
            birthday = dict.get(name, "No data Found \n "
                                     "please add Birthday list")
            print(birthday)

    elif choice == 2:
        name = input("Enter Friend's name= ")
        date = input("Enter Birth date = ")
        dict[name]=date
        print("Birthday Added")
    elif choice == 3:
        break
    else:
        print("Enter Correct Choice")

print(dict)





