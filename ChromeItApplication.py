import chromeItParser as parser
import time
print "Welcome to ChromeIt!\n"
time.sleep(.25)
print "Processing ChromeIt Code.\n"
time.sleep(.25)
print "----------------------------------------------------------------------------------\nERRORS:"

file = "ChromeItCode.txt"

try:
    parser.translateCode(file)
    print "NONE\n----------------------------------------------------------------------------------\n\n\nNo errors during translation. \'ChromeItCompilable\' folder is ready for compilation. Thanks for using ChromeIt!\n\n\n"

except:
    print "----------------------------------------------------------------------------------\nAn Error Occured while translating code. Check Error messages above or contact the developers."

