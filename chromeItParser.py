#---------------------------------------------#
#              ChromeIT Parser                #
#---------------------------------------------#
import ply.yacc as yacc
import TranslatorFunctions as toCFunctions

import chromeItLexer
#Get tokens from lexer
tokens = chromeItLexer.tokens

#---------------------------------------------#
#           ChromeIT Grammar Rules            #
#---------------------------------------------#


def p_start(p):
  'start : effect COLON COLON playSequence'

  createEffects(p[1])
  playEffects(p[4])


    
  
def p_effect(p):
  '''effect : ID effectDevice 
            | ID effectDevice effect'''


  if(len(p) == 3):
    f = [p[1]]
    f.extend(p[2])
    p[0] = [f]
  else:
    f = [p[1]]
    f.extend(p[2])
    x = [f]
    x.extend(p[3])
    p[0] = x




  
def p_effectDevice(p):
  '''effectDevice : mouseEffect 
                  | keyboardEffect'''

  f = p[1]
  p[0] = f


def p_mouseEffect(p):
  'mouseEffect : MOUSE mouseEffectType'

  f = [1]
  f.extend(p[2])

  p[0] = f


def p_keyboardEffect(p):
  'keyboardEffect : KEYBOARD keyboardEffectType'
  f=[2]
  f.extend(p[2])
  p[0] = f

  
def p_mouseEffectType(p):
  #1 Static Arguments order: [color]
  #2 Blink Arguments order: [NUMBER, NUMBER, [COLORS]]
  #3 Spectrum Arguments order: [NUMBER]
  #4 Custom Arguments order: [[zone, color],[zone, color]...]


  '''mouseEffectType : STATIC staticArguments
                     | BLINK blinkArguments
                     | SPECTRUM spectrumArguments
                     | CUSTOM customMouseArguments'''


  if (p[1] == "STATIC"):
    f = [1]
    f.extend(p[2])
    p[0] = f
  elif (p[1] == "BLINK"):
    f = [2]
    f.extend(p[2])
    p[0] = f
  elif (p[1] == "SPECTRUM"):
    f = [3]
    f.extend(p[2])
    p[0] = f
  elif (p[1] == "CUSTOM"):
    f = [4]
    f.extend(p[2])
    p[0] = f


def p_keyboardEffectType(p):
  #1 Static Arguments order: [color]
  #2 Blink Arguments order: [NUMBER, NUMBER, [COLORS]]
  #3 Spectrum Arguments order: [NUMBER]
  #4 Custom Arguments order: [[key, color],[key, color]...]
  #5 Wave Arguments order: [direction]
  #6 Breathe Arguments order: [breatheType, [Colors]]
  #7 React Arguments order: [reactType, color]
  #8 Starlight Arguments order: [NUMBER, color]


  '''keyboardEffectType : STATIC staticArguments
                        | BLINK blinkArguments
                        | SPECTRUM spectrumArguments
                        | CUSTOM customKeyboardArguments
                        | WAVE waveArguments
                        | BREATHE breatheArguments
                        | REACT reactArguments
                        | STARLIGHT starlightArguments'''
  if (p[1] == "STATIC"):
    f = [1]
    f.extend(p[2])
    p[0] = f
  elif (p[1] == "BLINK"):
    f = [2]
    f.extend(p[2])
    p[0] = f
  elif (p[1] == "SPECTRUM"):
    f = [3]
    f.extend(p[2])
    p[0] = f
  elif (p[1] == "CUSTOM"):
    f = [4]
    f.extend(p[2])
    p[0] = f
  elif (p[1] == "WAVE"):
    f = [5]
    f.extend(p[2])
    p[0] = f
  elif (p[1] == "BREATHE"):
    f = [6]
    f.extend(p[2])
    p[0] = f
  elif (p[1] == "REACT"):
    f = [7]
    f.extend(p[2])
    p[0] = f
  elif(p[1] == "STARLIGHT"):
    f = [8]
    f.extend(p[2])
    p[0] = f


