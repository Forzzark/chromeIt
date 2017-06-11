ChromeIt Application:

I. Developers:
Fernando J Ortiz Sacarello
Luis Perez
Jaime Cortes


II. ChromeIt Notes:
2 Applications included:
    A) ChromeItApplication.py - This one is used for the Phase 2 of the Programming Languages Course Project.
                                 This version of ChromeIt includes the translator for ChromeIt Code (lexer, parser and intermediate code); it generates a folder with the C++ files ready for compilation.

    B) ChromeItApplicationWithCComplier.py - This version of ChromeIt Includes everything in version A but additionally attempts to compile the code and create an executable with the Razer Chroma Application
                                NOTE: SINCE THIS IS NOT PART OF THE REQUIREMENTS FOR THE PROJECT, THE VERSION HAS NOT BEEN TESTED TO WORK ON ALL WINDOWS SYSTEMS.
                                      MAINLY USED FOR TESTING IN MANUALLY CONFIGURED SYSTEMS.
                                      IT HAS MANY CONSTRAINTS AND ADDITIONAL REQUIREMENTS. IT'S A WORK IN PROGRESS.



III. REQUIREMENTS AND NOTES:

Version A:
-Python 2.7 must be installed
-ChromeIt Code written in 'ChromeItCode.txt'
-Translated code will be ready in ChromeItCompilable
-Razer Chroma SDK must be installed

Additional Reqs. and notes for Version B:
-Project must be located in C: drive
-Visual Stduio C++ Enterprise or superior version with MFC support Must be Installed
-Razer Chroma SDK must be installed
-Path to folder "tools" of visual studio must be in the system's environment variables
-Output .exe located in ChromeItCompilable folder
-Again, this version is not guaranteed to work.


IV. To execute the ChromeIt Application:
-Make sure requirements in the previous section are met.
-Run ChromeItApplication.py or ChromeItApplicationWithCComplier.py



V. FOLLOWING NOTES ARE NOT OFFICIAL, BUT FOR SOME KIND OF REFERENCE:


Language manuals due next phase but for testing purposes, some example code is found in the current ChromeItCode.txt file

To provide an idea of the code grammar it is written as follows:

<effectID> <effectDevice> <EffectType> <EffectArguments> :: <EffectID> <EffectDuration>
