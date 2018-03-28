input = int(input('input munber:'))
for i in range(input):
    for j in range(i):
        print (' '*(j-1)+'*'*j)
    print ('\n')
