import os
import time
import tarfile
import pickle as p
import hashlib

def check_md5(fname):
    m = hashlib.md5()
    with open(fname) as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

def full_backup(src_dir,dst_dir,md5file):
    md5file = {}
    base_dir,back_dir = os.path.split(src_dir.rstrip('/'))
    back_name = "%s_full_%s.tar.gz" % (back_dir,time.strftime('%Y%m%d'))
    full_path = os.path.join(dst_dir,back_name)

    os.chdir(base_dir)
    tar = tarfile.open(full_path,'w:gz')
    tar.add(back_dir)
    tar.close()

    for path,dirs,files in os.walk(src_dir):
        for each_file in files:
            full_name = os.path.join(path,each_file)
            md5dict[full_name] = check_md5(each_file)

    with open(md5file,'w') as fobj:
        p.dump(md5dict,fobj)

def incr_backup(src_dir,dst_dir,md5file):
    pass

if __name__ == '__main__':
    src_dir = '/home/demo'
    dst_dir = '/home/dst'
    md5file = '/home/dst/md5.data'
    if time.strftime('%a') == "Mon":
        full_backup(src_dir,dst_dir,md5file)
    else:
        incr_backup(src_dir,dst_dir,md5file)

