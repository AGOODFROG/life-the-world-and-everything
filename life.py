class life:
    def __init__(self, width, length):
        self.grid = []
        self.cellPoscitons = []
        #TODO optimise using a forloop to generatat the inn part of the list and store it

        for i in range(length):
            self.grid.append([])
            for j in range(width):
                self.grid[-1].append([0])
            
       
    def __str__(self):
        #TODO fix bug that prints as an array 
        # TODO add slow mode 
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

        if self.grid[row-1][collnmum] == [1]:out += 1 #checks up

        if self.grid[row+1][collnmum+1] == [1]:out+= 1 # right down

        if self.grid[row-1][collnmum+1] == [1]:out+= 1 # right up

        if self.grid[row+1][collnmum-1] == [1]:out+= 1 # left down

        if self.grid[row-1][collnmum-1] == [1]:out+= 1 # left up

        


        return out
    def addDeadNabor(row, collnum):
        pass 



        





myLife = life(10,10) # tested up to 5000 by 5000 takes a while probly 

myLife.addCell(2,2)
myLife.addCell(2,1)
myLife.addCell(2,3)
myLife.addCell(1,2)
myLife.addCell(3,2)
myLife.addCell(1,1)
myLife.addCell(3,3)
myLife.addCell(1,3)
#myLife.addCell(3,1)


print(myLife) # the litness test for all life on the console!
print(myLife.getNabors([2,2]))
print(myLife.cellPoscitons)


