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
		while(true){
		}
	}
	void keyboard(){
			
	COLORREF e5Colors[] =  {RED,RED}; 
	
	int e5Zones[] =  {ChromaSDK::Keyboard::RZKEY_ENTER,ChromaSDK::Keyboard::RZKEY_ESC};
		while(true){
		kbStart = clock();
		while(clock() - kbStart < 1000){
			
	m_ChromaSDKImpl.ShowKeyboardCustomEffect(e5Colors,e5Keys,2);
		}
		}
	}
	int main() {
		CChromaSDKImpl m_ChromaSDKImpl;
		m_ChromaSDKImpl.Initialize();
		Sleep(2000);
		thread t1(mouse);
		thread t2(keyboard);
		t1.join();
		t2.join();
		return 0;
	}