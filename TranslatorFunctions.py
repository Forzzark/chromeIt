

#---------------------------------------------#
#           Python Intermediate Code          #
#---------------------------------------------#

def createMouseEffect(effect):
    if (effect[0] in keyboardEffects.keys()  or effect[0] in mouseEffects.keys()):
        print("You cannot defined more than one effect with the same ID. ID used more than once: " + effect[0])
        exit()
    if(effect[2] == 1):
        createStaticMouseEffect(effect[0], effect[3])
    elif(effect[2] == 2):
        createBlinkMouseEffect(effect[0], effect[3], effect[4], effect[5])
    elif (effect[2] == 3):
        createSpectrumMouseEffect(effect[0], effect[3])
    elif (effect[2] == 4):
        createCustomMouseEffect(effect[0], effect[3])

def createKeyboardEffect(effect):
    if (effect[0] in keyboardEffects.keys()  or effect[0] in mouseEffects.keys()):
        print("You cannot defined more than one effect with the same ID. ID used more than once: " + effect[0])
        exit()

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
        createStarlightKeyboardEffect(effect[0], effect[3], effect[4])


def playEffects(effects):
    RazerChromaApplication(effects)

#-----------------------------------------------#
#                Call Methods                   #
#-----------------------------------------------#

mouseEffects = {}
mouseEffectsPrecalls = {}
keyboardEffects = {}
keyboardEffectsPrecalls = {}
mouseClock = 0
kbClock = 0

def createStaticMouseEffect(name, color):
    mouseEffectsPrecalls[str(name)] = ""

    mouseEffects[str(name)] = "m_ChromaSDKImpl." + "ShowMouseStaticEffect(" + str(color) + ");"

def createBlinkMouseEffect(name, timeOn, timeOf, colors):
    string = "\n\tCOLORREF " + name + "Colors[] =  {"
    for color in colors:
        string += str(color) + ","
    mouseEffectsPrecalls[str(name)] = string[:-1] + "};"
    mouseEffects[str(name)] = "\n\tm_ChromaSDKImpl." + "ShowMouseBlinkEffect(" + str(timeOn) + "," + str(timeOf) + "," + name + "Colors" + "," + str(len(colors)) + ");"

def createSpectrumMouseEffect(name, time):
    mouseEffectsPrecalls[str(name)] = ""
    mouseEffects[str(name)] = "m_ChromaSDKImpl." + "ShowMouseSpectrumEffect(" + str(time) + ");"

def createCustomMouseEffect(name, keysAndColors):
    colorsString = "\n\tCOLORREF " + name + "Colors[] =  {"
    zonesString = "\n\tint " + name + "Zones[] =  {"
    for keyAndColor in keysAndColors:
        if(keyAndColor[0] is "TOP"):
            zonesString += "ChromaSDK::Mouse::RZLED2_SCROLLWHEEL,"
        elif(keyAndColor[0] is "MIDDLE"):
            zonesString += "ChromaSDK::Mouse::RZLED2_BACKLIGHT,"
        elif (keyAndColor[0] is "BOTTOM"):
            zonesString += "ChromaSDK::Mouse::RZLED2_LOGO,"
        colorsString += str(keyAndColor[1]) + ","
    string2 = "};"
    mouseEffectsPrecalls[str(name)] = colorsString[:-1] + "}; \n\t" + zonesString[:-1] + string2
    mouseEffects[str(name)] = "\n\tm_ChromaSDKImpl." + "ShowMouseCustomEffect(" + name + "Colors" + "," + name + "Zones" + "," + str(len(keysAndColors)) + ");"

def createStaticKeyboardEffect(name, color):
    keyboardEffectsPrecalls[str(name)] = ""
    keyboardEffects[str(name)] = "m_ChromaSDKImpl." + "ShowKeyboardStaticEffect(" + str(color) + ");"

def createBlinkKeyboardEffect(name, timeOn, timeOf, colors):
    string = "\n\tCOLORREF " + name + "Colors[] =  {"
    for color in colors:
        string += str(color) + ","
    string2 = "};"
    keyboardEffectsPrecalls[str(name)] = string[:-1] + string2
    keyboardEffects[str(name)] =  "\n\tm_ChromaSDKImpl." + "ShowKeyboardBlinkEffect(" + str(timeOn) + "," + str(timeOf) + "," + name + "Colors" + "," + str(len(colors)) + ");"

def createSpectrumKeyboardEffect(name, time):
    keyboardEffectsPrecalls[str(name)] = ""
    keyboardEffects[str(name)] = "m_ChromaSDKImpl." + "ShowKeyboardSpectrumEffect(" + str(time) + ");"

def createCustomKeyboardEffect(name, keysAndColors):
    colorsString = "\n\tCOLORREF " + name + "Colors[] =  {"
    keysString = "\n\tint " + name + "Keys[] =  {"
    for keyAndColor in keysAndColors:
        keysString += "ChromaSDK::Keyboard::" + keyAndColor[0] + ","
        colorsString += str(keyAndColor[1]) + ","
    string2 = "};"
    keyboardEffectsPrecalls[str(name)] = colorsString[:-1] + "}; \n\t" + keysString[:-1] + string2
    keyboardEffects[str(name)] = "\n\tm_ChromaSDKImpl." + "ShowKeyboardCustomEffect(" + name + "Colors" + "," + name + "Keys" + "," + str(len(keysAndColors)) + ");"

