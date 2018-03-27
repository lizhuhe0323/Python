import tabnanny
import sys
while True:
    try:
        n = int(input('Please input number:').strip())
        for i in range(2,n+1):
            for x in range(2,i):
                if i % x ==0:
                    break
                else:
                    print(i)
    except ValueError:
        print('Error! Please input again!')
    except KeyboardInterrupt:
        sys.exit('\n')
