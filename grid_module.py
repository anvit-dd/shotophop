from config import *

class Grid:
    def __init__(self,row,col,width,height,grid_visible,grid_color = WHITE) -> None:
        self.row = row
        self.col = col
        self.width = width
        self.height = height-100
        self.grid_color = grid_color
        self.grid = None
        self.grid_visible = False
        self.cell_width = self.width//self.col
        self.cell_height = self.height//self.row
        self.adj_lis = []

    def make_Grid(self,color):
        """
        Makes a 3-D array of the grid with a given color.
        """
        self.grid = []
        for i in range(self.row):
            self.grid.append([])
            for _ in range(self.col):
                self.grid[i].append(color)
        return self.grid

    def draw_Grid(self):
        """
        Displays the new pixels/cells on the canvas.
        """
        for i,row in enumerate(self.grid):
            for j,cell_color in enumerate(row):
                x = i*self.cell_width
                y = j*self.cell_height
                pygame.draw.rect(screen, cell_color, (x,y, self.cell_width+1,self.cell_height+1))

        if self.grid_visible:
            for i in range(self.row+1):
                pygame.draw.line(screen,[200,200,200],(0,(i*self.cell_width)),(self.width+100,(i*self.cell_height)))
            for j in range(self.col+1):
                pygame.draw.line(screen,[200,200,200],((j*self.cell_width),0),((j*self.cell_height),self.height))
        pygame.display.update()

    def make_menu_panel(self):
        """
        Displays the menu panel.
        """
        pygame.draw.rect(screen,menu_color,(0,600,600,100))
        pygame.display.update()

    def get_adj(self,x,y,brushcolor,thickness):

        if thickness>1:
            x = x- (thickness-1)
            y = y - 1*(thickness-1)
            for i in range(thickness+1):
                for j in range(thickness+1):
                    if 0<=x+i<self.col and 0<=y+j<self.row:
                        self.grid[x+i][y+j] = brushcolor

        else:
            self.grid[x][y] = brushcolor
    
    def refresh_cells(self):
        """
        Reassigns cell width and cell height usng new rows and columns.
        """
        self.cell_width = self.width//self.col
        self.cell_height = self.height//self.row
    
    def make_grid_using_another_grid(self,tempgrid):
        """
        Constructs the canvas again given another grid as a param.
        """
        self.grid = []
        for i in range(self.row):
            self.grid.append([])
            for j in range(self.col):
                self.grid[i].append(tempgrid[i][j])