# -*- coding: UTF-8 -*- 
from sys import argv
script,filename=argv

print "准备擦除 %r." % filename
print "不需要擦除,请按CTRL-C (^C)。"
print "需要擦除,请按回车键。"

raw_input("?")

print "打开文件...."
target=open(filename,'w')

print "擦除文件...."
target.truncate()

print "现在请输入三行文字："

line1=raw_input("第一行:")
line2=raw_input("第二行:")
line3=raw_input("第三行:")

print "正在保存文件...."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "文件已关闭"
target.close()



