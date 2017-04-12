#include "stdafx.h"
// RazerChromaSampleApplication.cpp : Defines the class behaviors for the application.
#include "ChromaSDKImpl.h"
#include "resource.h"
#include <iostream>
#include <thread>

using namespace std;

CChromaSDKImpl m_ChromaSDKImpl;
long kbStart = 0;
long mouseStart = 0; 
	void mouse(){
			
			
	COLORREF e2Colors[] =  {RED,BLUE};
			
			
	COLORREF e4Colors[] =  {RED,BLUE,YELLOW}; 
	
	int e4Zones[] =  {ChromaSDK::Mouse::RZLED2_SCROLLWHEEL,ChromaSDK::Mouse::RZLED2_LOGO,ChromaSDK::Mouse::RZLED2_BACKLIGHT};
		while(true){
		mouseStart = clock();
		while(clock() - mouseStart < 5000){
			m_ChromaSDKImpl.ShowMouseSpectrumEffect(1);
		}
		mouseStart = clock();
		while(clock() - mouseStart < 5000){
			
	m_ChromaSDKImpl.ShowMouseBlinkEffect(200,200,e2Colors,2);
		}
		mouseStart = clock();
		while(clock() - mouseStart < 5000){
			m_ChromaSDKImpl.ShowMouseStaticEffect(RED);
		}
		mouseStart = clock();
		while(clock() - mouseStart < 5000){
			
	m_ChromaSDKImpl.ShowMouseCustomEffect(e4Colors,e4Zones,3);
		}
		}
	}
	void keyboard(){
			
			
	COLORREF e6Colors[] =  {RED,BLUE};
			
			
	COLORREF e8Colors[] =  {RED,BLUE,YELLOW}; 
	
	int e8Keys[] =  {ChromaSDK::Keyboard::RZKEY_V,ChromaSDK::Keyboard::RZKEY_ENTER,ChromaSDK::Keyboard::RZKEY_H};
			
			
	COLORREF e10Colors[] =  { NULL};
			
			
		while(true){
		kbStart = clock();
		while(clock() - kbStart < 5000){
			m_ChromaSDKImpl.ShowKeyboardSpectrumEffect(1);
		}
		kbStart = clock();
		while(clock() - kbStart < 5000){
			
	m_ChromaSDKImpl.ShowKeyboardBlinkEffect(200,200,e6Colors,2);
		}
		kbStart = clock();
		while(clock() - kbStart < 5000){
			m_ChromaSDKImpl.ShowKeyboardStaticEffect(RED);
		}
		kbStart = clock();
		while(clock() - kbStart < 5000){
			
	m_ChromaSDKImpl.ShowKeyboardCustomEffect(e8Colors,e8Keys,3);
		}
		kbStart = clock();
		while(clock() - kbStart < 5000){
			m_ChromaSDKImpl.ShowKeyboardWaveEffect(ChromaSDK::Keyboard::WAVE_EFFECT_TYPE::DIRECTION_LEFT_TO_RIGHT);
		}
		kbStart = clock();
		while(clock() - kbStart < 5000){
			
	m_ChromaSDKImpl.ShowKeyboardBreatheEffect(1,e10Colors);
		}
		kbStart = clock();
		while(clock() - kbStart < 5000){
			
	m_ChromaSDKImpl.ShowKeyboardReactEffect(RED,0);
		}
		kbStart = clock();
		while(clock() - kbStart < 5000){
			m_ChromaSDKImpl.ShowKeyboardStarlightEffect(10, RED);
		}
		}
	}
	int main() {
		m_ChromaSDKImpl.Initialize();
		Sleep(2000);
		thread t1(mouse);
		thread t2(keyboard);
		t1.join();
		t2.join();
		return 0;
	}