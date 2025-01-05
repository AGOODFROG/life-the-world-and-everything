class life:
    def __init__(self, cols, rows):
        #self.next_grid = [] # set to an empty list to avoid wirrd stuff happening
        self.grid =  [[0 for i in range(cols)] for j in range(rows)]
        self.livingCellPoscitons = []# living cel
        self.deadNeighborCells = [] # if a dead cell has three neighbors it is born, no need for dublicates just slows things down 
        
        '''
        for i in range(length):
            self.grid.append([])
            for j in range(width):
                self.grid[-1].append(0)
        '''
      
        
        
            
       
    def __str__(self):
        #TODO fix bug that prints as an array 
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
        self.livingCellPoscitons.append([row, column]) # appends to a list witch is a value in a dict
    
    # make method that adds a list of cells
    def addCellList(self, array):
        for i, j in array:
            self.addCell(i , j)
            
    def addDeadNeibor(self, cell):
        #print(cell)
        self.deadNeighborCells.append(cell)

    # TODO add a method that iterates the game of life
    def iterateGrid(self):
        pass

    

    # TODO get nabors
    def getNabors(self, postion):
        row = postion[0]
        collnmum = postion[1]
        out = 0
        #print(collnmum)
        cell_postions =[[row+1, collnmum+1],[row+1, collnmum],[row-1, collnmum+1],
                        [row, collnmum+1],                      [row, collnmum-1],
                        [row+1, collnmum-1],[row-1, collnmum],[row-1, collnmum-1],]
        for cell in cell_postions:
            #TODO implent add dead neibor
            row = cell[0]
            col = cell[1]
            if self.grid[row][col] == 1:
                out += 1
            else:
                self.addDeadNeibor(cell)
        return out

    # returns cells to kill
    def runDeathLogic(self):
       # get list of living cell to kill
       #print(self.livingCellPoscitons)
        cell_to_kill = []
       # go over each cell that may or may not be killed
        for cell in self.livingCellPoscitons:
            #print(cell, self.getNabors(cell))
            #checks if should live
            if self.getNabors(cell) != 2 and self.getNabors(cell) != 3:
                #store cell so it can be  killed by iterate life
               
                cell_to_kill.append(cell)
                
            
        print("next cell gen:",cell_to_kill)
        return cell_to_kill


       # if cell should live copy to new grid of all dead cells



       # if not do nothing


    
                
myLife = life(10,10)


#myLife.addCell(1,1)
#myLife.addCell(2,2)
#myLife.addCell(2,3)
#myLife.addCell(3,2)
myLife.addCell(3,3)



print(myLife.runDeathLogic())

print("dead nierbors",myLife.deadNeighborCells)

print("final",myLife) # the litness test for all life on the console!
#print(myLife.getNabors([2,2]))
#print(myLife.cellPoscitons)
#print(myLife.deadNeighborCells)



