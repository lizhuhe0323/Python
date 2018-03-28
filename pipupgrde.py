import pip
from subprocess import call
 
for dist in pip.get_installed_distributions():
    call("pip3 install --upgrade " + dist.project_name +' -i https://pypi.tuna.tsinghua.edu.cn/simple', shell=True)
