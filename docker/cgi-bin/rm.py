#!/usr/bin/python3
print("content-text: type/plain")
print()

import subprocess as sp
import cgi
import os

field = cgi.FieldStorage()
osname = field.getvalue("osn")

cmd = "sudo docker rm -f {}".format(osname)
output = sp.getoutput(cmd)

print(output)
