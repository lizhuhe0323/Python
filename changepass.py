import sys
import paramiko

def remote_comm(host,pwd,comm):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,username='lizhuhe',password=pwd)
    stdin,stdout,stderr = ssh.exec_command(comm)
    print (stdout.read()),
    print (stderr.read()),

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print ("Usage: %s ipfile oldpass newpass" % sys.argv[0])
    else:
        ipfile = sys.argv[1]
        oldpass = sys.argv[2]
        newpass = sys.argv[3]
        ch_pwd = "echo %s | passwd --stdin root" % newpass
        fobj = open(ipfile)
        for line in fobj:
            ip = line.strip()
            remote_comm(ip,oldpass,ch_pwd)

