import unittest
import random
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
    
    def test_maze_break_entrance_and_exit(self):
        m = Maze(20, 20, 5, 6, 20, 20)
        self.assertEqual(
            m._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m._cells[m._num_rows-1][m._num_cols-1].has_bottom_wall,
            False
        )

    def test_reset_cells_visited(self):
        num_rows = 5
        num_cols = 6
        m = Maze(20, 20, num_rows, num_cols, 20, 20)
        rand_row = random.randrange(num_rows)
        rand_col = random.randrange(num_cols)
        m._cells[rand_row][rand_col].visited = True
        m._reset_cells_visited()
        self.assertEqual(m._cells[rand_row][rand_col].visited, False)

if __name__ == "__main__":
    unittest.main()