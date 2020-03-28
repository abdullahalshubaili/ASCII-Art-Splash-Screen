import os
import subprocess

#folderr = subprocess.check_output('pwd')[:-1]

class Getdir():        
    def __init__(self):
        folderr = subprocess.check_output('pwd')[:-1]
        self.ff = folderr.decode('utf-8')

    def __repr__(self):
        return repr(self.ff)


