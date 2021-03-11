import pyautogui as pg

def getP():
    pos = pg.position()
    pg.alert(str(pos))
    return
def conP():
    count = 0
    cmax = 20000
    #while count < cmax:
    while True:
        print(pg.position())
        count += 1


conP()
    

