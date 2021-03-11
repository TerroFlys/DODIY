import pyautogui as pg
import sys
from time import sleep
from math import floor

#EXPERIMENTAL

pg.PAUSE = 0.5
locpos = pg.locateOnScreen('images/loc.png')
refpos = pg.locateOnScreen('images/locrefine.png')
if locpos == None or refpos == None:
    pg.alert("Please open the skylab on the backpage.\nAlso open the updates in the game window.")
    sys.exit()
locX = locpos[0]
locY = locpos[1]
refX = refpos[0]
refY = refpos[1]
print("locpos: " + str(locY) + "X" + ", " + str(locY) + "Y")
print("refpos: " + str(refX) + "X" + ", " + str(refY) + "Y")
#DO NOT TOUCH
#START
TransportX = 195 + locX
TransportY = 625 + locY
PromX = 478 + locX
PromY = 560 + locY
InstSendX = 586 + locX
InstSendY = 502 + locY
ConfX = 452 + locX
ConfY = 396 + locY
SendedX = 497 + locX
SendedY = 414 + locY
ShipPromX = 225 + refX
ShipPromY = 321 + refY
ShipLaserX = 44 + refX
ShipLaserY = 442 + refY
ShipOptX = 345 + refX
ShipOptY = 280 + refY
OptDownX = 362 + refX
OptDownY = 380 + refY
LowOptX = 314 + refX
LowOptY = 394 + refY
UpgradeX = 275 + refX
UpgradeY =  317 + refY
#END

amountA = 7954 #Amount to send #7954
amountB = 50000 #Amount left
count = floor(amountB / amountA) 
sleep(2)
while count > 0:
    pg.click(TransportX, TransportY)
    sleep(0.2)
    pg.click(PromX, PromY)
    pg.hotkey('ctrl', 'a')
    pg.typewrite(str(amountA))
    sleep(0.2)
    pg.click(InstSendX, InstSendY)
    sleep(1)
    pg.click(ConfX, ConfY)
    sleep(4.5)
    pg.click(SendedX, SendedY)
    pg.moveTo(ShipPromX, ShipPromY, 0.2)
    pg.dragTo(ShipLaserX, ShipLaserY, 0.5)
    sleep(0.7)
    pg.click(ShipOptX, ShipOptY)
    pg.click(OptDownX, OptDownY)
    pg.click(LowOptX, LowOptY)
    pg.click(UpgradeX, UpgradeY)    
    count -= 1


