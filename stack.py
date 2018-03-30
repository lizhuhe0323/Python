stack = []

def pushit():
    item = input('item:')
    stack.append(item)
    print (stack)

def popit():
    if stack:
        print ('poped itme:' ,stack.pop())
    else:
        print ("Empty stack.")

def viewit():
    if stack:
        print (stack)
    else:
        print ("Empty stack.")

def show_menu():
    CMDs = {'0':pushit,'1':popit,'2':viewit}
    prompt = """(0) push it
(1) pop it
(2) view it
(3) quit
Please input your choice(0/1/2/3): """

    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0123':
            print ('Invalid input,Try again.')
            continue
        if choice == '3':
            break
        CMDs[choice]()

if __name__ == '__main__':
    show_menu()