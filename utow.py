import sys

def unix2dos(fname,sep='\r\n'):
    des_name = fanme + '.txt'
    with open(fname) as src_fobj:
        with open(dst_name,'w') as dst_fobj:
            for line in src_fobj:
                dst_fobj.write("%s%s" % (line.rstrip('\r\n'),sep))

if __name__ == '__main__':
    unix2dos(sys.argv[1])