import time
import pyautogui as pg

time.sleep(1)
pg.hotkey('winleft') # Abre el buscador de windows
pg.typewrite('league') # Escribe 'league'
pg.hotkey('enter') # Da enter

time.sleep(6) # Deja un tiempo para que cargue el lol

# pg.click('username')

pg.typewrite('') # <----- colocar username
pg.hotkey('tab') # Cambiar de input username -> password
pg.typewrite('') # <----- colocar password

# pg.hotkey('enter') # también se puede entrar directamente 
# con este comando pero quería probar haciendolo con 
# pyautogui.locateCenterOnScreen() y pyautogui.click()

enter = pg.locateCenterOnScreen("E:\PYTHON VSCODE\workspace\league\login.png")
pg.click(enter)