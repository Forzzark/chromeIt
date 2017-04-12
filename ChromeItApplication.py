import chromeItParser as parser

import subprocess
import os


file = "ChromeItCode.txt"

parser.translateCode(file)


devToolPath = open("setting1.txt").read()
cmds = ['C:', "cd ../", 'VsDevCmd.bat', os.getcwd()[:2], 'cd chromeIt/chromeitcompilable','cl /EHsc /MD RazerChromaApplication.cpp ChromaSDKImpl.cpp']
#cmds = [devToolPath[:2], "cd " +devToolPath[3:] , 'VsDevCmd.bat', os.getcwd()[:2], 'cd chromeitcompilable','cl /EHsc /MD RazerChromaApplication.cpp ChromaSDKImpl.cpp']

encoding = 'latin1'

p = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for cmd in cmds:
    p.stdin.write(cmd + "\n")
p.stdin.close()
print (p.stdout.read())



