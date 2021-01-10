import os

if os.path.exists('maspass.txt'):
    pass
else:
    f = open("maspass.txt", "w+")

def maspass():
    file_path = 'maspass.txt'
    with open('maspass.txt', "r+") as f:
        first_line = f.readline()
        if os.stat(file_path).st_size == 0:
            masterpass = input("Create a master password:")
            f.write(masterpass)
        else:
            print("Enter your password")
            if input() == first_line:
                print("Welcome")
                neworget()
            else:
                print("Wrong password")
                maspass()

def neworget():
    p = open("passwords.txt", "a+")
    print("Would you like to enter a new password, or retrieve one?")
    print("new/get/exit")
    ask = input()
    if ask == "new":
        print("Please enter the source, with a space, followed by the password")
        newpassword = input()
        for i in range(1):
            p.write("\n" + newpassword)
        neworget()
    elif ask == "get":
        print("Which password would you like to retrieve?")
        password = input() + " "
        searchfile = open("passwords.txt", "r")
        no_password = True

        for line in searchfile:
            if password in line:
                no_password = False
                print(line)
                neworget()

        if no_password:
            print("No password found")
    elif ask == "exit":
        print("Thank you")
        exit()
    else:
        print("Wrong input")
        neworget()





maspass()
