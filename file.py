'Mouse and Keyboard Automation in Python'
import pyautogui
import time

print(pyautogui.position())

pyautogui.click(300, 300, duration=3)
pyautogui.hotkey('ctrlleft', 'a')
