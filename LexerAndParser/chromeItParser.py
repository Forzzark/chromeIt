#---------------------------------------------#
#              ChromeIT Parser                #
#---------------------------------------------#
import ply.yacc as yacc 

import chromeItLexer
#Get tokens from lexer
tokens = chromeItLexer.tokens

#---------------------------------------------#
#           ChromeIT Grammar Rules            #
#---------------------------------------------#


def p_start(p):
  'start : effect playSequence'
  p[0] = p[1] + p[2]

  createEffects(p[1])
  playEffects(p[2])
    
  
def p_effect(p):
  '''effect : ID effectDevice 
            | ID effectDevice effect'''

  if(len(p) == 2):
    p[0] = [[p[1]].extend(p[2])]
  else:
    [[p[1]].extend(p[2])].extend(p[3])



  
def p_effectDevice(p):
  '''effectDevice : mouseEffect 
                  | keyboardEffect'''
  p[0] = p[1]

def p_mouseEffect(p):
  'mouseEffect : MOUSE mouseEffectType '
  p[0] = [1].extend(p[2])

def p_keyboardEffect(p):
  'keyboardEffect : KEYBOARD keyboardEffectType '
  p[0] = [2].extend(p[2])
  
def p_mouseEffectType(p):
  #1 Static Arguments order: [color]
  #2 Blink Arguments order: [TIME, TIME, [COLORS]]
  #3 Spectrum Arguments order: [TIME]
  #4 Custom Arguments order: [[zone, color],[zone, color]...]


  '''mouseEffectType : STATIC staticArguments
                     | BLINK blinkArguments
                     | SPECTRUM + spectrumArguments
                     | CUSTOM + customMouseArguments'''
  if (p[2] == "static"):
    p[0] = [1].extend[p[2]]
  elif (p[2] == "blink"):
    p[0] = [2].extend[p[2]]
  elif (p[2] == "spectrum"):
    p[0] = [3].extend[p[2]]
  elif (p[2] == "custom"):
    p[0] = [4].extend[p[2]]


def p_keyboardEffectType(p):
  #1 Static Arguments order: [color]
  #2 Blink Arguments order: [TIME, TIME, [COLORS]]
  #3 Spectrum Arguments order: [TIME]
  #4 Custom Arguments order: [[key, color],[key, color]...]
  #5 Wave Arguments order: [direction]
  #6 Breathe Arguments order: [breatheType, [Colors]]
  #7 React Arguments order: [reactType, color]
  #8 Starlight Arguments order: [NUMBER]


  '''keyboardEffectType : STATIC staticArguments
                        | BLINK blinkArguments
                        | SPECTRUM spectrumArguments
                        | CUSTOM customMouseArguments
                        | WAVE waveArguments
                        | BREATHE breatheArguments
                        | REACT reactArguments
                        | STARLIGHT starlightArguments'''

  if(p[2] == "static"):
    p[0] = [1].extend[p[2]]
  elif(p[2] == "blink"):
    p[0] = [2].extend[p[2]]
  elif (p[2] == "spectrum"):
    p[0] = [3].extend[p[2]]
  elif (p[2] == "custom"):
    p[0] = [4].extend[p[2]]
  elif (p[2] == "wave"):
    p[0] = [5].extend[p[2]]
  elif (p[2] == "breathe"):
    p[0] = [6].extend[p[2]]
  elif (p[2] == "react"):
    p[0] = [7].extend[p[2]]
  elif(p[2] == "starlight"):
    p[0] = [8].extend[p[2]]



def p_staticArguments(p):
  'staticArgument : color'
  p[0] = [p[1]]

  
def p_blinkArguments(p):
  'blinkArguments : TIME TIME colors'
  p[0] = [p[1], p[2] , p[3]]
  
def p_spectrumArguments(p):
  'spectrumArguments : TIME'
  p[0] = [p[1]]
  
def p_waveArguments(p):
  'keyboardEffect : direction'
  p[0] = [p[1]]
  
def p_direction(p):
  '''direction : L2R 
              | R2L'''
  p[0] = p[1]

def p_breatheArguments(p):
  'breatheArguments : breatheType colors'
  p[0] = [p[1], p[2]]
  
def p_reactArguments(p):
  'reactArguments : reactType color'
  p[0] = [p[1], p[2]]
  
def p_starlightArguments(p):
  'starlightArguments : NUMBER'
  p[0] = [p[1]]
  
def p_customMouseArguments(p):
  '''customMouseArguments : zone color 
                          | zone color customMouseArguments'''
  if(len(p) == 2):
    p[0] = [[p[1], p[2]]]
  else:
    p[0] = [[p[1], p[2]]].extend(p[3])
  
def p_customKeyboardArguments(p):
  '''customKeyboardArguments : key color 
                             | key color customKeyboardArguments'''
  if (len(p) == 2):
    p[0] = [[p[1], p[2]]]
  else:
    p[0] = [[p[1], p[2]]].extend(p[3])

def p_zone(p):
  '''zone: TOP 
         | MIDDLE 
         | BOTTOM'''
  p[0] = p[1]
  
