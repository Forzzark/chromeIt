# Introduction

## About Razer Chroma
Razer is a company based in San Diego, California that has the mission to create the best products for the gaming industry. One of the most prestigious products from Razer are their peripherals. Ranging from  headphones, keyboards and mice, they have a huge product base which many believe are the top of the line of its category. One of its most reputable line of products is their Razer ChromaTM brand which consists of peripherals with fully customizable RGB LED lighting. Razer has various methods of customizing your device’s lights including a GUI profile creator and an SDK to integrate the Chroma features with your own software.

## Why should I ChromeIt!?
Razer Chroma SDK is developed for C/C++/C# which for some programmers and people with limited programming knowledge can be extremely tedious. The goal of creating a programming language like ChromIt is making the ChromaTM integration very easy for individuals who are not familiar with the previously mentioned languages. With easy syntax you can still create profiles using code rather than the GUI, without the need to struggle learning a complex language like C/C++/C#.

# About the Language

## Language Features

The purpose of the ChromeIt language is to bring simplicity to its users in order to achieve the results they want within the Chroma ecosystem. This is achieved with the inclusion of some key features to shorten the bridge between implementation and execution. Such language features include: 
 
* Translate simple grammar to complex C++/C/C# code to work with Chroma SDK
* Create a custom chroma animation profile
* Profiles usable for Razer Blackwidow Chroma and Razer Deathadder Chroma


## Approach

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/83798954@N06/34883137920/in/dateposted-public/" title="Untitled Diagram"><img src="https://c1.staticflickr.com/5/4288/34883137920_573a0c17e7_b.jpg" width="841" height="321" alt="Untitled Diagram"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
##### The ChromeIt! Architecture works the following way:


1. First the User writes code in the ChromeIt Language.
2. Following, when the user runs the ChromeIt translator which reads the ChromeIt Code and is sent to the PLY Lexer whcih tokenizes the code and then to the PLY parser which parses it.
3. After all data has been obtained from the code, it is sent to the Python intermediate code which categorizes and translates it into C/C++ source code.
4. The C/C++ code creates the effects and playlists making use of the C/C++ intermediate code and Razer's ChromaSDK.
5. After this code is ready, it is ready to be compiled using a C/C++ compiler with MFC support (Visual C++ recommended)
6. The generated ChromeIt Application can be executed to play the effects on Chroma Enabled devices


# Learning ChromeIt!

## Video Tutorial
Following is a video tutorial on how to install and use the ChromeIt! translator. (Click the image below)
[![ChromeIt!](http://img.youtube.com/vi/SGVZe83Ewiw/0.jpg)](http://www.youtube.com/watch?v=SGVZe83Ewiw)

## Language tutorial

Click [here](https://github.com/Forzzark/chromeIt/wiki/Language-Tutorial) to go to the Language Tutorial.

## Reference Manual

Click [here](https://github.com/Forzzark/chromeIt/wiki/Reference-Manual) to go to the Reference Manual.


# Contributors

* [Fernando J. Ortiz Sacarello](https://github.com/Forzzark)
* [Luis R. Pérez Pagán](https://github.com/luisroperez)
* [Jaime A. Cortés Cortés](https://github.com/jcdfusion)

