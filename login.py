import getpass
import mysql
import os
from formattxt import format

def new_user():
    while True:
        user = input("username:")
        if not user:
            print ("\nUsername can't be empty!\n")
        else:
            results = mysql.select(user)
            if results:
                print ("\n%s already exists,please select an other.\n" % user)
            else:
                while True:
                    pwd = input("password:")
                    if pwd:
                        if len(pwd) >= 8:
                            mysql.insert(user,pwd)
                            print ("\n%s Register successful\n" % user)
                            break
                        else:
                            print ("\nPassword can't lease than 8!")
                    else:
                        print ("\nPassword can't be empty!0\n")
                break

def old_user():
    countnum = 0
    while countnum <= 2:
        user = input("username:")
        pwd = getpass.getpass("password:")
        results = mysql.select(user)
        if pwd != results:
            countnum += 1
            print ("\nLogin incorrent.Try again,there are %s chances left.\n" % (3-countnum))
        else:
            print ("\n%s Login successful!\n" %user)
            os.system("say 'welcome to login,%s'" %user)
            break

def show_menu():
    CMDs = {'0':new_user,"1":old_user}
    lines = ["WELCOME TO MY PYCHARM LAB","WARINING!!!","Unauthorized access is Forbidden."]
    prompt = """(0) NEW USER REGISTER
(1) OLD USER LOGIN IN
(2) QUIT
Please input your choice(0/1/2): """
    while True:
        format(lines)
        choice = input(prompt).strip()[0]
        if choice not in '012':
            print ("\nInvalid choice,Try again.\n")
            continue
        if choice == '2':
            print("\nBye Bye!\n")
            break
        CMDs[choice]()





