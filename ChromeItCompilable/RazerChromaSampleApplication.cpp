#include "stdafx.h"
// RazerChromaSampleApplication.cpp : Defines the class behaviors for the application.
//



#include "ChromaSDKImpl.h"



#include "resource.h" 
#include <iostream>



using namespace std;


int main(){

	CChromaSDKImpl m_ChromaSDKImpl;
	m_ChromaSDKImpl.Initialize();
	m_ChromaSDKImpl.ShowKeyboardStaticEffect(RED);

	return 0;
}



