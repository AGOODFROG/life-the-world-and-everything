class life:
    def __init__(self, width, length):
        self.grid = []
        self.cellPoscitons = []
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
        self.cellPoscitons.append([row,column])
    
    # TODO make method that adds a list of cells
    def addCellList(self, array):
        for i, j in array:
            self.addCell(i , j)

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

        if self.grid[row][collnmum-1] == [1]:out += 1 # checks left

        if self.grid[row+1][collnmum] == [1]: out += 1 #checks down 

        if self.grid[row-1][collnmum] == [1]:out += 1 #check up

        return out



        





myLife = life(10,10)

myLife.addCell(2,2)
myLife.addCell(2,1)
myLife.addCell(2,3)
myLife.addCell(1,2)
#myLife.addCell(3,2)


print(myLife) # the litness test for all life on the console!
print(myLife.getNabors([2,2]))
print(myLife.cellPoscitons)


