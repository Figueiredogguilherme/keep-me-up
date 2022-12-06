import time, pyautogui

print("Mantendo a tela ligada...\nPara desligar, feche o terminal.")

while True:
    pyautogui.press('volumedown')
    time.sleep(1)
    pyautogui.press('volumeup')
    time.sleep(300)
