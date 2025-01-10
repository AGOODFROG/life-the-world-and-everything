class life:
    def __init__(self, s):
        self.grid =  [[0 for i in range(s)] for j in range(s)]
        self.livingCellPoscitons = []# living cel
        #TODO fix dubliation in deadNeighorCells
        self.deadNeighborCells = set({}) # if a dead cell has three neighbors it is born, no need for dublicates just slows things down 
        
    def __str__(self):
        #TODO fix bug that prints as an array 
        return self.formatGrid(self.grid)
    # reduant?    
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
        self.livingCellPoscitons.append([row, column]) 
    
    # make method that adds a list of cells
    def addCellList(self, array):
        for i, j in array:
            self.addCell(i , j)
            
    def addDeadNeibor(self, cell):
        #print(cell)
        self.deadNeighborCells.add(cell)

    # TODO add a method that iterates the game of life
    def iterateGrid(self):
        cell_to_kill = self.runDeathLogic()
        for i in cell_to_kill:
            row = i[0]
            collum = i[1]
            self.grid[row][collum] = 0
        cells_to_birth = self.birthLogic()
        for i in cells_to_birth:
            self.addCell

    

    # TODO get nabors
    def getNabors(self, postion, addDeadNeibors = True):
        #TODO store result in varible to avoid exstra loops running
        row = postion[0]
        collnmum = postion[1]
        out = 0
        #print(collnmum)
        cell_postions =[(row+1, collnmum+1),(row+1, collnmum),(row-1, collnmum+1),
                        (row, collnmum+1),                      (row, collnmum-1),
                        (row+1, collnmum-1),(row-1, collnmum),(row-1, collnmum-1),]
        for cell in cell_postions:
            #TODO FIX DUPLATION IN ADDDEADNEIBOR
            row = cell[0]
            col = cell[1]
            if self.grid[row][col] == 1:
                out += 1
            else:
                print(cell)
                self.addDeadNeibor(cell)
        return out

    # returns cells to kill
    #DOSE NOT KILL CELLS
    def runDeathLogic(self):
        cell_to_kill = []
        for cell in self.livingCellPoscitons:
            #checks if should die
            if self.getNabors(cell) != 2 and self.getNabors(cell) != 3:
                #store cell so it can be  killed by iterate life
                cell_to_kill.append(cell)

        return cell_to_kill
    
    def birthLogic(self):
        # keep log of cells to be born
        cells_to_birth = set({}) # no duplication
        # iterate of possible cells to be born
        for i in self.deadNeighborCells:
            if self.getNabors(i, False) == 3: cells_to_birth.append(i)

        #return cells to be born
        print("test:", cells_to_birth)
        return cells_to_birth



    
                
myLife = life(10)



myLife.addCell(2,2)
myLife.addCell(2,3)
myLife.addCell(3,2)
myLife.addCell(3,3)



print(myLife.iterateGrid())

print("dead nierbors",myLife.deadNeighborCells)

print("final",myLife) # the litness test for all life on the console!
#print(myLife.getNabors([2,2]))
#print(myLife.cellPoscitons)
#print(myLife.deadNeighborCells)



