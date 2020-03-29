import random
import os.path
import os
import subprocess
import fileinput

# delete last chart from the output of pwd command and store in folder var
folder = subprocess.check_output('pwd')[:-1]        

# locate bashrc/bash_profile 
bash_locator = subprocess.getoutput('echo ' + '~')


bashrc = bash_locator+"/.bashrc"
bash_profile = bash_locator+"/.bash_profile"

# convert bytes to string with decode
# expanduser func to locate the relative files
# below will right file named banners_path to retrieve downloaded project path
place = 'python3 ' + folder.decode('utf-8') + '/ascii.py'
repath = "~/.banners_path"
fpath = os.path.expanduser(repath)
with open(fpath, "w") as mypath:
    mypath.write(folder.decode('utf-8'))
    mypath.close()

ss = 'ASCII-Art-Splash-Screen'


c = 0
# check which file exists bashrc or bash_profile
try:
    f = open(bashrc)
    c = 1
except IOError:
    cc = 3
try:
    f = open(bash_profile)
    c = 4
except IOError:
    cc = 8
finally:
    f.close()

def does_it_exists_in_bashrc(c):
    if c == 1:
        file_bashrc = open(bashrc).read()
        if ss in file_bashrc:
            c = 20
        return c 


def does_it_exists_in_bash_profile(c):
    if c == 4:
        file_bash_profile = open(bash_profile).read()
        if ss in file_bash_profile:
            c += 20
        return c 


# if no, then processed 
if does_it_exists_in_bashrc(c) == 1:
    b = open(bashrc, "a+")
    b.write(place)
    b.close()
if does_it_exists_in_bash_profile(c) == 4:
    b = open(bash_profile, "a+")
    b.write(place)
    b.close()
print('open a new terminl to witness banners')