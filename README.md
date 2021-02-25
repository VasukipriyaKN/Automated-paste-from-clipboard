# Automated-paste-from-clipboard
It's helpful, where copy and paste option is disabled in some websites.
It's also helps while makeing notes from online.
You can make it even more advance by giving the path of text editing file so that it automatically paste everything you copy somewhere, which can be run in background.


Run the followings in the Command Prompt:
1. pip install pyautogui
2. pip install pyperclip

Working: 
1. Run the python script. It will run in background.
2. You need to copy the desired text.
    2.1. If copying option is blocked, use the below chrome extensions.
    2.2. https://chrome.google.com/webstore/detail/enable-right-click-for-go/ofgdcdohlhjfdhbnfkikfeakhpojhpgm?hl=en
3. Once you copied the text move to desired window (within 5 sec), where you want to paste the copied text.
    3.1. You can change the time between the copy and paste at the line 18.
4. When you moved into another window, keep the cursor at the desired place.
5. Wait for 5 sec, it will automatically paste.

You can download and watch the video HTTPS://github.com/VasukipriyaKN/Automated-paste-from-clipboard/blob/main/Video.mp4
