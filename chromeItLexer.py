#---------------------------------------------#
#               ChromeIT Lexer                #
#---------------------------------------------#


import ply.lex as lex

#List of tokens
tokens = [
    # Identifier
    'ID',

    # Numbers
    'NUMBER',

    # Left parenthesis/Right parenthesis/COMA/SEMICOLON
    'LP', 'RP', 'COMA', 'COLON',

    # Colors
    'RED', 'BLUE', 'GREEN', 'YELLOW', 'BLACK', 'WHITE', 'ORANGE', 'GREY', 'CYAN', 'PURPLE', 'PINK', 'RGB',

    # Mouse effect
    'MOUSE',


    # Keyboard effect
    'KEYBOARD',

    # Effect types
    'STATIC', 'BLINK', 'SPECTRUM', 'WAVE', 'BREATHE', 'REACT', 'CUSTOM', 'STARLIGHT',

    # Direction
    'L2R', 'R2L',

    # Breathe Type
    'TWOCOLORS', 'RANDOM',

    # React type
    'SHORT', 'MEDIUM', 'LONG',

    # Zone
    'TOP', 'MIDDLE', 'BOTTOM',

    # Keys
    'RZKEY_NUMLOCK', 'RZKEY_NUMPAD', 'RZKEY_NUMPAD2', 'RZKEY_NUMPAD3', 'RZKEY_NUMPAD4', 'RZKEY_NUMPAD5',
    'RZKEY_NUMPAD6', 'RZKEY_NUMPAD7', 'RZKEY_NUMPAD8', 'RZKEY_NUMPAD9', 'RZKEY_NUMPAD_DIVIDE', 'RZKEY_NUMPAD_MULTIPLY',
    'RZKEY_NUMPAD_SUBTRACT', 'RZKEY_NUMPAD_ADD', 'RZKEY_NUMPAD_ENTER', 'RZKEY_NUMPAD_DECIMAL', 'RZKEY_PRINTSCREEN',
    'RZKEY_SCROLL', 'RZKEY_PAUSE', 'RZKEY_INSERT', 'RZKEY_HOME', 'RZKEY_PAGEUP', 'RZKEY_DELETE', 'RZKEY_END',
    'RZKEY_PAGEDOWN', 'RZKEY_UP', 'RZKEY_LEFT', 'RZKEY_DOWN', 'RZKEY_RIGHT', 'RZKEY_TAB', 'RZKEY_CAPSLOCK',
    'RZKEY_BACKSPACE', 'RZKEY_ENTER', 'RZKEY_LCTRL', 'RZKEY_LWIN', 'RZKEY_LALT', 'RZKEY_SPACE', 'RZKEY_RALT',
    'RZKEY_FN', 'RZKEY_RMENU', 'RZKEY_RCTRL', 'RZKEY_LSHIFT', 'RZKEY_RSHIFT', 'RZKEY_MACRO1', 'RZKEY_MACRO2',
    'RZKEY_MACRO3', 'RZKEY_MACRO4', 'RZKEY_MACRO5', 'RZKEY_OEM_1', 'RZKEY_OEM_2', 'RZKEY_OEM_3', 'RZKEY_OEM_4',
    'RZKEY_OEM_5', 'RZKEY_OEM_6', 'RZKEY_OEM_7', 'RZKEY_OEM_8', 'RZKEY_OEM_9', 'RZKEY_OEM_10', 'RZKEY_OEM_11',
    'RZKEY_EUR_1', 'RZKEY_EUR_2', 'RZKEY_JPN_1', 'RZKEY_JPN_2', 'RZKEY_JPN_3', 'RZKEY_JPN_4', 'RZKEY_JPN_5',
    'RZKEY_KOR_1', 'RZKEY_KOR_2', 'RZKEY_KOR_3', 'RZKEY_KOR_4', 'RZKEY_KOR_5', 'RZKEY_KOR_6', 'RZKEY_KOR_7',
    'RZKEY_ESC', 'RZKEY_F1', 'RZKEY_F2', 'RZKEY_F3', 'RZKEY_F4', 'RZKEY_F5', 'RZKEY_F6', 'RZKEY_F7', 'RZKEY_F8',
    'RZKEY_F9', 'RZKEY_F10', 'RZKEY_F11', 'RZKEY_F12', 'RZKEY_1', 'RZKEY_2', 'RZKEY_3', 'RZKEY_4', 'RZKEY_5',
    'RZKEY_6', 'RZKEY_7', 'RZKEY_8', 'RZKEY_9', 'RZKEY_0', 'RZKEY_A', 'RZKEY_B', 'RZKEY_C', 'RZKEY_D', 'RZKEY_E',
    'RZKEY_F', 'RZKEY_G', 'RZKEY_H', 'RZKEY_I', 'RZKEY_J', 'RZKEY_K', 'RZKEY_L', 'RZKEY_M', 'RZKEY_N', 'RZKEY_O',
    'RZKEY_P', 'RZKEY_Q', 'RZKEY_R', 'RZKEY_S', 'RZKEY_T', 'RZKEY_U', 'RZKEY_V', 'RZKEY_W', 'RZKEY_X', 'RZKEY_Y',
    'RZKEY_Z'

]