def createWaveKeyboardEffect(name, direction):
    keyboardEffectsPrecalls[str(name)] = ""
    if(direction == "L2R"):
        keyboardEffects[str(name)] = "m_ChromaSDKImpl." + "ShowKeyboardWaveEffect(" + "ChromaSDK::Keyboard::WAVE_EFFECT_TYPE::DIRECTION_LEFT_TO_RIGHT);"
    elif(direction == "R2L"):
        keyboardEffects[str(name)] = "m_ChromaSDKImpl." + "ShowKeyboardWaveEffect(" + "ChromaSDK::Keyboard::WAVE_EFFECT_TYPE::DIRECTION_RIGHT_TO_LEFT);"

def createBreatheKeyboardEffect(name, type, colors):
    string = "\n\tCOLORREF " + name + "Colors[] =  { "
    if len(colors) is not 0:
        for color in colors:
            string += str(color) + ","
    else:
        string += "NULL "
    if(type == "TWOCOLORS"):
        string2 = "\n\tm_ChromaSDKImpl." + "ShowKeyboardBreatheEffect(" + str(0) + ","+ name + "Colors" + ");"
    elif (type == "RANDOM"):
        string2 = "\n\tm_ChromaSDKImpl." + "ShowKeyboardBreatheEffect(" + str(1) + "," + name + "Colors" + ");"

    keyboardEffectsPrecalls[str(name)] = string[:-1] + "};"
    keyboardEffects[str(name)] = string2

def createReactKeyboardEffect(name, type, color):

    if (type == "SHORT"):
        string2 = "\n\tm_ChromaSDKImpl." + "ShowKeyboardReactEffect(" + str(color) + "," + str(0) + ");"
    elif (type == "MEDIUM"):
        string2 = "\n\tm_ChromaSDKImpl." + "ShowKeyboardReactEffect(" + str(color) + "," + str(1) + ");"
    elif (type == "LONG"):
        string2 = "\n\tm_ChromaSDKImpl." + "ShowKeyboardReactEffect(" + str(color) + "," + str(2) + ");"

    keyboardEffectsPrecalls[str(name)] = ""
    keyboardEffects[str(name)] = string2

def createStarlightKeyboardEffect(name, lightCount, color):
    keyboardEffectsPrecalls[str(name)] = ""
    keyboardEffects[str(name)] = "m_ChromaSDKImpl." + "ShowKeyboardStarlightEffect(" + str(lightCount) + ", " + str(color) + ");"



def RazerChromaApplication(effectsCalls):

    alreadyWrittenEffects= []
    appFile = open('ChromeItCompilable/RazerChromaApplication.cpp', 'w+')
    # Concatenated between lines to facilitate reading and future editing.


    #Write header files

    appFile.write("#include \"stdafx.h\"" + "\n// RazerChromaSampleApplication.cpp : Defines the class behaviors for the application." + "\n#include \"ChromaSDKImpl.h\"" + "\n#include \"resource.h\"" + "\n#include <iostream>" + "\n#include <thread>" + "\n" + "\nusing namespace std;" + "\n" + "\nCChromaSDKImpl m_ChromaSDKImpl;" + "\nlong kbStart = 0;"
 + "\nlong mouseStart = 0; ")

    for effect in effectsCalls:
        if effect[0] not in mouseEffects.keys() and effect[0] not in keyboardEffects.keys():
            print("At least one of the IDs in the play sequence is not defined")
            exit()

    #Write mouse thread
    appFile.write("\n\tvoid mouse(){")

    #write mouse precalls
    for effect in effectsCalls:
        if effect[0] in mouseEffects.keys():
            if effect[0] not in alreadyWrittenEffects:
                appFile.write("\n\t\t\t" + mouseEffectsPrecalls[effect[0]])
                alreadyWrittenEffects.append(effect[0])
    appFile.write("\n\t\twhile(true){")

    #Write mouse effect calls
    for effect in effectsCalls:
        if effect[0] in mouseEffects.keys():
            appFile.write("\n\t\tmouseStart = clock();")
            appFile.write("\n\t\twhile(clock() - mouseStart < " + str(effect[1]) + "){")
            appFile.write("\n\t\t\t" + mouseEffects[effect[0]])
            appFile.write("\n\t\t}")
    appFile.write("\n\t\t}")

    appFile.write("\n\t}")

    #Write kb thread
    appFile.write("\n\tvoid keyboard(){")

    # Write kb precalls
    for effect in effectsCalls:
        if effect[0] in keyboardEffects.keys():
            if effect[0] not in alreadyWrittenEffects:
                appFile.write("\n\t\t\t" + keyboardEffectsPrecalls[effect[0]])
                alreadyWrittenEffects.append(effect[0])
    appFile.write("\n\t\twhile(true){")

    # Write kb effect calls
    for effect in effectsCalls:
        if effect[0] in keyboardEffects.keys():
            appFile.write("\n\t\tkbStart = clock();")
            appFile.write("\n\t\twhile(clock() - kbStart < " + str(effect[1]) + "){")
            appFile.write("\n\t\t\t" + keyboardEffects[effect[0]])
            appFile.write("\n\t\t}")
    appFile.write("\n\t\t}")
    appFile.write("\n\t}")

    #Write Main function which activate threads
    appFile.write("\n\tint main() {" + "\n\t\tm_ChromaSDKImpl.Initialize();")
    appFile.write("\n\t\tSleep(2000);")
    appFile.write("\n\t\tthread t1(mouse);")
    appFile.write("\n\t\tthread t2(keyboard);")
    appFile.write("\n\t\tt1.join();")
    appFile.write("\n\t\tt2.join();")
    appFile.write("\n\t\treturn 0;\n\t}")







    appFile.close()
