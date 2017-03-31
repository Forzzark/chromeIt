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
    
  
def p_effect(p):
  '''effect : ID effectDevice 
            | ID effectDevice effect'''
  
def p_effectDevice(p):
  '''effectDevice : mouseEffect 
                  | keyboardEffect'''
  
def p_mouseEffect(p):
  'mouseEffect : MOUSE mouseEffectType '
  
def p_keyboardEffect(p):
  'keyboardEffect : KEYBOARD keyboardEffectType '
  
def p_mouseEffectType(p):
  '''mouseEffectType : STATIC staticArgument 
                     | BLINK blinkArguments 
                     | SPECTRUM + spectrumArguments 
                     | CUSTOM + customMouseArguments'''  

def p_keyboardEffectType(p):
  '''keyboardEffectType : STATIC staticArgument 
                        | BLINK blinkArguments 
                        | SPECTRUM spectrumArguments 
                        | CUSTOM customMouseArguments 
                        | WAVE waveArguments 
                        | BREATHE breatheArguments 
                        | REACT reactArguments 
                        | CUSTOM customKeyboardArguments 
                        | STARLIGHT starlightArguments'''    

def p_staticArguments(p):
  'staticArgument : color'
  
def p_blinkArguments(p):
  'blinkArguments : TIME TIME colors'
  
def p_spectrumArguments(p):
  'spectrumArguments : TIME'
  
def p_waveArguments(p):
  'keyboardEffect : direction'
  
def p_direction(p):
  '''direction : L2R 
              | R2L'''

def p_breatheArguments(p):
  'breatheArguments : breatheType colors'  
  
def p_reactArguments(p):
  'reactArguments : color reactType'  
  
def p_starlightArguments(p):
  'starlightArguments : NUMBER'''  
  
def p_customMouseArguments(p):
  '''customMouseArguments : zone color 
                          | zone color customMouseArguments'''  
  
def p_customKeyboardArguments(p):
  '''customKeyboardArguments : key color 
                             | key color customKeyboardArguments'''

def p_zone(p):
  '''zone: TOP 
         | MIDDLE 
         | BOTTOM'''
  
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
  
def p_playSequence(p):
  '''playSequence: ID NUMBER
                 | ID NUMBER playSequence'''

def p_colors(p):
  '''colors: color 
           | color colors'''
  
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

def p_rgbColor(p):
  'rgbColor: RGB LP RGBNUM COMA RGBNUM COMA RGBNUM RP'   

def p_reactType(p):
  '''reactType: SHORT 
              | MEDIUM
              | LONG'''
  
def p_breatheType(p):
  '''breatheType: SLOW 
                | MEDIUM 
                | FAST''' 
  
def p_direction(p):
  '''direction: L2R 
              | R2L'''
  

  
# Error rule 
def p_error(p):
    print("Syntax error in input")
    
    
#---------------------------------------------#
#           Python Intermediate Code          #
#---------------------------------------------#


ids = []
