import chromeItParser as parser
import subprocess
import os
import time



print "Welcome to ChromeIt!\n"
time.sleep(.25)
print "Processing ChromeIt Code.\n"
time.sleep(.25)
print "----------------------------------------------------------------------------------\nERRORS:"

file = "ChromeItCode.txt"

try:
    parser.translateCode(file)
    print "NONE\n----------------------------------------------------------------------------------\n\n\nNo errors during translation. \'ChromeItCompilable\' folder is ready for compilation."

except:
    print "----------------------------------------------------------------------------------\nAn Error Occured while translating code. Check Error messages above or contact the developers."



print "Attempting to compile ChromeIt App...\n"
print "----------------------------------------------------------------------------------\nERRORS:"

try:

    devToolPath = open("setting1.txt").read()
    log = open("log.txt", 'w+')
    cmds = ['C:', "cd ../", 'VsDevCmd.bat', os.getcwd()[:2], 'cd chromeIt/chromeitcompilable','cl /EHsc /MD RazerChromaApplication.cpp ChromaSDKImpl.cpp']

    encoding = 'latin1'

    p = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for cmd in cmds:
        p.stdin.write(cmd + "\n")
    p.stdin.close()
    log.write(p.stdout.read())
    print "NONE\n----------------------------------------------------------------------------------\n\n\nNo errors during compilation process. \n\nRazerChromaApplication is ready for execution. You can find it in the ChromeItCompilable folder. \n\nThanks for using ChromeIt!\n\n\n"

except:
    print "Please contact the developers for assistance. Include the log.txt file.\n----------------------------------------------------------------------------------\nAn Error Occured while compiling code. \nPlease contact the developers for assistance."




