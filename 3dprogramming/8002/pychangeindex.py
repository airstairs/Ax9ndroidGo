import os
import time
go = True
while go:
    os.system("cat file2 > index.html")
    os.system("cat index.html")
    os.system("echo")
    time.sleep(3)
    os.system("cat file1 > index.html")
    os.system("echo")
    os.system("cat index.html")
    time.sleep(3)