#Regular expression for some tokens

t_ID = r'[a-z]([a-z]|[A-Z]|[0-9])+'
t_NUMBER = r'[0-9]+'
t_LP = r'\('
t_RP = r'\)'
t_COMA = r'\,'
t_COLON = r'\:'
t_ignore = ' \t\n'




def t_RZKEY_NUMLOCK(t):
    r'RZKEY_NUMLOCK'
    t.value = 'RZKEY_NUMLOCK'
    return t


def t_RZKEY_NUMPAD(t):
    r'RZKEY_NUMPAD'
    t.value = 'RZKEY_NUMPAD'
    return t


def t_RZKEY_NUMPAD2(t):
    r'RZKEY_NUMPAD2'
    t.value = 'RZKEY_NUMPAD2'
    return t


def t_RZKEY_NUMPAD3(t):
    r'RZKEY_NUMPAD3'
    t.value = 'RZKEY_NUMPAD3'
    return t


def t_RZKEY_NUMPAD4(t):
    r'RZKEY_NUMPAD4'
    t.value = 'RZKEY_NUMPAD4'
    return t


def t_RZKEY_NUMPAD5(t):
    r'RZKEY_NUMPAD5'
    t.value = 'RZKEY_NUMPAD5'
    return t


def t_RZKEY_NUMPAD6(t):
    r'RZKEY_NUMPAD6'
    t.value = 'RZKEY_NUMPAD6'
    return t


def t_RZKEY_NUMPAD7(t):
    r'RZKEY_NUMPAD7'
    t.value = 'RZKEY_NUMPAD7'
    return t


def t_RZKEY_NUMPAD8(t):
    r'RZKEY_NUMPAD8'
    t.value = 'RZKEY_NUMPAD8'
    return t


def t_RZKEY_NUMPAD9(t):
    r'RZKEY_NUMPAD9'
    t.value = 'RZKEY_NUMPAD9'
    return t


def t_RZKEY_NUMPAD_DIVIDE(t):
    r'RZKEY_NUMPAD_DIVIDE'
    t.value = 'RZKEY_NUMPAD_DIVIDE'
    return t


def t_RZKEY_NUMPAD_MULTIPLY(t):
    r'RZKEY_NUMPAD_MULTIPLY'
    t.value = 'RZKEY_NUMPAD_MULTIPLY'
    return t


def t_RZKEY_NUMPAD_SUBTRACT(t):
    r'RZKEY_NUMPAD_SUBTRACT'
    t.value = 'RZKEY_NUMPAD_SUBTRACT'
    return t


def t_RZKEY_NUMPAD_ADD(t):
    r'RZKEY_NUMPAD_ADD'
    t.value = 'RZKEY_NUMPAD_ADD'
    return t


def t_RZKEY_NUMPAD_ENTER(t):
    r'RZKEY_NUMPAD_ENTER'
    t.value = 'RZKEY_NUMPAD_ENTER'
    return t


def t_RZKEY_NUMPAD_DECIMAL(t):
    r'RZKEY_NUMPAD_DECIMAL'
    t.value = 'RZKEY_NUMPAD_DECIMAL'
    return t


def t_RZKEY_PRINTSCREEN(t):
    r'RZKEY_PRINTSCREEN'
    t.value = 'RZKEY_PRINTSCREEN'
    return t


def t_RZKEY_SCROLL(t):
    r'RZKEY_SCROLL'
    t.value = 'RZKEY_SCROLL'
    return t


