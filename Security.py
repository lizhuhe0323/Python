import login

try:
    while True:
        login.show_menu()
        break

except KeyboardInterrupt:
    print ("\n\nBye Bye!\n")