//! \example ChromaSDKImpl.cpp

#include "stdafx.h"
#include "ChromaSDKImpl.h"
#include <iostream>

#ifdef _WIN64
#define CHROMASDKDLL        _T("RzChromaSDK64.dll")
#else
#define CHROMASDKDLL        _T("RzChromaSDK.dll")
#endif

using namespace ChromaSDK;
using namespace ChromaSDK::Keyboard;
using namespace ChromaSDK::Keypad;
using namespace ChromaSDK::Mouse;
using namespace ChromaSDK::Mousepad;
using namespace ChromaSDK::Headset;

typedef RZRESULT(*INIT)(void);
typedef RZRESULT(*UNINIT)(void);
typedef RZRESULT(*CREATEEFFECT)(RZDEVICEID DeviceId, ChromaSDK::EFFECT_TYPE Effect, PRZPARAM pParam, RZEFFECTID *pEffectId);
typedef RZRESULT(*CREATEKEYBOARDEFFECT)(ChromaSDK::Keyboard::EFFECT_TYPE Effect, PRZPARAM pParam, RZEFFECTID *pEffectId);
typedef RZRESULT(*CREATEHEADSETEFFECT)(ChromaSDK::Headset::EFFECT_TYPE Effect, PRZPARAM pParam, RZEFFECTID *pEffectId);
typedef RZRESULT(*CREATEMOUSEPADEFFECT)(ChromaSDK::Mousepad::EFFECT_TYPE Effect, PRZPARAM pParam, RZEFFECTID *pEffectId);
typedef RZRESULT(*CREATEMOUSEEFFECT)(ChromaSDK::Mouse::EFFECT_TYPE Effect, PRZPARAM pParam, RZEFFECTID *pEffectId);
typedef RZRESULT(*CREATEKEYPADEFFECT)(ChromaSDK::Keypad::EFFECT_TYPE Effect, PRZPARAM pParam, RZEFFECTID *pEffectId);
typedef RZRESULT(*SETEFFECT)(RZEFFECTID EffectId);
typedef RZRESULT(*DELETEEFFECT)(RZEFFECTID EffectId);
typedef RZRESULT(*REGISTEREVENTNOTIFICATION)(HWND hWnd);
typedef RZRESULT(*UNREGISTEREVENTNOTIFICATION)(void);
typedef RZRESULT(*QUERYDEVICE)(RZDEVICEID DeviceId, ChromaSDK::DEVICE_INFO_TYPE &DeviceInfo);

INIT Init = NULL;
UNINIT UnInit = NULL;
CREATEEFFECT CreateEffect = NULL;
CREATEKEYBOARDEFFECT CreateKeyboardEffect = NULL;
CREATEMOUSEEFFECT CreateMouseEffect = NULL;
CREATEHEADSETEFFECT CreateHeadsetEffect = NULL;
CREATEMOUSEPADEFFECT CreateMousepadEffect = NULL;
CREATEKEYPADEFFECT CreateKeypadEffect = NULL;
SETEFFECT SetEffect = NULL;
DELETEEFFECT DeleteEffect = NULL;
QUERYDEVICE QueryDevice = NULL;



