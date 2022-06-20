

PROGTIMER README:

ProgTimer is a program which serves the purpose of timing how long you can use a Single application. How it works is by the user choosing a program 
that they wish to time their usage for, this is done by clicking the "Choose program" button and navigating through the FileMenu to find the .exe file for the Application that they want to time their usage for. 
The user can enter the duration of  the timer into the text entry box. NOTE: THE TIMER IS IN MINUTES. So the number entered in the Textbox is the number of minutes you can use the Application before it is remotely stopped by Progtimer.
For example: If i wanted to limit my usage of Chrome to one hour, so that i do not waste too much time watching youtube, i enter 60 into the Entry box, press the confirm timer button. Then i find the chrome.exe by clicking on the Select program button and then press the Start timer button. 
Now the Progress bar on the GUI will increase as time goes on until it reaches 60 minutes when it will be filled green indicating that it has been 60 minutes, then the Application will close.


If you are having any trouble, you can open the "Options" Menubar and there will be an item titled Help: Which when chosen will display messages that will help the user use the Program.






Blocker Mode README:

Blocker Mode is a Program which allows the user to block Certain Programs, add them to a Blocklist, where until Blocker Mode is closed, the user cannot access these Applications. Unlike progTimer, you can add several Applications at once, the blocking stops once Blocker Mode is closed. 

HOW IT WORKS: 

You open blocker mode by going to the "Options" Menubar in PROGTIMER and select the first option in the Menu, that is "Switch to Blocker Mode". This will then open a New window and close the existing one, and you will now be in Blocker Mode. 
Then you press the "Choose Applications Button" and add all the Applications that you want. Then after having chosen all the Applications that you want disable, you press the cancel button in the Filemenu to go back to the GUI Window and then press the Start button. 


Whenever you try to open any of the applications that you have selected to disable whilst blockmode is still open, the process will be Automatically killed. 
You can end the Blocker Mode by simply closing the program. 

The program resets every time you close it, therefore you have to manually add the Program to the blocker each time you re-open it, but this also means that the reset allows the user to never have to remember what they added to the blocker. 

The design isn't the greatest, i know there are better ways to implement the block list, like writing the filelist array to a Text file that way it hard saves and remembers the users input.
-FarengarsAnvil