import time, pyautogui

print("Mantendo o computador acordado...\nPara desligar, feche o terminal.")

while True:
    pyautogui.press('volumeup')
    time.sleep(1)
    pyautogui.press('volumedown')
    time.sleep(300)