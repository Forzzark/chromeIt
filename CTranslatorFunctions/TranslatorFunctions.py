import ChromeItCompilable as Compilable

#---------------------------------------------#
#           Python Intermediate Code          #
#---------------------------------------------#

def createMouseEffect(effect):
    if(effect[2] == 1):
        createStaticMouseEffect(effect[0], effect[3])
    elif(effect[2] == 2):
        createBlinkMouseEffect(effect[0], effect[3], effect[4], effect[5])
    elif (effect[2] == 3):
        createSpectrumMouseEffect(effect[0], effect[3])
    elif (effect[2] == 4):
        createCustomMouseEffect(effect[0], effect[3])

def createKeyboardEffect(effect):
    if (effect[2] == 1):
        createStaticKeyboardEffect(effect[0], effect[3])
    elif (effect[2] == 2):
        createBlinkKeyboardEffect(effect[0], effect[3], effect[4], effect[5])
    elif (effect[2] == 3):
        createSpectrumKeyboardEffect(effect[0], effect[3])
    elif (effect[2] == 4):
        createCustomKeyboardEffect(effect[0], effect[3])
    elif (effect[2] == 5):
        createWaveKeyboardEffect(effect[0], effect[3])
    elif (effect[2] == 6):
        createBreatheKeyboardEffect(effect[0], effect[3], effect[4])
    elif (effect[2] == 7):
        createReactKeyboardEffect(effect[0], effect[3], effect[4])
    elif (effect[2] == 8):
        createStarlightKeyboardEffect(effect[0], effect[3])


def playEffects(effects):
    for effect in effects:
        playEffect(effect[0], effect[1])

#-----------------------------------------------#
#                Call Methods                   #
#-----------------------------------------------#

output = {}

def createStaticMouseEffect(name, color):
    output[str(name)] = "m_ChromaSDKImpl." + "ShowMouseStaticEffect(" + str("\"" + color + "\"") + ");"

def createBlinkMouseEffect(name, timeOn, timeOf, color):
    output[str(name)] = "m_ChromaSDKImpl." + "ShowMouseBlinkEffect(" + str(timeOn) + "," + str(timeOf) + "," + str("\"" + color + "\"") + ");"

def createSpectrumMouseEffect(name, time):
    output[str(name)] = "m_ChromaSDKImpl." + "ShowMouseSpectrumEffect(" + str(time) + ");"

def createCustomMouseEffect(name, keyAndColor):
    output[str(name)] = "m_ChromaSDKImpl." + "ShowMouseCustomEffect(" + str(keyAndColor) + ");"

def createStaticKeyboardEffect(name, color):
    output[str(name)] = "m_ChromaSDKImpl." + "ShowKeyboardStaticEffect(" + str("\"" + color + "\"") + ");"

def createBlinkKeyboardEffect(name, timeOn, timeOf, color):
    output[str(name)] = "m_ChromaSDKImpl." + "ShowKeyboardBlinkEffect(" + str(timeOn) + "," + str(timeOf) + "," + str("\"" + color + "\"") + ");"

def createSpectrumKeyboardEffect(name, time):
    output[str(name)] = "m_ChromaSDKImpl." + "ShowKeyboardSpectrumEffect(" + str(time) + ");"

def createCustomKeyboardEffect(name, keyAndColor):
    output[str(name)] = "m_ChromaSDKImpl." + "ShowKeyboardCustomEffect(" + str(keyAndColor) + ");"

def createWaveKeyboardEffect(name, direction):
    output[str(name)] = "m_ChromaSDKImpl." + "ShowKeyboardWaveEffect(" + str(direction) + ");"

def createBreatheKeyboardEffect(name, type, colors):
    output[str(name)] = "m_ChromaSDKImpl." + "ShowKeyboardBreatheEffect(" + str(type) + "," + str("\"" + colors + "\"") + ");"

def createReactKeyboardEffect(name, type, color):
    output[str(name)] = "m_ChromaSDKImpl." + "ShowKeyboardReactEffect(" + str(type) + "," + str("\"" + color + "\"") + ");"

def createStarlightKeyboardEffect(name, lightCount):
    output[str(name)] = "m_ChromaSDKImpl." + "ShowKeyboardStarlightEffect(" + str(lightCount) + ");"

def playEffect(effectName, times):
    pass

def RazerChromaApplication():
    appFile = open('RazerChromaApplication.cpp', 'w+')
    # Concatenated between lines to facilitate reading and future editing.
    appFile.write("#include \"stdafx.h\"" + "\n// RazerChromaSampleApplication.cpp : Defines the class behaviors for the application." + "\n#include \"ChromaSDKImpl.h\"" + "\n#include \"resource.h\"" + "\n#include <iostream>" + "\n" + "\nusing namespace std;" + "\n" + "\nint main() {" + "\n\tCChromaSDKImpl m_ChromaSDKImpl;" + "\n\tm_ChromaSDKImpl.Initialize();" + "\n\tCOLORREF colors[] = {RED, BLUE};")
    if not output:
        appFile.write("\n\t//There are no functions to call.")
    else:
        outputStrings = output.values()
        for string in outputStrings:
            appFile.write("\n\t" + string)
    appFile.write("\n\treturn 0;\n}")
    appFile.close()
