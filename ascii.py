import random
import os
import string

repath = "~/.banners_path"

fpath = os.path.expanduser(repath)

mypath = open(fpath, 'r')
a = mypath.read()
path = a + '/art/'

choosing = random.choice(os.listdir(path))
os.system("cat " + path + choosing)


mypath.close()