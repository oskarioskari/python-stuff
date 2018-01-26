# tablehandler uses random and sqlite3
from tablehandler import formatfile
from tablehandler import formatfile_random
from tablehandler import dropTable
# draw uses pygame
from draw import drawWin
# for testing:
#from tablehandler import getRows
#from gameoflife import playRound

# Databasefile
table = "database.db"

# Table limits
# Number of cells (tx * ty)
tx = 100
ty = 100

# Window limits
# wx = width (pixels)
# wy = height (pixels)
wx = 400
wy = 400

# Ask if user wants to use new table
newtable = raw_input("New play area? (Y/N) ")
if (newtable == 'Y'):
    dropTable(table)

# Make new table (new table wont be made if table already exists)
formatfile_random(table,tx,ty)
# Draw window
drawWin(wx,wy,table,tx,ty)
# Program ends
print "Program done"
