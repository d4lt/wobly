import pygame

class Cell:
    def __init__(self, win, force, row, col, gap):
        self.win = win
        self.force = force
        self.row = row
        self.col = col
        self.gap = gap

        self.color = (force, force, force)

        self.x = self.col // self.gap
        self.y = self.row // self.gap

    def draw(self):
        pygame.draw.rect(self.win, self.color, pygame.Rect(self.x, self.y, self.gap, self.gap))


    def make_force(self, force):
        self.force = force


class Grid:

    def __init__(self, win, rows):
        self.win = win
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.rows = rows
        self.gap = self.height // self.rows
        self.collums = self.width // self.gap

    def make_grid(self):
        grid = []

        for row in range(self.rows):
            grid.append( [] )
            for col in range(self.collums):
                new_cell = Cell(self.win, 0, row, col, self.gap)
                grid[row].append(new_cell)

        return grid

    def draw_grid(self):
        GREY = (100, 100, 100)
        for row in range(self.rows):
            pygame.draw.line(self.win, GREY, (self.gap * row, 0) , (self.gap * row, self.height))

        for collum in range(self.collums):
            pygame.draw.line(self.win, GREY, (0, self.gap * collum) , (self.width, self.gap * collum))

    def draw(self, grid):

        for row in grid:
            for cell in row:
                cell.draw()

        self.draw_grid()
        pygame.display.update()
