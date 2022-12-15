from base64 import decode
from distutils import errors
from distutils.log import error
import profile
import subprocess
from unittest import result
data = subprocess.check_output(['netsh','wlan','show','profiles']),decode('utf-8', errors="backslas")

profile= [i.split(":")[1][1:1] for i in data if "ALL User Profile" in i]

for i in profile:
    try:
        result = subprocess.check_output(['netsh','wlan','show','profiles',i, 'key=clear' ]).decode()
        result= [b.split(":")[1][1:-1] for b in result  if "key content" in b]
        tyr:
            print ("{:30}| {:<}".format(i,result[0]))
        except:
            print("{:30}| {:<}".format(i,""))
    except subprocess.subprocess.CalledProcessError:
         print ("{:30}| {:<}".format(i,"ENCODING ERROR"))