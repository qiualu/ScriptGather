import win32api
import getpass
import  os

import wmi,zlib


print(getpass.getuser())
user = getpass.getuser()
exepath = r'C:\Users' + "\\"
exepath += user
exepath += r"\AppData\Local\GP"
print(exepath)
if not os.path.exists(exepath):
      os.makedirs(exepath)
pathinfo = os.path.join(exepath,"path.txt")
with open(pathinfo,"w") as f:
    f.write(os.getcwd())
    f.flush()

with open(pathinfo,"r") as f:
    mm = f.read()
    print(mm)
    print(zlib.adler32(mm.encode()))




