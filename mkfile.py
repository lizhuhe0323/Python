import os

def get_fname():
    while True:
        fname = input("Please input filename:")
        if not os.path.exists(fname):
            break
        print ("%s already exists.Tay again." % fname)
    return fname

def get_contents():
    contents = []
    while True:
        data = input("(Enter to quit)>")
        if not data:
            break
        contents.append(data + '\n')
    return contents

def wfile(fname,contents):
    fobj = open(fname,'w')
    fobj.writelines(contents)
    fobj.close()

if __name__ == '__main__':
    filename = get_fname()
    lines = get_contents()
    wfile(filename,lines)

