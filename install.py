import random
import os.path
import os
import subprocess

# get working dir
folder = subprocess.check_output('pwd')[:-1]        

# locate bashrc/bash_profile 
bash_locator = subprocess.getoutput('echo ' + '~')

bashrc = bash_locator+"/.bashrc"
bash_profile = bash_locator+"/.bash_profile"

# convert bytes to string with decode
place = 'python3 ' + folder.decode('utf-8') + '/ascii.py'

repath = "~/.banners_path"

fpath = os.path.expanduser(repath)

#subprocess.check_output('touch '+ fpath)
with open(fpath, "w") as mypath:
    mypath.write(folder.decode('utf-8'))
    mypath.close()
try:
    with open(bashrc, "a+") as myfile:
    # Do something with the file
        myfile.write('\n')
        myfile.write(str(place) + '\n')
        myfile.close()
except:
    try:
        with open(bash_profile, "a+") as myfile:
    # Do something with the file
            myfile.write('\n')
            myfile.write(str(place) + '\n')
            myfile.close()
    except IOError:
        print("bashrc or bash_profile not accessible\nplease insert your bash profile path manually in the script")

print('close and open a terminal to witness banners')