//Important SDK Methods
CChromaSDKImpl::CChromaSDKImpl() :m_ChromaSDKModule(NULL)
{
}
CChromaSDKImpl::~CChromaSDKImpl()
{
}
BOOL CChromaSDKImpl::Initialize()
{
	if (m_ChromaSDKModule == NULL)
	{
		m_ChromaSDKModule = LoadLibrary(CHROMASDKDLL);
		if (m_ChromaSDKModule == NULL)
		{
			ASSERT(GetLastError() == ERROR_SUCCESS);
			return FALSE;
		}
	}

	if (Init == NULL)
	{
		RZRESULT Result = RZRESULT_INVALID;
		Init = (INIT)GetProcAddress(m_ChromaSDKModule, "Init");
		if (Init)
		{
			Result = Init();
			if (Result == RZRESULT_SUCCESS)
			{
				CreateEffect = (CREATEEFFECT)GetProcAddress(m_ChromaSDKModule, "CreateEffect");
				CreateKeyboardEffect = (CREATEKEYBOARDEFFECT)GetProcAddress(m_ChromaSDKModule, "CreateKeyboardEffect");
				CreateMouseEffect = (CREATEMOUSEEFFECT)GetProcAddress(m_ChromaSDKModule, "CreateMouseEffect");
				CreateHeadsetEffect = (CREATEHEADSETEFFECT)GetProcAddress(m_ChromaSDKModule, "CreateHeadsetEffect");
				CreateMousepadEffect = (CREATEMOUSEPADEFFECT)GetProcAddress(m_ChromaSDKModule, "CreateMousepadEffect");
				CreateKeypadEffect = (CREATEKEYPADEFFECT)GetProcAddress(m_ChromaSDKModule, "CreateKeypadEffect");
				SetEffect = (SETEFFECT)GetProcAddress(m_ChromaSDKModule, "SetEffect");
				DeleteEffect = (DELETEEFFECT)GetProcAddress(m_ChromaSDKModule, "DeleteEffect");
				QueryDevice = (QUERYDEVICE)GetProcAddress(m_ChromaSDKModule, "QueryDevice");

				if (CreateEffect &&
					CreateKeyboardEffect &&
					CreateMouseEffect &&
					CreateHeadsetEffect &&
					CreateMousepadEffect &&
					CreateKeypadEffect &&
					SetEffect &&
					DeleteEffect &&
					QueryDevice)
				{
					return TRUE;
				}
				else
				{
					return FALSE;
				}
			}
		}
	}

	return TRUE;
}
BOOL CChromaSDKImpl::UnInitialize()
{
	if (m_ChromaSDKModule != NULL)
	{
		RZRESULT Result = RZRESULT_INVALID;
		UNINIT UnInit = (UNINIT)GetProcAddress(m_ChromaSDKModule, "UnInit");
		if (UnInit)
		{
			Result = UnInit();
			ASSERT(Result == RZRESULT_SUCCESS);
		}

		FreeLibrary(m_ChromaSDKModule);
		m_ChromaSDKModule = NULL;

		return TRUE;
	}

	return FALSE;
}


