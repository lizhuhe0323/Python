def counter(start_at=0):
    count = [start_at]
    def incr():
        count[0] +=1
        return count[0]
    return incr

if __name__ == '__main__':
    a = counter()
    print (a())
    print (a())
    b = counter(10)
    print (b())