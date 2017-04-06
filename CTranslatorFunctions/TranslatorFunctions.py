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



def createStaticMouseEffect(name, color):
  pass

def createBlinkMouseEffect(name, timeOn, timeOf, color):
  pass

def createSpectrumMouseEffect(name, time):
  pass

def createCustomMouseEffect(name, zoneAndColor):
  pass



def createStaticKeyboardEffect(name, color):
  pass

def createBlinkKeyboardEffect(name, timeOn, timeOf, color):
  pass

def createSpectrumKeyboardEffect(name, time):
  pass

def createCustomKeyboardEffect(name, keyAndColor):
  pass

def createWaveKeyboardEffect(name, direction):
  pass

def createBreatheKeyboardEffect(name, type, colors):
  pass

def createReactKeyboardEffect(name, type, color):
  pass

def createStarlightKeyboardEffect(name, lightCount):
  pass

def playEffect(effectName, times):
  pass





