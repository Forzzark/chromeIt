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
			
	COLORREF e5Colors[] =  {RED};
		while(true){
		kbStart = clock();
		while(clock() - kbStart < 1000){
			
	m_ChromaSDKImpl.ShowKeyboardBlinkEffect(50,50,e5Colors,1);
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