def t_RZKEY_PAUSE(t):
    r'RZKEY_PAUSE'
    t.value = 'RZKEY_PAUSE'
    return t


def t_RZKEY_INSERT(t):
    r'RZKEY_INSERT'
    t.value = 'RZKEY_INSERT'
    return t


def t_RZKEY_HOME(t):
    r'RZKEY_HOME'
    t.value = 'RZKEY_HOME'
    return t


def t_RZKEY_PAGEUP(t):
    r'RZKEY_PAGEUP'
    t.value = 'RZKEY_PAGEUP'
    return t


def t_RZKEY_DELETE(t):
    r'RZKEY_DELETE'
    t.value = 'RZKEY_DELETE'
    return t


def t_RZKEY_END(t):
    r'RZKEY_END'
    t.value = 'RZKEY_END'
    return t


def t_RZKEY_PAGEDOWN(t):
    r'RZKEY_PAGEDOWN'
    t.value = 'RZKEY_PAGEDOWN'
    return t


def t_RZKEY_UP(t):
    r'RZKEY_UP'
    t.value = 'RZKEY_UP'
    return t


def t_RZKEY_LEFT(t):
    r'RZKEY_LEFT'
    t.value = 'RZKEY_LEFT'
    return t


def t_RZKEY_DOWN(t):
    r'RZKEY_DOWN'
    t.value = 'RZKEY_DOWN'
    return t


def t_RZKEY_RIGHT(t):
    r'RZKEY_RIGHT'
    t.value = 'RZKEY_RIGHT'
    return t


def t_RZKEY_TAB(t):
    r'RZKEY_TAB'
    t.value = 'RZKEY_TAB'
    return t


def t_RZKEY_CAPSLOCK(t):
    r'RZKEY_CAPSLOCK'
    t.value = 'RZKEY_CAPSLOCK'
    return t


def t_RZKEY_BACKSPACE(t):
    r'RZKEY_BACKSPACE'
    t.value = 'RZKEY_BACKSPACE'
    return t


def t_RZKEY_ENTER(t):
    r'RZKEY_ENTER'
    t.value = 'RZKEY_ENTER'
    return t


def t_RZKEY_LCTRL(t):
    r'RZKEY_LCTRL'
    t.value = 'RZKEY_LCTRL'
    return t


def t_RZKEY_LWIN(t):
    r'RZKEY_LWIN'
    t.value = 'RZKEY_LWIN'
    return t


def t_RZKEY_LALT(t):
    r'RZKEY_LALT'
    t.value = 'RZKEY_LALT'
    return t


def t_RZKEY_SPACE(t):
    r'RZKEY_SPACE'
    t.value = 'RZKEY_SPACE'
    return t


def t_RZKEY_RALT(t):
    r'RZKEY_RALT'
    t.value = 'RZKEY_RALT'
    return t


def t_RZKEY_FN(t):
    r'RZKEY_FN'
    t.value = 'RZKEY_FN'
    return t


def t_RZKEY_RMENU(t):
    r'RZKEY_RMENU'
    t.value = 'RZKEY_RMENU'
    return t


def t_RZKEY_RCTRL(t):
    r'RZKEY_RCTRL'
    t.value = 'RZKEY_RCTRL'
    return t


def t_RZKEY_LSHIFT(t):
    r'RZKEY_LSHIFT'
    t.value = 'RZKEY_LSHIFT'
    return t


def t_RZKEY_RSHIFT(t):
    r'RZKEY_RSHIFT'
    t.value = 'RZKEY_RSHIFT'
    return t


def t_RZKEY_MACRO1(t):
    r'RZKEY_MACRO1'
    t.value = 'RZKEY_MACRO1'
    return t


def t_RZKEY_MACRO2(t):
    r'RZKEY_MACRO2'
    t.value = 'RZKEY_MACRO2'
    return t


def t_RZKEY_MACRO3(t):
    r'RZKEY_MACRO3'
    t.value = 'RZKEY_MACRO3'
    return t


def t_RZKEY_MACRO4(t):
    r'RZKEY_MACRO4'
    t.value = 'RZKEY_MACRO4'
    return t


def t_RZKEY_MACRO5(t):
    r'RZKEY_MACRO5'
    t.value = 'RZKEY_MACRO5'
    return t


def t_RZKEY_OEM_1(t):
    r'RZKEY_OEM_1'
    t.value = 'RZKEY_OEM_1'
    return t