//Mouse Effects
void CChromaSDKImpl::ShowMouseStaticEffect(COLORREF color) {
	RZEFFECTID Play = GUID_NULL;



	ChromaSDK::Mouse::CUSTOM_EFFECT_TYPE2 Effect = {};

	for (UINT row = 0; row<ChromaSDK::Mouse::MAX_ROW; row++)
	{
		for (UINT col = 0; col<ChromaSDK::Mouse::MAX_COLUMN; col++)
		{
			Effect.Color[row][col] = color;
		}
	}


	CreateMouseEffect(ChromaSDK::Mouse::CHROMA_CUSTOM2, &Effect, &Play);

	while (true) {
		SetEffect(Play);
	}
}
void CChromaSDKImpl::ShowMouseCustomEffect(COLORREF colors[], int zones[], int size) {
	RZEFFECTID Play = GUID_NULL;



	ChromaSDK::Mouse::CUSTOM_EFFECT_TYPE2 Effect = {};

	for (int index = 0; index < size ; index++)
	{
		
		Effect.Color[HIBYTE(zones[index])][LOBYTE(zones[index])] = colors[index];
	
	}


	CreateMouseEffect(ChromaSDK::Mouse::CHROMA_CUSTOM2, &Effect, &Play);

	while (true) {
		SetEffect(Play);
	}
}
void CChromaSDKImpl::ShowMouseBlinkEffect(int on, int off, COLORREF colors[], int size) {
	//on- time it takes to come on; off - time it takes to come off
	RZEFFECTID Play = GUID_NULL;
	RZEFFECTID Play2 = GUID_NULL;



	ChromaSDK::Mouse::CUSTOM_EFFECT_TYPE2 Effect = {};
	while (true) {
		for (int index = 0; index < size; index++) {
			for (UINT row = 0; row < ChromaSDK::Mouse::MAX_ROW; row++)
			{
				for (UINT col = 0; col < ChromaSDK::Mouse::MAX_COLUMN; col++)
				{
					Effect.Color[row][col] = colors[index];
				}
			}



			CreateMouseEffect(ChromaSDK::Mouse::CHROMA_CUSTOM2, &Effect, &Play);
			CreateMouseEffect(ChromaSDK::Mouse::CHROMA_NONE, NULL, &Play2);
			SetEffect(Play);
			Sleep(off);
			SetEffect(Play2);
			Sleep(on);
		}
	}
	
}
void CChromaSDKImpl::ShowMouseSpectrumEffect(int time) {
	RZEFFECTID Play = GUID_NULL;
	ChromaSDK::Mouse::CUSTOM_EFFECT_TYPE2 Effect = {};
	COLORREF Color;
	int r = 255;
	int g = 0;
	int b = 0;
	while (true) {
		for (int i = 0; i <= 255; i++) {
			g = i;
			Color = RGB(r, g, b);
			for (UINT row = 0; row<ChromaSDK::Mouse::MAX_ROW; row++)
			{
				for (UINT col = 0; col<ChromaSDK::Mouse::MAX_COLUMN; col++)
				{
					Effect.Color[row][col] = Color;
				}
			}
			CreateMouseEffect(ChromaSDK::Mouse::CHROMA_CUSTOM2, &Effect, NULL);
			Sleep(time);
		}
		for (int i = 254; i >= 0; i--) {
			r = i;
			Color = RGB(r, g, b);
			for (UINT row = 0; row<ChromaSDK::Mouse::MAX_ROW; row++)
			{
				for (UINT col = 0; col<ChromaSDK::Mouse::MAX_COLUMN; col++)
				{
					Effect.Color[row][col] = Color;
				}
			}
			CreateMouseEffect(ChromaSDK::Mouse::CHROMA_CUSTOM2, &Effect, NULL);
			Sleep(time);

		}
		for (int i = 0; i <= 255; i++) {
			b = i;
			Color = RGB(r, g, b);
			for (UINT row = 0; row<ChromaSDK::Mouse::MAX_ROW; row++)
			{
				for (UINT col = 0; col<ChromaSDK::Mouse::MAX_COLUMN; col++)
				{
					Effect.Color[row][col] = Color;
				}
			}
			CreateMouseEffect(ChromaSDK::Mouse::CHROMA_CUSTOM2, &Effect, NULL);
			Sleep(time);
		}
		for (int i = 254; i >= 0; i--) {
			g = i;
			Color = RGB(r, g, b);
			for (UINT row = 0; row<ChromaSDK::Mouse::MAX_ROW; row++)
			{
				for (UINT col = 0; col<ChromaSDK::Mouse::MAX_COLUMN; col++)
				{
					Effect.Color[row][col] = Color;
				}
			}
			CreateMouseEffect(ChromaSDK::Mouse::CHROMA_CUSTOM2, &Effect, NULL);
			Sleep(time);

		}
		for (int i = 0; i <= 255; i++) {
			r = i;
			Color = RGB(r, g, b);
			for (UINT row = 0; row<ChromaSDK::Mouse::MAX_ROW; row++)
			{
				for (UINT col = 0; col<ChromaSDK::Mouse::MAX_COLUMN; col++)
				{
					Effect.Color[row][col] = Color;
				}
			}
			CreateMouseEffect(ChromaSDK::Mouse::CHROMA_CUSTOM2, &Effect, NULL);
			Sleep(time);
		}
		for (int i = 254; i >= 0; i--) {
			b = i;
			Color = RGB(r, g, b);
			for (UINT row = 0; row<ChromaSDK::Mouse::MAX_ROW; row++)
			{
				for (UINT col = 0; col<ChromaSDK::Mouse::MAX_COLUMN; col++)
				{
					Effect.Color[row][col] = Color;
				}
			}
			CreateMouseEffect(ChromaSDK::Mouse::CHROMA_CUSTOM2, &Effect, NULL);
			Sleep(time);

		}

	}
}

