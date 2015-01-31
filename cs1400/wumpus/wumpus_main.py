from graphics     import *
from wumpus_data  import *
from wumpus_logic import *
from wumpus_draw  import *

# Implement setCellVisible here
def setCellVisible(data, x, y):
    index = 4*y + x
    vList = getVisible(data)
    vList[index] = True
        
# Implement visitCell here

def clickCell(window, data):
    (width, height) = getDimensions(data)
    cell_size = getCellSize(data)
    
    (x, y) = (-1, -1)
    while (x == -1) and (y == -1):
        point = window.getMouse()
        x = int(point.getX()/cell_size)
        y = int(point.getY()/cell_size)
        if not neighborCellIsVisible(data, x, y):
            (x, y) = (-1, -1)

    return (x, y)

def visitCell(data,x,y):
    if cellContainsWumpus(data,x,y) or cellContainsPit(data,x,y):
        setIsAlive(data,False)
    elif cellContainsGold(data,x,y):
        setHaveGold(data,True)
    setCellVisible(data, x, y)

def main():
    CELL_SIZE = 100
    WIDTH     = 4
    HEIGHT    = 4

    window = initializeGraphics(WIDTH, HEIGHT, CELL_SIZE)
    data   = initializeData(WIDTH, HEIGHT, CELL_SIZE, 0)

    (x, y) = (0, 0)
    while getIsAlive(data) and (not getHaveGold(data)):
        updateDisplay(window, data, x, y)
        (x, y) = clickCell(window, data)
        visitCell(data, x,y)

    updateDisplay(window, data, x, y)
    point = window.getMouse()
    window.close()

if __name__ == '__main__':
    main()
    
