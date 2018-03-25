from ssh import ssh_cmd

def h(n):
    print('test!')
    return(n)

def p(t):
    a = input('a=')
    b = input('b=')
    print ('!!!!')
    return(t)

@ssh_cmd('192.168.1.12', 'Ab@12345','uname -a')
@h
@p
def c():
    a = 1 
    b = 2
    print('a+b')

def d(i):
    print('4')

def e():
    print('5')

c()

d(e())
