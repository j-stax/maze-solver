from point import Point
from line import Line

class Cell:
    def __init__(self, x1, y1, x2, y2, win=None, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True, visited=False):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.visited=visited
    
    def draw(self):
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "#d9d9d9")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "#d9d9d9")
        if self.has_bottom_wall:
            line = Line(Point(self._x2, self._y2), Point(self._x1, self._y2))
            self._win.draw_line(line, "black")
        else: 
            line = Line(Point(self._x2, self._y2), Point(self._x1, self._y2))
            self._win.draw_line(line, "#d9d9d9")
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x1, self._y1))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(self._x1, self._y2), Point(self._x1, self._y1))
            self._win.draw_line(line, "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        line_color = "gray" if undo else "red"
        p1_ctr_half_x = (self._x2 - self._x1) // 2
        p1_ctr_half_y = (self._y2 - self._y1) // 2
        p2_ctr_half_x = (to_cell._x2 - to_cell._x1) // 2
        p2_ctr_half_y = (to_cell._y2 - to_cell._y1) // 2
        line = Line(Point(self._x1 + p1_ctr_half_x, self._y1 + p1_ctr_half_y), Point(to_cell._x1 + p2_ctr_half_x, to_cell._y1 + p2_ctr_half_y))
        self._win.draw_line(line, line_color)

        
        