def p_staticArguments(p):
  'staticArguments : color'

  p[0] = [p[1]]

  
def p_blinkArguments(p):
  'blinkArguments : NUMBER NUMBER colors'
  p[0] = [p[1], p[2] , p[3]]
  
def p_spectrumArguments(p):
  'spectrumArguments : NUMBER'
  p[0] = [p[1]]
  
def p_waveArguments(p):
  'waveArguments : direction'
  p[0] = [p[1]]
  
def p_direction(p):
  '''direction : L2R 
              | R2L'''
  p[0] = p[1]

def p_breatheArguments(p):
  '''breatheArguments : breatheType colors
                      | breatheType'''
  if(len(p)==3):
    p[0] = [p[1], p[2]]
  else:
    p[0] = [p[1], []]
  
def p_reactArguments(p):
  'reactArguments : reactType color'
  p[0] = [p[1], p[2]]
  
def p_starlightArguments(p):
  'starlightArguments : NUMBER color'
  p[0] = [p[1], p[2]]
  
def p_customMouseArguments(p):
  '''customMouseArguments : zone color 
                          | zone color customMouseArguments'''
  if (len(p) == 3):
    p[0] = [[[p[1], p[2]]]]
  else:
    f = [[p[1], p[2]]]
    z = (p[3])[0]
    f.extend(z)
    p[0] = [f]

  
def p_customKeyboardArguments(p):
  '''customKeyboardArguments : key color 
                             | key color customKeyboardArguments'''
  if (len(p) == 3):
    p[0] = [[[p[1], p[2]]]]
  else:
    f = [[p[1], p[2]]]
    z = (p[3])[0]
    f.extend(z)
    p[0] = [f]

def p_zone(p):
  '''zone : TOP
         | MIDDLE 
         | BOTTOM'''
  p[0] = p[1]
  
def p_key(p):
  '''key : RZKEY_ESC
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
  '''playSequence : ID NUMBER
                  | ID NUMBER playSequence'''

  if(len(p) == 3):
    p[0] = [[p[1], p[2]]]
  else:
    f = [[p[1], p[2]]]
    f.extend(p[3])
    p[0] = f

def p_colors(p):
  '''colors : color
           | color colors'''
  if(len(p) == 2):
    p[0] = [p[1]]
  else:
    f = [p[1]]
    f.extend(p[2])
    p[0] = f
  
def p_color(p):
  '''color : BLACK
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
          | rgbColor'''
  p[0] = p[1]

def p_rgbColor(p):
  'rgbColor : RGB LP NUMBER COMA NUMBER COMA NUMBER RP'
  p[0] = p[1] + p[2] + p[3] + p[4] + p[5]+ p[6]+ p[7] + p[8]

def p_reactType(p):
  '''reactType : SHORT
              | MEDIUM
              | LONG'''
  p[0] = p[1]
  
def p_breatheType(p):
  '''breatheType : TWOCOLORS
                 | RANDOM'''
  p[0] = p[1]


# Error rule 
def p_error(p):
    print("Syntax error in input")
    raise

    
#---------------------------------------------#
#           Python Intermediate Code          #
#---------------------------------------------#

def createEffects(effectsList):
  for effect in effectsList:
    if(effect[1] == 1):
      toCFunctions.createMouseEffect(effect)
    elif (effect[1] == 2):
      toCFunctions.createKeyboardEffect(effect)


def playEffects(effects):

    toCFunctions.RazerChromaApplication(effects)



#---------------------------------------------#
#             Parser Testing Code             #
#---------------------------------------------#

def translateCode(p):
  try:
    ChromeItSource = open(p, 'r')
  except IOError:
    print("Error opening file")
    exit()

  fileText = ChromeItSource.read()

  parser = yacc.yacc()
  res = parser.parse(fileText)