def t_RZKEY_OEM_2(t):
    r'RZKEY_OEM_2'
    t.value = 'RZKEY_OEM_2'
    return t


def t_RZKEY_OEM_3(t):
    r'RZKEY_OEM_3'
    t.value = 'RZKEY_OEM_3'
    return t


def t_RZKEY_OEM_4(t):
    r'RZKEY_OEM_4'
    t.value = 'RZKEY_OEM_4'
    return t


def t_RZKEY_OEM_5(t):
    r'RZKEY_OEM_5'
    t.value = 'RZKEY_OEM_5'
    return t


def t_RZKEY_OEM_6(t):
    r'RZKEY_OEM_6'
    t.value = 'RZKEY_OEM_6'
    return t


def t_RZKEY_OEM_7(t):
    r'RZKEY_OEM_7'
    t.value = 'RZKEY_OEM_7'
    return t


def t_RZKEY_OEM_8(t):
    r'RZKEY_OEM_8'
    t.value = 'RZKEY_OEM_8'
    return t


def t_RZKEY_OEM_9(t):
    r'RZKEY_OEM_9'
    t.value = 'RZKEY_OEM_9'
    return t


def t_RZKEY_OEM_10(t):
    r'RZKEY_OEM_10'
    t.value = 'RZKEY_OEM_10'
    return t


def t_RZKEY_OEM_11(t):
    r'RZKEY_OEM_11'
    t.value = 'RZKEY_OEM_11'
    return t


def t_RZKEY_EUR_1(t):
    r'RZKEY_EUR_1'
    t.value = 'RZKEY_EUR_1'
    return t


def t_RZKEY_EUR_2(t):
    r'RZKEY_EUR_2'
    t.value = 'RZKEY_EUR_2'
    return t


def t_RZKEY_JPN_1(t):
    r'RZKEY_JPN_1'
    t.value = 'RZKEY_JPN_1'
    return t


def t_RZKEY_JPN_2(t):
    r'RZKEY_JPN_2'
    t.value = 'RZKEY_JPN_2'
    return t


def t_RZKEY_JPN_3(t):
    r'RZKEY_JPN_3'
    t.value = 'RZKEY_JPN_3'
    return t


def t_RZKEY_JPN_4(t):
    r'RZKEY_JPN_4'
    t.value = 'RZKEY_JPN_4'
    return t


def t_RZKEY_JPN_5(t):
    r'RZKEY_JPN_5'
    t.value = 'RZKEY_JPN_5'
    return t


def t_RZKEY_KOR_1(t):
    r'RZKEY_KOR_1'
    t.value = 'RZKEY_KOR_1'
    return t


def t_RZKEY_KOR_2(t):
    r'RZKEY_KOR_2'
    t.value = 'RZKEY_KOR_2'
    return t


def t_RZKEY_KOR_3(t):
    r'RZKEY_KOR_3'
    t.value = 'RZKEY_KOR_3'
    return t


def t_RZKEY_KOR_4(t):
    r'RZKEY_KOR_4'
    t.value = 'RZKEY_KOR_4'
    return t


def t_RZKEY_KOR_5(t):
    r'RZKEY_KOR_5'
    t.value = 'RZKEY_KOR_5'
    return t


def t_RZKEY_KOR_6(t):
    r'RZKEY_KOR_6'
    t.value = 'RZKEY_KOR_6'
    return t


def t_RZKEY_KOR_7(t):
    r'RZKEY_KOR_7'
    t.value = 'RZKEY_KOR_7'
    return t

def t_MOUSE(t):
	r'MOUSE'
	t.value = 'MOUSE'
	return t

def t_STATIC(t):
	r'STATIC'
	t.value = 'STATIC'
	return t

def t_BLINK(t):
	r'BLINK'
	t.value = 'BLINK'
	return t

def t_SPECTRUM(t):
	r'SPECTRUM'
	t.value = 'SPECTRUM'
	return t

def t_KEYBOARD(t):
	r'KEYBOARD'
	t.value = 'KEYBOARD'
	return t

def t_REACT(t):
	r'REACT'
	t.value = 'REACT'
	return t

def t_CUSTOM(t):
	r'CUSTOM'
	t.value = 'CUSTOM'
	return t

def t_BREATHE(t):
	r'BREATHE'
	t.value = 'BREATHE'
	return t

