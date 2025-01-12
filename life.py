import time
class life:
    def __init__(self, size):
        self.grid =  [[0 for i in range(size)] for j in range(size)]
        self.livingCellPoscitons = set()
        
        
        self.deadNeighborCells = set() # if a dead cell has three neighbors it is born, no need for dublicates just slows things down 
        
    def __str__(self):
        return self.formatGrid(self.grid)
    
    def formatGrid(self, grid):
         out = ""
         for i in range(len(grid)):
            out += "\n"
            for j in range(len(grid)):
                val = grid[i][j]
                if val == 1:
                    out += "[#]" 
                else:
                    out += "[ ]" 
         return out
        
    """
    addCell is only for adding a single cells and 

    works by inputing a the row and column of the new cell
    """
    def addCell(self, row, column):
        self.grid[row][column] = 1
        self.livingCellPoscitons.add((row, column)) 
    
    # make method that adds a list of cells
    def addCellList(self, array):
        for i, j in array:
            self.addCell(i , j)
            
    def addDeadNeibor(self, cell):
        self.deadNeighborCells.add(cell)

    # TODO add a method that iterates the game of life
    def iterateGrid(self):
        while True:
            time.sleep(0.5)
            print("",myLife)# the litness test for all life on the console!
            
            
            self.storeDeadNeigors()
            
            cell_to_kill = self.runDeathLogic()
            cells_to_birth = self.birthLogic()

            for cell in cell_to_kill:  
                row = cell[0]
                collum = cell[1]
                self.grid[row][collum] = 0
            cell_to_kill.clear()

            for cell in cells_to_birth:
                row = cell[0]
                col = cell[1]
                self.addCell(row, col)
            cells_to_birth.clear()


    # TODO get nabors
    def getNabors(self, postion, addDeadNeibors = False):
        #TODO store result in varible to avoid exstra loops running
        row = postion[0]
        collnmum = postion[1]
        out = 0
        cell_postions =[(row+1, collnmum+1),(row+1, collnmum),(row-1, collnmum+1),
                        (row, collnmum+1),                      (row, collnmum-1),
                        (row+1, collnmum-1),(row-1, collnmum),(row-1, collnmum-1),]
        for cell in cell_postions:
            #TODO FIX DUPLATION IN ADDDEADNEIBOR
            row = cell[0]
            col = cell[1]
            if self.grid[row][col] == 1:
                out += 1
            elif addDeadNeibors:
                self.addDeadNeibor(cell)
        return out

    # returns cells to kill
    #DOSE NOT KILL CELLS
    def runDeathLogic(self):
        cell_to_kill = set({})
        for cell in self.livingCellPoscitons:
            #checks if should die
            if self.getNabors(cell) != 2 and self.getNabors(cell) != 3:
                cell_to_kill.add(cell)

        return cell_to_kill
    
    def birthLogic(self):
        cells_to_birth = set({}) # no duplication
        # deadNeighors are cells that may or may not be
        for i in self.deadNeighborCells:
            if self.getNabors(i) == 3: cells_to_birth.add(i)

        #return cells to be born
        
        return cells_to_birth
    def storeDeadNeigors(self):
        for cell in self.livingCellPoscitons:
            self.getNabors(cell, True)# get DeadNeigors


myLife = life(10)

myLife.addCell(2,2)
myLife.addCell(3,3)
myLife.addCell(4,1)
myLife.addCell(4,3)
myLife.addCell(4,2)

#for i in range(10): myLife.iterateGrid()

myLife.iterateGrid()


