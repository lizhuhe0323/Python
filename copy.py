# -*- coding: UTF-8 -*- 
from sys import argv
from os.path import exists
script,from_file,to_file=argv
print "复制 %s 到 %s" % (from_file,to_file)

in_file=open(from_file)
indata=in_file.read()

print "文件大小为 %d bytes" % len(indata)
print "就绪,按回车键继续,按CTRL-C取消。"
raw_input()

out_file=open(to_file,'w')
out_file.write(indata)

print "处理完毕。"

out_file.close()
in_file.close()
