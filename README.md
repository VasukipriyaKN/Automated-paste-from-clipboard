# Automated-paste-from-clipboard
Run the followings in the Command Prompt:
1. pip install pyautogui
2. pip install pyperclip

Working: 
1. You need to copy the desired text.
    1.1. If copying option is blocked, use the below chrome extensions.
    1.2. https://chrome.google.com/webstore/detail/enable-right-click-for-go/ofgdcdohlhjfdhbnfkikfeakhpojhpgm?hl=en
2. Once you copied the text move to desired window (within 5 sec), where you want to paste the copied text.
    2.1. You can change the time between the copy and paste at the line 18.
3. When you moved into another window, keep the cursor at the desired place.
4. Wait for 5 sec, it will automatically paste.

