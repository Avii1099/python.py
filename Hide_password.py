import getpass

user = getpass.getuser()
while True:
    pwd = getpass.getpass("User Name : %s" % user)

    if pwd == 'abcd':
        print("Welcome!!!")
        break
    else:
        print("The password you entered is incorrect.")


