import getpass
import mysql
import os
from formattxt import format

def new_user():
    while True:
        user = input("\033[1;37m%s\033[0m" % "username:")
        if not user:
            print ("\033[0;31m%s\033[0m" % "\nUsername can't be empty!\n")
        else:
            results = mysql.select(user)
            if results:
                print ("\033[0;31m%s\033[0m" % "\n%s already exists,please select an other.\n" % user)
            else:
                while True:
                    pwd = input("\033[1;37m%s\033[0m" % "password:")
                    pwd_again = input("\033[1;37m%s\033[0m" % "password again:")
                    if pwd and pwd == pwd_again:
                        if len(pwd) >= 8:
                            mysql.insert(user,pwd)
                            print ("\033[0;31m%s\033[0m" % "\n%s Register successful!\n" % user)
                            break
                        else:
                            print ("\033[0;31m%s\033[0m" % "\nPassword must not be less than 8!")
                    else:
                        if pwd == pwd_again:
                            print ("\033[0;31m%s\033[0m" % "\nPassword can't be empty!\n")
                        else:
                            print ("\033[0;31m%s\033[0m" % "\nPassword mismatch!\n")
                break

def old_user():
    countnum = 0
    while countnum <= 2:
        user = input("\033[1;37m%s\033[0m" % "username:")
        pwd = getpass.getpass("\033[1;37m%s\033[0m" % "password:")
        results = mysql.select(user)
        if pwd != results:
            countnum += 1
            print ("\033[0;31m%s\033[0m" % "\nLogin incorrent,there are %s/3 chances left.\n" % (3-countnum))
        else:
            print ("\033[0;31m%s\033[0m" % "\n%s Login successful!\n" %user)
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
        try:
            choice = input(prompt).strip()[0]
            if choice not in '012':
                print ("\033[0;31m%s\033[0m" % "\nInvalid choice,try again.\n")
                continue
            if choice == '2':
                break
            CMDs[choice]()
        except (ValueError, IndexError):
            print("\033[0;31m%s\033[0m" % "\nInvalid choice,try again.\n")





