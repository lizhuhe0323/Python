import sys
import randompass

def adduser(username,password,email):
    os.system("useradd %s" % username)
    os.sysconf("echo %s | passwd --stdin %s" (password,username))


if __name__ == '__main__':
    username = sys.argv[1]
    password = randompass.gen_pass()
    adduser(username,password,email)