def p_key(p):
  '''key: RZKEY_ESC 
        | RZKEY_F1
        | RZKEY_F2 
        | RZKEY_F3 
        | RZKEY_F4 
        | RZKEY_F5 
        | RZKEY_F6 
        | RZKEY_F7 
        | RZKEY_F8 
        | RZKEY_F9 
        | RZKEY_F10 
        | RZKEY_F11 
        | RZKEY_F12 
        | RZKEY_1 
        | RZKEY_2 
        | RZKEY_3 
        | RZKEY_4 
        | RZKEY_5 
        | RZKEY_6 
        | RZKEY_7 
        | RZKEY_8 
        | RZKEY_9 
        | RZKEY_0 
        | RZKEY_A 
        | RZKEY_B 
        | RZKEY_C 
        | RZKEY_D 
        | RZKEY_E 
        | RZKEY_F 
        | RZKEY_G 
        | RZKEY_H 
        | RZKEY_I 
        | RZKEY_J 
        | RZKEY_K 
        | RZKEY_L 
        | RZKEY_M 
        | RZKEY_N
        | RZKEY_O 
        | RZKEY_P 
        | RZKEY_Q 
        | RZKEY_R
        | RZKEY_S 
        | RZKEY_T
        | RZKEY_U
        | RZKEY_V 
        | RZKEY_W 
        | RZKEY_X 
        | RZKEY_Y 
        | RZKEY_Z 
        | RZKEY_NUMLOCK 
        | RZKEY_NUMPAD 
        | RZKEY_NUMPAD2 
        | RZKEY_NUMPAD3 
        | RZKEY_NUMPAD4 
        | RZKEY_NUMPAD5 
        | RZKEY_NUMPAD6 
        | RZKEY_NUMPAD7 
        | RZKEY_NUMPAD8 
        | RZKEY_NUMPAD9 
        | RZKEY_NUMPAD_DIVIDE 
        | RZKEY_NUMPAD_MULTIPLY 
        | RZKEY_NUMPAD_SUBTRACT 
        | RZKEY_NUMPAD_ADD 
        | RZKEY_NUMPAD_ENTER 
        | RZKEY_NUMPAD_DECIMAL 
        | RZKEY_PRINTSCREEN 
        | RZKEY_SCROLL 
        | RZKEY_PAUSE
        | RZKEY_INSERT
        | RZKEY_HOME
        | RZKEY_PAGEUP
        | RZKEY_DELETE 
        | RZKEY_END 
        | RZKEY_PAGEDOWN 
        | RZKEY_UP 
        | RZKEY_LEFT 
        | RZKEY_DOWN 
        | RZKEY_RIGHT
        | RZKEY_TAB
        | RZKEY_CAPSLOCK 
        | RZKEY_BACKSPACE 
        | RZKEY_ENTER 
        | RZKEY_LCTRL 
        | RZKEY_LWIN 
        | RZKEY_LALT 
        | RZKEY_SPACE 
        | RZKEY_RALT 
        | RZKEY_FN 
        | RZKEY_RMENU 
        | RZKEY_RCTRL 
        | RZKEY_LSHIFT 
        | RZKEY_RSHIFT 
        | RZKEY_MACRO1 
        | RZKEY_MACRO2 
        | RZKEY_MACRO3 
        | RZKEY_MACRO4 
        | RZKEY_MACRO5 
        | RZKEY_OEM_1 
        | RZKEY_OEM_2 
        | RZKEY_OEM_3 
        | RZKEY_OEM_4 
        | RZKEY_OEM_5 
        | RZKEY_OEM_6
        | RZKEY_OEM_7
        | RZKEY_OEM_8 
        | RZKEY_OEM_9 
        | RZKEY_OEM_10 
        | RZKEY_OEM_11
        | RZKEY_EUR_1
        | RZKEY_EUR_2 
        | RZKEY_JPN_1 
        | RZKEY_JPN_2 
        | RZKEY_JPN_3 
        | RZKEY_JPN_4 
        | RZKEY_JPN_5 
        | RZKEY_KOR_1 
        | RZKEY_KOR_2 
        | RZKEY_KOR_3 
        | RZKEY_KOR_4 
        | RZKEY_KOR_5 
        | RZKEY_KOR_6
        | RZKEY_KOR_7'''
  p[0] = p[1]
  
def p_playSequence(p):
  '''playSequence: ID NUMBER
                 | ID NUMBER playSequence'''

  if(len(p) == 2):
    p[0] = [[p[1], p[2]]]
  else:
    p[0] = [[p[1], p[2]]].extend(p[3])

def p_colors(p):
  '''colors: color 
           | color colors'''
  if(len(p) == 1):
    p[0] = [p[1]]
  else:
    p[0] = [p[1]].extend(p[2])
  
def p_color(p):
  '''color: BLACK 
          | RED 
          | WHITE 
          | GREEN 
          | BLUE 
          | YELLOW 
          | PURPLE 
          | CYAN 
          | ORANGE 
          | PINK 
          | GREY 
          | RANDOM 
          | rgbColor'''
  p[0] = p[1]

def p_rgbColor(p):
  'rgbColor: RGB LP RGBNUM COMA RGBNUM COMA RGBNUM RP'
  p[0] = p[1] + p[2] + p[3] + p[4] + p[5]+ p[6]+ p[7] + p[8]

def p_reactType(p):
  '''reactType: SHORT 
              | MEDIUM
              | LONG'''
  p[0] = p[1]
  
def p_breatheType(p):
  '''breatheType: SLOW 
                | MEDIUM 
                | FAST'''
  p[0] = p[1]
  
def p_direction(p):
  '''direction: L2R 
              | R2L'''
  p[0] = p[1]
  

  
# Error rule 
def p_error(p):
    print("Syntax error in input")
    
    
#---------------------------------------------#
#           Python Intermediate Code          #
#---------------------------------------------#

def createEffects(effectsList):
  for effect in effectsList:
    if(effect[1] == 1):
      createMouseEffect(effect)
    elif (effect[1] == 2):
      createKeyboardEffect(effect)

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

def createCustomMouseEffect(name, keyAndColor):
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







#---------------------------------------------#
#             Parser Testing Code             #
#---------------------------------------------#
try:
  ChromeItSource = open("../Testing/Test1.txt", 'r')
except IOError:
  print("Error")
  exit()

fileText = ChromeItSource.read()

parser = yacc.yacc()
res = parser.parse(fileText)