def t_WAVE(t):
	r'WAVE'
	t.value = 'WAVE'
	return t

def t_STARLIGHT(t):
	r'STARLIGHT'
	t.value = 'STARLIGHT'
	return t

def t_L2R(t):
	r'L2R'
	t.value = 'L2R'
	return t

def t_R2L(t):
	r'R2L'
	t.value = 'R2L'
	return t

def t_SLOW(t):
	r'SLOW'
	t.value = 'SLOW'
	return t

def t_MEDIUM(t):
	r'MEDIUM'
	t.value = 'MEDIUM'
	return t

def t_FAST(t):
	r'FAST'
	t.value = 'FAST'
	return t

def t_SHORT(t):
	r'SHORT'
	t.value = 'SHORT'
	return t

def t_LONG(t):
	r'LONG'
	t.value = 'LONG'
	return t

def t_TOP(t):
	r'TOP'
	t.value = 'TOP'
	return t

def t_MIDDLE(t):
	r'MIDDLE'
	t.value = 'MIDDLE'
	return t

def t_BOTTOM(t):
	r'BOTTOM'
	t.value = 'BOTTOM'
	return t

def t_BLACK(t):
	r'BLACK'
	t.value = 'BLACK'
	return t

def t_RED(t):
	r'RED'
	t.value = 'RED'
	return t

def t_WHITE(t):
	r'WHITE'
	t.value = 'WHITE'
	return t

def t_GREEN(t):
	r'GREEN'
	t.value = 'GREEN'
	return t

def t_BLUE(t):
	r'BLUE'
	t.value = 'BLUE'
	return t

def t_YELLOW(t):
	r'YELLOW'
	t.value = 'YELLOW'
	return t

def t_PURPLE(t):
	r'PURPLE'
	t.value = 'PURPLE'
	return t

def t_CYAN(t):
	r'CYAN'
	t.value = 'CYAN'
	return t

def t_ORANGE(t):
	r'ORANGE'
	t.value = 'ORANGE'
	return t

def t_PINK(t):
	r'PINK'
	t.value = 'PINK'
	return t

def t_GREY(t):
	r'GREY'
	t.value = 'GREY'
	return t

def t_RGB(t):
	r'RGB'
	t.value = 'RGB'
	return t

def t_RANDOM(t):
	r'RANDOM'
	t.value = 'RANDOM'
	return t
def t_TWOCOLORS(t):
	r'TWOCOLORS'
	t.value = 'TWOCOLORS'
	return t

def t_RZKEY_ESC(t):
    r'RZKEY_ESC'
    t.value = 'RZKEY_ESC'
    return t


def t_RZKEY_F1(t):
    r'RZKEY_F1'
    t.value = 'RZKEY_F1'
    return t


def t_RZKEY_F2(t):
    r'RZKEY_F2'
    t.value = 'RZKEY_F2'
    return t


def t_RZKEY_F3(t):
    r'RZKEY_F3'
    t.value = 'RZKEY_F3'
    return t


def t_RZKEY_F4(t):
    r'RZKEY_F4'
    t.value = 'RZKEY_F4'
    return t


def t_RZKEY_F5(t):
    r'RZKEY_F5'
    t.value = 'RZKEY_F5'
    return t


def t_RZKEY_F6(t):
    r'RZKEY_F6'
    t.value = 'RZKEY_F6'
    return t


def t_RZKEY_F7(t):
    r'RZKEY_F7'
    t.value = 'RZKEY_F7'
    return t


def t_RZKEY_F8(t):
    r'RZKEY_F8'
    t.value = 'RZKEY_F8'
    return t


def t_RZKEY_F9(t):
    r'RZKEY_F9'
    t.value = 'RZKEY_F9'
    return t


def t_RZKEY_F10(t):
    r'RZKEY_F10'
    t.value = 'RZKEY_F10'
    return t


def t_RZKEY_F11(t):
    r'RZKEY_F11'
    t.value = 'RZKEY_F11'
    return t


def t_RZKEY_F12(t):
    r'RZKEY_F12'
    t.value = 'RZKEY_F12'
    return t


def t_RZKEY_1(t):
    r'RZKEY_1'
    t.value = 'RZKEY_1'
    return t


def t_RZKEY_2(t):
    r'RZKEY_2'
    t.value = 'RZKEY_2'
    return t


