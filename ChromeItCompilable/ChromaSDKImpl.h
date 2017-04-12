
#ifndef _CHROMASDKIMPL_H_
#define _CHROMASDKIMPL_H_

#pragma once

#include "RzChromaSDKDefines.h"
#include "RzChromaSDKTypes.h"
#include "RzErrors.h"

const COLORREF BLACK = RGB(0, 0, 0);
const COLORREF WHITE = RGB(255, 255, 255);
const COLORREF RED = RGB(255, 0, 0);
const COLORREF GREEN = RGB(0, 255, 0);
const COLORREF BLUE = RGB(0, 0, 255);
const COLORREF YELLOW = RGB(255, 255, 0);
const COLORREF PURPLE = RGB(128, 0, 128);
const COLORREF CYAN = RGB(00, 255, 255);
const COLORREF ORANGE = RGB(255, 165, 00);
const COLORREF PINK = RGB(255, 105, 180);
const COLORREF GREY = RGB(125, 125, 125);

#define ALL_DEVICES         0
#define KEYBOARD_DEVICES    1
#define MOUSEMAT_DEVICES    2
#define MOUSE_DEVICES       3
#define HEADSET_DEVICES     4
#define KEYPAD_DEVICES      5

class CChromaSDKImpl
{
public:
	CChromaSDKImpl();
	~CChromaSDKImpl();

	BOOL Initialize();
	BOOL UnInitialize();

	void ShowMouseStaticEffect(COLORREF color);
	void ShowMouseBlinkEffect(int on, int off, COLORREF colors[], int size);
	void ShowMouseSpectrumEffect(int time);
	void ShowMouseCustomEffect(COLORREF colors[], int zones[], int size);

	void ShowKeyboardWaveEffect(int direction);
	void ShowKeyboardSpectrumEffect(int time);
	void ShowKeyboardBreatheEffect(int type, COLORREF colors[]);
	void ShowKeyboardBlinkEffect(int on, int off, COLORREF colors[], int size);
	void ShowKeyboardReactEffect(COLORREF color, int duration);
	void ShowKeyboardStarlightEffect(int atATime, COLORREF color);
	void ShowKeyboardStaticEffect(COLORREF color);
	void ShowKeyboardCustomEffect(COLORREF colors[], int keys[], int size);



	BOOL IsDeviceConnected(RZDEVICEID DeviceId);

private:
	HMODULE m_ChromaSDKModule;
};

#endif
