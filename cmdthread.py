import sys
import paramiko
import threading

def remote_comm(host,username,pwd,comm):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,username=username,password=pwd)
    stdin,stdout,stderr = ssh.exec_command(comm)
    print (stdout.read()),
    print (stderr.read()),

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print ("Usage: %s ipfile password command" % sys.argv[0])
    else:
        ipfile = sys.argv[1]
        user = sys.argv[2]
        password = sys.argv[3]
        #newpass = sys.argv[3]
        command = sys.argv[4]
        #ch_pwd = "echo %s | passwd --stdin root" % newpass
        fobj = open(ipfile)
        for line in fobj:
            ip = line.strip()
            t = threading.Thread(target=remote_comm,args=(ip,user,password,command))
            t.start()


