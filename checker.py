def register():
    username = input("Please input a username:  ")
    password = input("Please input a password:  ")
    file = open("passwords.txt", "a")  # You dan change the filename to your desired filename
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    if login():
        print("Welcome {}".format(username))
    else:
        print("Invalid login...")


def login():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    for line in open("passwords.txt", "r").readlines():  # You dan change the filename to your desired filename
        login_info = line.split()
        if username == login_info[0] and password == login_info[1]:
            print("You are now logged in...")
            return True
        else:
            continue
    print("Invalid login...")
    answer = input("Would you like to register? y/n:  ".lower())
    if answer == 'y'.lower():
        register()
    else:
        return False


if 'passwords.txt' == 0:  # You dan change the filename to your desired filename
    register()

login()
