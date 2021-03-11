import pyautogui as pg
from time import sleep

loc = pg.locateOnScreen("images/locrefine.png")
print(str(loc[0]) + "x " + str(loc[1]) + "y")
x = 314 + loc[0]
y = 392 + loc[1]
pg.moveTo(x,y)


