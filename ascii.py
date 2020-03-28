import random
import os
from pckgs import *
import string

#f = str(Getdir())
#to strip "'" from the path 
#a = f.strip("'")
repath = "~/.banners_path"

fpath = os.path.expanduser(repath)

mypath = open(fpath, 'r')
a = mypath.read()
print(a)
path = a + '/art/'
print(path)
choosing = random.choice(os.listdir(path))
os.system("cat " + path + choosing)


mypath.close()