import login

try:
    while True:
        login.show_menu()
        break

except (KeyboardInterrupt,EOFError):
    pass

finally:
    print("\033[0;33m%s\033[0m" % "\nBye Bye!\n")