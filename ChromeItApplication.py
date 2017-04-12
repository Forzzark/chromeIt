import chromeItParser as parser

import subprocess


file = "ChromeItCode.txt"

parser.translateCode(file)



cmds = ['G:', 'cd Visual Studio Enterprise\Common7\Tools', 'VsDevCmd.bat', 'C:', 'cd chromeitcompilable','cl /EHsc /MD RazerChromaApplication.cpp ChromaSDKImpl.cpp']
encoding = 'latin1'
p = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE,
             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for cmd in cmds:
    p.stdin.write(cmd + "\n")
p.stdin.close()
print (p.stdout.read())



