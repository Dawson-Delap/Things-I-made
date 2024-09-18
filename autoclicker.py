import pyautogui
import keyboard
pressed=0
while True:
    if keyboard.is_pressed("`") == True:
        pyautogui.click() 
