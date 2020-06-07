def user_register():
    user_name = input("Please input a username:  ")
    password = input("Please input a password:  ")
    file = open("passwords.txt", "a")  # You dan change the filename to your desired filename
    file.write(user_name)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    if user_login():
        print("Welcome {}".format(user_name))
    else:
        print("Invalid login...")


def user_login():
    user_name = input("Please enter your username: ")
    password = input("Please enter your password: ")
    for line in open("passwords.txt", "r").readlines():  # You dan change the filename to your desired filename
        login_info = line.split()
        if user_name == login_info[0] and password == login_info[1]:
            print("You are now logged in...")
            return True
        else:
            continue
    print("Invalid login...")
    answer = input("Would you like to register? y/n:  ".lower())
    if answer == 'y'.lower():
        user_register()
    else:
        return False


user_login()
