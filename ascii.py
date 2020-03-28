import random
import os
from pckgs import *
import string

f = str(Getdir())
#to strip "'" from the path 
a = f.strip("'")

path = a + '/art/'
choosing = random.choice(os.listdir(path))
os.system("cat " + path + choosing)


