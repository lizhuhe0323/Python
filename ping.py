import os

for i in range(1,255):
    ip = "192.168.1.%s" % i
    result = os.system("ping -c2 %s &> /dev/null" % ip)
    if result:
        print ("%s:down" % ip)
    else:
        print ("%s up" % ip)