def t_RZKEY_3(t):
    r'RZKEY_3'
    t.value = 'RZKEY_3'
    return t


def t_RZKEY_4(t):
    r'RZKEY_4'
    t.value = 'RZKEY_4'
    return t


def t_RZKEY_5(t):
    r'RZKEY_5'
    t.value = 'RZKEY_5'
    return t


def t_RZKEY_6(t):
    r'RZKEY_6'
    t.value = 'RZKEY_6'
    return t


def t_RZKEY_7(t):
    r'RZKEY_7'
    t.value = 'RZKEY_7'
    return t


def t_RZKEY_8(t):
    r'RZKEY_8'
    t.value = 'RZKEY_8'
    return t


def t_RZKEY_9(t):
    r'RZKEY_9'
    t.value = 'RZKEY_9'
    return t


def t_RZKEY_0(t):
    r'RZKEY_0'
    t.value = 'RZKEY_0'
    return t


def t_RZKEY_A(t):
    r'RZKEY_A'
    t.value = 'RZKEY_A'
    return t


def t_RZKEY_B(t):
    r'RZKEY_B'
    t.value = 'RZKEY_B'
    return t


def t_RZKEY_C(t):
    r'RZKEY_C'
    t.value = 'RZKEY_C'
    return t


def t_RZKEY_D(t):
    r'RZKEY_D'
    t.value = 'RZKEY_D'
    return t


def t_RZKEY_E(t):
    r'RZKEY_E'
    t.value = 'RZKEY_E'
    return t


def t_RZKEY_F(t):
    r'RZKEY_F'
    t.value = 'RZKEY_F'
    return t


def t_RZKEY_G(t):
    r'RZKEY_G'
    t.value = 'RZKEY_G'
    return t


def t_RZKEY_H(t):
    r'RZKEY_H'
    t.value = 'RZKEY_H'
    return t


def t_RZKEY_I(t):
    r'RZKEY_I'
    t.value = 'RZKEY_I'
    return t


def t_RZKEY_J(t):
    r'RZKEY_J'
    t.value = 'RZKEY_J'
    return t


def t_RZKEY_K(t):
    r'RZKEY_K'
    t.value = 'RZKEY_K'
    return t


def t_RZKEY_L(t):
    r'RZKEY_L'
    t.value = 'RZKEY_L'
    return t


def t_RZKEY_M(t):
    r'RZKEY_M'
    t.value = 'RZKEY_M'
    return t


def t_RZKEY_N(t):
    r'RZKEY_N'
    t.value = 'RZKEY_N'
    return t


def t_RZKEY_O(t):
    r'RZKEY_O'
    t.value = 'RZKEY_O'
    return t


def t_RZKEY_P(t):
    r'RZKEY_P'
    t.value = 'RZKEY_P'
    return t


def t_RZKEY_Q(t):
    r'RZKEY_Q'
    t.value = 'RZKEY_Q'
    return t


def t_RZKEY_R(t):
    r'RZKEY_R'
    t.value = 'RZKEY_R'
    return t


def t_RZKEY_S(t):
    r'RZKEY_S'
    t.value = 'RZKEY_S'
    return t


def t_RZKEY_T(t):
    r'RZKEY_T'
    t.value = 'RZKEY_T'
    return t


def t_RZKEY_U(t):
    r'RZKEY_U'
    t.value = 'RZKEY_U'
    return t


def t_RZKEY_V(t):
    r'RZKEY_V'
    t.value = 'RZKEY_V'
    return t


def t_RZKEY_W(t):
    r'RZKEY_W'
    t.value = 'RZKEY_W'
    return t


def t_RZKEY_X(t):
    r'RZKEY_X'
    t.value = 'RZKEY_X'
    return t


def t_RZKEY_Y(t):
    r'RZKEY_Y'
    t.value = 'RZKEY_Y'
    return t


def t_RZKEY_Z(t):
    r'RZKEY_Z'
    t.value = 'RZKEY_Z'
    return t




#Defines error behavior
def t_error(t):
    print("Illegal character '%s'" % t.value[0])


#initializes lexer

lexer = lex.lex()
# try:
#   ChromeItSource = open("test.txt", 'r')
# except IOError:
#   print("Error opening file")
#   exit()
#
# fileText = ChromeItSource.read()
# lexer.input(fileText)
#
# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     print(tok)