//Keyboard Effects
void CChromaSDKImpl::ShowKeyboardWaveEffect(int direction) {
	//directions: 0 - L2R  1 - R2L
	RZEFFECTID Play = GUID_NULL;


	ChromaSDK::Keyboard::WAVE_EFFECT_TYPE Effect1 = {};
	if (direction == 0)
		Effect1.Direction = Keyboard::WAVE_EFFECT_TYPE::DIRECTION_LEFT_TO_RIGHT;
	else if (direction == 1)
		Effect1.Direction = Keyboard::WAVE_EFFECT_TYPE::DIRECTION_RIGHT_TO_LEFT;


	CreateKeyboardEffect(ChromaSDK::Keyboard::CHROMA_WAVE, &Effect1, &Play);

	do {
		Sleep(900); //Sleep first to stop twitch effect
		SetEffect(Play);
	} while (true);

}
void CChromaSDKImpl::ShowKeyboardSpectrumEffect(int time) {
	RZEFFECTID Play = GUID_NULL;


	ChromaSDK::Keyboard::CUSTOM_KEY_EFFECT_TYPE Effect = {};
	COLORREF Color;
	int r = 255;
	int g = 0;
	int b = 0;
	while (true) {
		for (int i = 0; i <= 255; i++) {
			g = i;
			Color = RGB(r, g, b);
			for (UINT row = 0; row<ChromaSDK::Keyboard::MAX_ROW; row++)
			{
				for (UINT col = 0; col<ChromaSDK::Keyboard::MAX_COLUMN; col++)
				{
					Effect.Color[row][col] = Color;
				}
			}
			CreateKeyboardEffect(ChromaSDK::Keyboard::CHROMA_CUSTOM_KEY, &Effect, NULL);
			Sleep(time);
		}
		for (int i = 254; i >= 0; i--) {
			r = i;
			Color = RGB(r, g, b);
			for (UINT row = 0; row<ChromaSDK::Keyboard::MAX_ROW; row++)
			{
				for (UINT col = 0; col<ChromaSDK::Keyboard::MAX_COLUMN; col++)
				{
					Effect.Color[row][col] = Color;
				}
			}
			CreateKeyboardEffect(ChromaSDK::Keyboard::CHROMA_CUSTOM_KEY, &Effect, NULL);
			Sleep(time);

		}
		for (int i = 0; i <= 255; i++) {
			b = i;
			Color = RGB(r, g, b);
			for (UINT row = 0; row<ChromaSDK::Keyboard::MAX_ROW; row++)
			{
				for (UINT col = 0; col<ChromaSDK::Keyboard::MAX_COLUMN; col++)
				{
					Effect.Color[row][col] = Color;
				}
			}
			CreateKeyboardEffect(ChromaSDK::Keyboard::CHROMA_CUSTOM_KEY, &Effect, NULL);
			Sleep(time);
		}
		for (int i = 254; i >= 0; i--) {
			g = i;
			Color = RGB(r, g, b);
			for (UINT row = 0; row<ChromaSDK::Keyboard::MAX_ROW; row++)
			{
				for (UINT col = 0; col<ChromaSDK::Keyboard::MAX_COLUMN; col++)
				{
					Effect.Color[row][col] = Color;
				}
			}
			CreateKeyboardEffect(ChromaSDK::Keyboard::CHROMA_CUSTOM_KEY, &Effect, NULL);
			Sleep(time);

		}
		for (int i = 0; i <= 255; i++) {
			r = i;
			Color = RGB(r, g, b);
			for (UINT row = 0; row<ChromaSDK::Keyboard::MAX_ROW; row++)
			{
				for (UINT col = 0; col<ChromaSDK::Keyboard::MAX_COLUMN; col++)
				{
					Effect.Color[row][col] = Color;
				}
			}
			CreateKeyboardEffect(ChromaSDK::Keyboard::CHROMA_CUSTOM_KEY, &Effect, NULL);
			Sleep(time);
		}
		for (int i = 254; i >= 0; i--) {
			b = i;
			Color = RGB(r, g, b);
			for (UINT row = 0; row<ChromaSDK::Keyboard::MAX_ROW; row++)
			{
				for (UINT col = 0; col<ChromaSDK::Keyboard::MAX_COLUMN; col++)
				{
					Effect.Color[row][col] = Color;
				}
			}
			CreateKeyboardEffect(ChromaSDK::Keyboard::CHROMA_CUSTOM_KEY, &Effect, NULL);
			Sleep(time);

		}

	}



}
void CChromaSDKImpl::ShowKeyboardBreatheEffect(int type, COLORREF colors[]) {
	//Types: type 0 - Two colors; type 1 - Random colors
	RZEFFECTID Play = GUID_NULL;
	RZEFFECTID Play2 = GUID_NULL;


	ChromaSDK::Keyboard::BREATHING_EFFECT_TYPE Effect1 = {};
	if (type == 0)
		Effect1.Type = Keyboard::BREATHING_EFFECT_TYPE::TWO_COLORS;
	else if (type == 1)
		Effect1.Type = Keyboard::BREATHING_EFFECT_TYPE::RANDOM_COLORS;


	Effect1.Color1 = colors[0];
	Effect1.Color2 = colors[1];


	CreateKeyboardEffect(ChromaSDK::Keyboard::CHROMA_BREATHING, &Effect1, &Play);

	Sleep(5000);
	SetEffect(Play);


	do {

		Sleep(15000); //Sleep first to stop twitch effect
		SetEffect(Play);
	} while (true);

}
void CChromaSDKImpl::ShowKeyboardBlinkEffect(int on, int off, COLORREF colors[], int size) {
	//on- time it takes to come on; off - time it takes to come off
	RZEFFECTID Play = GUID_NULL;
	RZEFFECTID Play2 = GUID_NULL;


	ChromaSDK::Keyboard::CUSTOM_KEY_EFFECT_TYPE Effect = {};

	while (true) {
		for (int index = 0; index < size; index++) {
			for (UINT row = 0; row < ChromaSDK::Keyboard::MAX_ROW; row++)
			{
				for (UINT col = 0; col < ChromaSDK::Keyboard::MAX_COLUMN; col++)
				{
					Effect.Color[row][col] = colors[index];
				}
			}



			CreateKeyboardEffect(ChromaSDK::Keyboard::CHROMA_CUSTOM_KEY, &Effect, &Play);
			CreateKeyboardEffect(ChromaSDK::Keyboard::CHROMA_NONE, NULL, &Play2);
			SetEffect(Play);
			Sleep(off);
			SetEffect(Play2);
			Sleep(on);
		}
	}
}
void CChromaSDKImpl::ShowKeyboardReactEffect(COLORREF color, int duration) {
	RZEFFECTID Play = GUID_NULL;

	ChromaSDK::Keyboard::REACTIVE_EFFECT_TYPE Effect = {};
	Effect.Color = color;
	if (duration == 0)
		Effect.Duration = Keyboard::REACTIVE_EFFECT_TYPE::DURATION_SHORT;
	else if (duration == 1)
		Effect.Duration = Keyboard::REACTIVE_EFFECT_TYPE::DURATION_MEDIUM;
	else if (duration == 2)
		Effect.Duration = Keyboard::REACTIVE_EFFECT_TYPE::DURATION_LONG;


	CreateKeyboardEffect(ChromaSDK::Keyboard::CHROMA_REACTIVE, &Effect, &Play);
	Sleep(910);
	SetEffect(Play);
	while (true) {

	}
}
void CChromaSDKImpl::ShowKeyboardStaticEffect(COLORREF color) {
	Keyboard::CUSTOM_KEY_EFFECT_TYPE Effect = {};


	COLORREF Color = color;





	for (UINT row = 0; row < ChromaSDK::Keyboard::MAX_ROW; row++)
	{
		for (UINT col = 0; col < ChromaSDK::Keyboard::MAX_COLUMN; col++)
		{
			Effect.Color[row][col] = Color;
		}
	}




	Sleep(1000);
	CreateKeyboardEffect(Keyboard::CHROMA_CUSTOM_KEY, &Effect, NULL);

	while (true) {

	}
}
void CChromaSDKImpl::ShowKeyboardCustomEffect(COLORREF colors[], int keys[], int size) {
	Keyboard::CUSTOM_KEY_EFFECT_TYPE Effect = {};

	for (int index = 0; index < size; index++)
	{

		Effect.Color[HIBYTE(keys[index])][LOBYTE(keys[index])] = colors[index];

	}


	Sleep(1000);
	CreateKeyboardEffect(Keyboard::CHROMA_CUSTOM_KEY, &Effect, NULL);

	while (true) {

	}
}
void CChromaSDKImpl::ShowKeyboardStarlightEffect(int atATime) {
	//atATime - num of LEDS on
	RZEFFECTID Play = GUID_NULL;


	Sleep(1000);

	while (true) {
		ChromaSDK::Keyboard::CUSTOM_KEY_EFFECT_TYPE Effect1 = {};
		int row;
		int col;
		COLORREF color;
		for (int i = 0; i < atATime; i++) {
			row = rand() % Keyboard::MAX_ROW;
			col = rand() % Keyboard::MAX_COLUMN;
			color = RGB(rand() % 255, rand() % 255, rand() % 255);
			Effect1.Color[row][col] = color;
		}
		CreateKeyboardEffect(Keyboard::CHROMA_CUSTOM_KEY, &Effect1, &Play);
		Sleep(175);
		SetEffect(Play);
	}
}

void setEffectOnSDK(RZEFFECTID effect) {
	SetEffect(effect);
}

BOOL CChromaSDKImpl::IsDeviceConnected(RZDEVICEID DeviceId)
{
	if (QueryDevice != NULL)
	{
		ChromaSDK::DEVICE_INFO_TYPE DeviceInfo = {};
		RZRESULT Result = QueryDevice(DeviceId, DeviceInfo);

		ASSERT(Result == RZRESULT_SUCCESS);

		return DeviceInfo.Connected;
	}

	return FALSE;
}

