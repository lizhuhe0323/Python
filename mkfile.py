import os

contents = []

while True:
    fname = input("Please input filename:")
    if not os.path.exists(fname):
        break
    print ("%s already exists.Tay again." % fname)

while True:
    data = input("(Enter to quit)>")
    if not data:
        break
    contents.append(data + '\n')

fobj = open(fname,'w')
fobj.writelines(contents)
fobj.close()


