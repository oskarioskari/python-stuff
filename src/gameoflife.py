import time
import dis

def countNB(playarea, imin, imax, jmin, jmax, x, y):
    nb = 0
    for i in xrange(imin, imax):
        for j in xrange(jmin, jmax):
                if i != 0 or j != 0:
                    tkey = str(x + i) + '-' + str(y + j)
                    if int(playarea[tkey]) == 2:
                        nb += 1
    return nb

def playRound(playarea, xlim, ylim):
    newarea = dict()
    keylist = playarea.keys()
    for k in keylist:
        nb = 0
        xy = k.split("-")
        x = int(xy[0])
        y = int(xy[1])
        alive = False
        if int(playarea[k]) == 2:
            alive = True
        if x != 0 and x != xlim-1 and y != 0 and y != ylim-1: #not at border
            nb = countNB(playarea, -1, 2, -1, 2, x, y)
        else: #at border
            # Check corners
            if x == 0 and y == 0: #upper-left
                nb = countNB(playarea, 0, 2, 0, 2, x, y)
            elif x == 0 and y == ylim-1: #lower-left
                nb = countNB(playarea, 0, 2, -1, 1, x, y)
            elif x == xlim-1 and y == 0: #upper-right
                nb = countNB(playarea, -1, 1, 0, 2, x, y)
            elif x == xlim-1 and y == ylim-1: #lower-right
                nb = countNB(playarea, -1, 1, -1, 1, x, y)
            elif x == 0: #left border
                nb = countNB(playarea, 0, 2, -1, 2, x, y)
            elif x == xlim-1: #right border
                nb = countNB(playarea, -1, 1, -1, 2, x, y)
            elif y == 0: #upper border
                nb = countNB(playarea, -1, 2, 0, 2, x, y)
            elif y == ylim-1: #lower border
                nb = countNB(playarea, -1, 2, -1, 1, x, y)
        # Check if survives?
        if alive:
            if nb < 2:
                alive = False
            elif nb == 2 or nb == 3:
                alive = True
            else:
                alive = False
        else: # New spawns?
            if nb == 3:
                alive = True
        # Add into next round
        if alive:
            newarea[k] = 2
        else:
            newarea[k] = 1
    return newarea
