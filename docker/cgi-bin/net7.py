!#/usr/bin/python3
print("content-text: type/plain")
print()

import subprocess as sp
import cgi
import os

field = cgi.FieldStorage()

cmd = "sudo docker network prune -y"
output = sp.getoutput(cmd)

print(output)
