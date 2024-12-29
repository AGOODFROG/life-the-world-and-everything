class life:
    def __init__(self, width, length):
        self.grid = []
        self.livingCellPoscitons = []# living cel
        for i in range(width):
            self.livingCellPoscitons[i] = [] 

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
        self.livingCellPoscitons[row].append(column) # appends to a list witch is a value in a dict
    
    # TODO make method that adds a list of cells
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
        if self.grid[row][collnmum+1] == [1]:out += 1 #checks right

        elif self.grid[row][collnmum+1] == [0]: 
            self.addDeadNeibor(row, collnmum+1)
            self.addDeadNeibor(row, collnmum+1)

        if self.grid[row][collnmum-1] == [1]:
            out += 1 # checks left

        elif self.grid[row][collnmum-1] == [0]: 
            self.addDeadNeibor(row, collnmum-1)
            
        if self.grid[row+1][collnmum] == [1]: 
            out += 1 #checks down 

        elif self.grid[row+1][collnmum] == [0]: 
            self.addDeadNeibor(row+1, collnmum)
            
        if self.grid[row-1][collnmum] == [1]:
            out += 1 #check up

        elif self.grid[row-1][collnmum] == [0]: 
            self.addDeadNeibor(row-1, collnmum)
            
        if self.grid[row+1][collnmum+1] == [1]:
            out+= 1 # right down

        elif self.grid[row+1][collnmum+1] == [0]: 
            self.addDeadNeibor(row+1, collnmum+1)
            
        if self.grid[row-1][collnmum+1] == [1]:
            out+= 1 # right up

        elif self.grid[row-1][collnmum+1] == [0]: 
            self.addDeadNeibor(row-1, collnmum+1)
            
        if self.grid[row+1][collnmum-1] == [1]:
            out += 1 # left down

        elif self.grid[row+1][collnmum-1] == [0]: 
            self.addDeadNeibor(row+1, collnmum-1)
            
        if self.grid[row-1][collnmum-1] == [1]:
            out+= 1 # left up

        elif self.grid[row-1][collnmum-1] == [0]: 
            self.addDeadNeibor(row-1, collnmum-1)
            
        print(self.grid[0][0] == [0])

        return out
   
    




        





myLife = life(10,10)

myLife.addCell(2,2)
#myLife.addCell(2,1)
#myLife.addCell(2,3)
#myLife.addCell(1,2)
#myLife.addCell(3,2)


print(myLife) # the litness test for all life on the console!
print(myLife.getNabors([2,2]))
#print(myLife.cellPoscitons)
print(myLife.deadNeighborCells)



