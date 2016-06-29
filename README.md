# ImagefapDownloader
This is a Python project that aims to allow users to download images from Imagefap with a single click of a button.

Things to look out for:
-Program will download the images into the folder in which the program is storred... Sorry about that. Might change that later.
-If there are any types of naming conflicts the program will override the files. 
 EG: 
 Let Gallery A contain File named "Alpha.jpg"
 Let Gallery B contain File named "Alpha.jpg" too
 If you run the program raw (Without any code alternations) or you don't relocate the files after downloading Gallery A but before downloading Gallery B, "Alpha.jpg" from Gallery B will override "Alpha.jpg" from Gallery B, resulting in "Alpha.jpg" from Gallery A being lost. (Lost from your PC, not from Imagefap. You can download it again.)
-This program uses the "Eval" statement. I was told that it can be used for corrupting your file data across your whole PC.
 As such, I recommend, if you know python, double check that it's evaluating a string into a dictionary which contains data about the image, and not into some malicious code. Further, I recommend that no one downloads this project from any other place as the uploader could have added some malicious code.

Version 4: (Earlier Versions were not uploaded)
Step 1:
To begin, you need python 3 (Tested with Python 3.4.4)
You can get it at the official website: https://www.python.org/downloads/release/python-344/
Step 2:
Once you install Python 3, simply download and run the file "DownloadTest4.py", prefferably by right clicking on the file and pressing "Edit with IDLE"
A new window will pop up.
Step 3:
At the top of the window, press "Run" and then "Run Module" or alternatively press the "F5" key on your keyboard.
Step 4:
You should be preompted with:
"Enter the Gallery Url:   (Write 'Break' to continue.)"
Under this text paste the Imagefap gallery URL and press enter to submit.
Step 5:
The text "Enter the Gallery Url:   (Write 'Break' to continue.)" will appear once again, giving you the choice to paste another URL. (If you do you're creating a download queue.)
Step 6:
Repeat Step 5 as many times as you wish.
Write "Break" and press enter to submit a command that will continue with the download.

----Warning! Be careful to paste valid urls and to write "Break" with no spelling mistakes or the program might crash!

Step 7:
Enjoy the download.
