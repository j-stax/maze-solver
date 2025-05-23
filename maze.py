from cell import Cell
import time
import random

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
        seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        

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

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if j > 0 and not self._cells[i][j-1].visited:
                next_index_list.append((i, j-1))
            # right
            if j < self._num_cols - 1 and not self._cells[i][j+1].visited:
                next_index_list.append((i, j+1))
            # up
            if i > 0 and not self._cells[i-1][j].visited:
                next_index_list.append((i-1, j))
            # down
            if i < self._num_rows - 1 and not self._cells[i+1][j].visited:
                next_index_list.append((i+1, j))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[1] == j + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i][j+1].has_left_wall = False
            # left
            if next_index[1] == j - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i][j-1].has_right_wall = False
            # down
            if next_index[0] == i + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i+1][j].has_top_wall = False
            # up
            if next_index[0] == i - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i-1][j].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
    
    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False

    def _solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i , j):
        self._animate()
        curr_cell = self._cells[i][j]
        curr_cell.visited = True

        # solved - end of maze is reached
        if curr_cell == self._cells[self._num_rows-1][self._num_cols-1]:
            return True
        
        # left
        if j > 0 and not self._cells[i][j-1].has_right_wall and not self._cells[i][j-1].visited:
            curr_cell.draw_move(self._cells[i][j-1])
            result = self._solve_r(i, j-1)
            if result:
                return True
            else:
                curr_cell.draw_move(self._cells[i][j-1], True)

        # right
        if j < self._num_cols - 1 and not self._cells[i][j+1].has_left_wall and not self._cells[i][j+1].visited:
            curr_cell.draw_move(self._cells[i][j+1])
            result = self._solve_r(i, j+1)
            if result:
                return True
            else:
                curr_cell.draw_move(self._cells[i][j+1], True)

        # down
        if i < self._num_rows - 1 and not self._cells[i+1][j].has_top_wall and not self._cells[i+1][j].visited:
            curr_cell.draw_move(self._cells[i+1][j])
            result = self._solve_r(i+1, j)
            if result:
                return True
            else:
                curr_cell.draw_move(self._cells[i+1][j], True)

        # up
        if i > 0 and not self._cells[i-1][j].has_bottom_wall and not self._cells[i-1][j].visited:
            curr_cell.draw_move(self._cells[i-1][j])
            result = self._solve_r(i-1, j)
            if result:
                return True
            else:
                curr_cell.draw_move(self._cells[i-1][j], True)
        
        return False