import pyautogui
import time 
hour=int(input("Enter the hour:"))
minute=int(input("Enter the minute:"))
second=int(input("Enter the second:"))
t=hour*3600+minute*60+second
pyautogui.hotkey("win","d")
time.sleep(t)
def command(n):
    if n=="close":
        pyautogui.hotkey("alt","f4") 
    if n=="shutdown":
        pyautogui.hotkey("win","r")
        pyautogui.typewrite("shutdown /s /t 0")
        pyautogui.press("enter") 
    if n == "minimize":
        pyautogui.hotkey("win","d")
    if n == "copy":
        pyautogui.hotkey("win","d")



n = input("Enter the command:")
ex=command(n)

pyautogui.FAILSAFE=False
time.sleep(14)