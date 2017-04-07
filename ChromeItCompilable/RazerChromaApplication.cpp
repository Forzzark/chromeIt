#include "stdafx.h"
// RazerChromaSampleApplication.cpp : Defines the class behaviors for the application.
//



#include "ChromaSDKImpl.h"



#include "resource.h" 
#include <iostream>



using namespace std;


int main() {

	CChromaSDKImpl m_ChromaSDKImpl;
	m_ChromaSDKImpl.Initialize();
	COLORREF colors[] = {RED, BLUE};
	m_ChromaSDKImpl.ShowKeyboardBreatheEffect(1, colors);

	return 0;
}



