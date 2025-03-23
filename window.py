from tkinter import Tk, BOTH, Canvas
from point import Point
from line import Line
from cell import Cell
from maze import Maze

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, height=height, width=width)
        self.canvas.pack()
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
    
    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

def main():
    win = Window(800, 600)
    # p1 = Point(15, 25)
    # p2 = Point(200, 25)
    # line = Line(p1, p2)
    # win.draw_line(line, "yellow")
    # c = Cell(40, 40, 80, 80, win)
    # c.draw()
    # c2 = Cell(100, 40, 140, 80, win)
    # c2.draw()
    # c.draw_move(c2)
    m = Maze(40, 40, 10, 10, 40, 40, win)
    m._solve()
    win.wait_for_close()

main()