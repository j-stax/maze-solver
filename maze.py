from cell import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        y1 = self._y1
        for i in range(self._num_rows):
            row = []
            x1 = self._x1
            for j in range(self._num_cols):
                row.append(Cell(x1, y1, x1 + self._cell_size_x, y1 + self._cell_size_y, self._win))
                x1 += self._cell_size_x
            self._cells.append(row)
            y1 += self._cell_size_y
        
        for i in range(len(self._cells)):
            row = self._cells[i]
            for j in range(len(row)):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        cell = self._cells[i][j]
        cell.draw()
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[self._num_rows-1][self._num_cols-1]
        entrance_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False
        if self._win is None:
            return
        entrance_cell.draw()
        exit_cell.draw()