class life:
    def __init__(self, width, length):
        self.grid = []
        self.next_grid = self.grid
        self.livingCellPoscitons = []# living cel
        self.deadNeighborCells = [] # if a dead cell has three neighbors it is born
        for i in range(length):
            self.grid.append([])
            for j in range(width):
                self.grid[-1].append([0])
            
       
    def __str__(self):
        #TODO fix bug that prints as an array 
        out = ""
        for i in range(len(self.grid)):
            out += "\n"
            for j in range(len(self.grid)):
                val = self.grid[i][j]
                out += f"{val} "    
        return out
    """
    addCell is only for adding a single cells and 

    works by inputing a the row and column of the new cell
    """
    def addCell(self, row, column):
        self.grid[row][column] = [1]
        self.livingCellPoscitons.append([row, column]) # appends to a list witch is a value in a dict
    
    # make method that adds a list of cells
    def addCellList(self, array):
        for i, j in array:
            self.addCell(i , j)
            
    def addDeadNeibor(self,row, collum):
        self.deadNeighborCells.append([row, collum])

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
                        [row, collnmum+1],                    [row, collnmum-1],
                        [row+1, collnmum-1],[row-1, collnmum],[row-1, collnmum-1],]
        for cell in cell_postions:
            #TODO REFATOR
            r = cell[0]
            c = cell[1]
            if self.grid[r][c] == [0]:
                out += 1
        return out
    def runDeathLogic(self):
        next_cell_gen = []
        for cell in self.livingCellPoscitons: 
            if not(self.getNabors(cell) > 3 or self.getNabors(cell) < 2): # chekcing if overpopulated or isolated
                next_cell_gen.append(cell)
                
            else:
                self.remove_cell_from_grid(cell)
        self.livingCellPoscitons = next_cell_gen
        self.grid = self.next_grid
        print(next_cell_gen)


    def remove_cell_from_grid(self, cell):
        row = cell[0]
        collum = cell[1]
        print(self.grid[row][collum], row, collum)
       
        self.next_grid[row][collum] = [0]
                
               
                



       

myLife = life(10,10)

#myLife.addCell(0,0)
myLife.addCell(1,1)
#myLife.addCell(2,2)

print(myLife.getNabors([1,1]))

print(myLife)
myLife.runDeathLogic()



#print(myLife) # the litness test for all life on the console!
#print(myLife.getNabors([2,2]))
#print(myLife.cellPoscitons)
#print(myLife.deadNeighborCells)



