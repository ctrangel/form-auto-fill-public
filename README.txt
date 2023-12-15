
Welcome to my little form auto filler for the scholarship page, 
I took the time to write this because I do not want to take the time to repeatedly fill out the same information
for each application over and over again. I did that last year like twenty times and did not hear back from any of them.

For any PPU students who want to use this as well feel free to download the file, here are the instructions:

1. Download the file
2. Open the file in vscode

you'll need to install python first if you don't have it already, here is a link to the download page: https://www.python.org/downloads/
or you can use the command line to install it, follow the instructions for your operating system here: https://realpython.com/installing-python/

3. Open the terminal in vscode and type in the following command:

```pip install selenium```

4. go into the form_script.py file and replace the webdriver path with the path to your webdriver, Here we are using the chrome webdrivers, which are 
included in the repo, locate your operating system, locate the chromedriver.exe file and copy the path to it, then paste it into the webdriver path variable.

5. *important* if you path has any backslashes in it, you need to replace them with forward slashes, otherwise it will not work because python is mean

6. next go down to the inputs and replace the arguments with your info respectively, make sure to keep the quotes around the arguments

7. run the script by typing in the following command in the terminal:

```python form_script.py```

8. it should pull up a little chrome window and fill out the form for you, if it does not, check the terminal for any errors. 

9. hopefully all goes well, and everything fills out nicely, if not, feel free to reach out to me and I will try to help can try and help cause I've already 
dealt with most of the bs making this thing work. I tested it out myself a bunch of times and it worked for me, but I can't guarantee it will work for you. no promises.

10. Once it is filled, make sure everything is correct, choose the correct scholarship, and submit it.

11. then go back to the terminal and press enter to close the window and script, then repeat the process for as many scholarships as you want to apply for.

* Oh ya, for right now this is only built for chrome, so make sure you have chrome installed.