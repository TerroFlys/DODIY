import pyautogui as pg
from time import sleep


count = 0
my = 200
mx = 400


cmax = 5 #amount of times to craft
b = 30 #Do not change, Amount to craft one ImmunizerCpu

cmaxs = pg.prompt('Enter how many alloy do you want to use.')
cmax = int(cmaxs)
cmax = int(cmaxs) / b #total to craft
cmax = int(cmax)
pg.alert("When you press OK the program will start in 3 seconds.\nUse ctrl+c in the terminal to terminate the program\nThe program will use: " + str(int(cmaxs)) + " H-Alloy to craft: " + str(cmax) + " CPU\'s")
sleep(3)
def ImmunizerCpuClicker():
    pg.moveTo(100,0)
    alloyloc = pg.locateOnScreen('images/alloy.png')
    if alloyloc == None:
        pg.alert("Open the assembly.\nSelect the Immunizer CPU")
        return
    else:
        buildloc = pg.locateOnScreen('images/build.png')
        collectloc = pg.locateOnScreen('images/collect.png')
        if buildloc == None and collectloc == None:
            print("cannot find now waiting 5 seconds")
            sleep(5)
            return
        elif buildloc != None and collectloc == None:
            pg.click(buildloc[0], buildloc[1])
            print("Clicked build")
            pg.moveRel(mx,my)
            print("Moved mouse\nStarting sleep for 6.5 seconds")
            sleep(6.5)
            print("sleep over")
            collectloc = pg.locateOnScreen('images/collect.png')
            print("Collect Loc: " + str(collectloc))
            pg.click(collectloc[0], collectloc[1])
            print("Clicked collect")
            pg.moveRel(mx,my)
            print("moved mouse")
            return
        elif buildloc == None and collectloc != None:
            pg.click(collectloc[0], collectloc[1])
            print("Clicked collect")
            pg.moveRel(mx,my)
            print("Moved mouse")
            return
        else:
            print('AAAAAAAAAAAAAAAA')
            return
    return



while count < cmax:
    print("crafting loop: " + str(count) + " from " + str(cmax) + "...")
    sleep(0.2)
    print("starting")
    ImmunizerCpuClicker()
    count += 1


