import json
import numpy as np
from PIL import Image
from grid_module import *
from savefile import *


class Paint(Grid):
    def __init__(self, row, col, width, height, brush_color) -> None:
        super().__init__(row, col, width, height, False)
        self.brush_color = brush_color
        self.thickness = 1
        self.is_Fill = False
        self.isSaved = False
        self.isPicked = False
        self.undo_stack = []

    def draw_pixel(self, brush_color, pos: tuple):
        """
        This method checks for the following conditions when mouse is clicked with the given params
        ``self.brush_color`` and ``pos`` of the cursor:\n -> If the mouse is not in the canvas region it will raise
        an exception.\n -> Otherwise, check if Fill or Pick tool are true.\n -> Else draw pixel on the canvas.
        :param brush_color:
        :param pos:
        """
        x, y = pos

        row, col = self.set_row_col(x, y)

        if row >= self.row or col >= self.col:
            raise IndexError
        else:

            if self.is_Fill:
                self.fill(col, row, brush_color, self.grid[col][row])

            elif self.isPicked:
                self.set_color(self.grid[col][row])
                self.current_color_display(self.brush_color)

            else:
                self.get_adj(col, row, self.brush_color, self.thickness)

            self.draw_Grid()
            self.isSaved = False

    def set_row_col(self, x, y):
        return y // self.cell_width, x // self.cell_height

    def set_color(self, color=WHITE):
        """
        Sets the color of the brush
        :param color:
        """
        self.brush_color = color

    def reset_canvas(self):
        """
        Resets all the pixels to White(255,255,255).
        """
        self.make_Grid(WHITE)
        self.draw_Grid()
        pygame.display.update()

    def fill(self, fill_col, fill_row, brushcolor, selected_color):
        """
        Fills an area of similar pixels with the current brush color.
        :param fill_col:
        :param fill_row:
        :param brushcolor:
        :param selected_color:
        """
        if not np.array_equal(brushcolor, selected_color):
            fill_stack = [(fill_col, fill_row)]
            while fill_stack:
                i, j = fill_stack.pop()
                if 0 <= i < self.col and 0 <= j < self.row and np.array_equal(self.grid[i][j], selected_color) is True:
                    self.grid[i][j] = brushcolor

                    fill_stack.extend(
                        [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])  # Adds neighboring cells to stack

    def image_save(self):
        """
        Saves the current image on the canvas(Default file format is *.shp).
        """
        file = save_image()
        if len(file):
            if file.endswith(".shp"):
                with open(file, 'w') as f:
                    json.dump(self.grid, f)
                caption = file.split("/")[-1]
                pygame.display.set_caption(f'{caption} | ShotoPhop  | {canvas_dim} x {canvas_dim} px')
            elif file.endswith(file[file.index("."):]):
                pixels = np.array(self.grid)
                surf = pygame.surfarray.make_surface(pixels)
                pygame.image.save(surf, file)
            self.isSaved = True

    def image_open(self):
        """
        Opens the selected image on the canvas.
        """
        file = open_image()
        caption = file.split("/")[-1]
        if file.endswith(".shp"):
            with open(file, 'r') as f:
                self.reset_canvas()
                temp_grid = json.load(f)
                self.row = self.col = 200 if len(temp_grid) > 200 else len(temp_grid)
                self.refresh_cells()
                self.make_grid_using_another_grid(temp_grid)
                self.draw_Grid()
        elif file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".jpg"):

            png_image = Image.open(file).convert("RGB")
            if png_image.size[0] > 200:
                png_image = png_image.resize((200, 200))
            png_image_array = np.asarray(png_image)
            png_image_array = np.transpose(png_image_array, (1, 0, 2))
            self.row = self.col = len(png_image_array)
            self.refresh_cells()
            self.grid = png_image_array
            self.make_grid_using_another_grid(self.grid)
            self.draw_Grid()

        pygame.display.set_caption(f'{caption} | ShotoPhop  | {self.row} x {self.col} px')

    def mouse_coords(self, row, col):
        """
        Displays the current mouse coords(row,col).
        :param row:
        :param col:
        """
        pygame.draw.rect(screen, [40, 40, 40], (520, 605, 590, 50))
        cursor_row = row // self.cell_width
        cursor_col = col // self.cell_height
        if cursor_row < self.row and cursor_col < self.col:
            font = pygame.font.Font(None, 25)
            x_coord = font.render(f"X: {cursor_col},", True, WHITE)
            y_coord = font.render(f"Y: {cursor_row}", True, WHITE)
            screen.blit(x_coord, (530, 610))
            screen.blit(y_coord, (530, 630))
            pygame.display.update()

    def black_white(self):
        """
        This method converts color images into greyscale by taking the average of the RGB values.
        """

        for row in range(self.row):
            for column in range(self.col):
                avg = (self.grid[row][column][0] + self.grid[row][column][1] + self.grid[row][column][2]) // 3
                self.grid[row][column] = (avg, avg, avg)

        self.make_grid_using_another_grid(self.grid)
        self.draw_Grid()

    def invert_image(self):
        """
        Inverts pixels of the canvas(255-RBG).
        """
        for row in range(self.row):
            for column in range(self.col):
                self.grid[row][column] = (
                    255 - self.grid[row][column][0], 255 - self.grid[row][column][1], 255 - self.grid[row][column][2])

        self.make_grid_using_another_grid(self.grid)
        self.draw_Grid()

    def color_pick(self):
        """
        Picks the colors from the canvas.
        """
        self.isPicked = True

    @staticmethod
    def current_color_display(current_color=WHITE):
        """
        This method displays the current brush color.
        :param current_color:
        """
        pygame.draw.rect(screen, current_color, (530, 660, 30, 30), 0)
        pygame.display.update()
