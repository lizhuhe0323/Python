from sys import argv
from os.path import exists
script,sfname,dfname=argv

def cp(sfname,dfname):
    src_fobj = open(sfname)
    dst_fobj = open(dfname,'w')

    while True:
        data = src_fobj.read(4096)
        if not data:
            break
        dst_fobj.write(data)

    src_fobj.close()
    dst_fobj.close()

cp(sfname,dfname)