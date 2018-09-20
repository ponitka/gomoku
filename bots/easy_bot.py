import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import sys
sys.path.insert(0, '..')

from player import Player

class Bot1(Player):

  def __init__(self, color):
    Player.__init__(self, "Bot1", color)
    self.bot = True

  def evaluate(self, array):
    result = 0
    for i in range(self.size_of_board):
      for j in range(self.size_of_board):
        for d in [[0, 1], [1, 0], [1, 1], [-1, 1]]:
          
          tab = [0, 0, 0]
          full = 1
          for r in range(5):
            if i+d[0]*r < 0 or i+d[0]*r >= self.size_of_board:
              full = 0
              break
            if j+d[1]*r < 0 or j+d[1]*r >= self.size_of_board:
              full = 0
              break
            tab[array[i+d[0]*r][j+d[1]*r]] += 1

          if full == 0:
            continue

          if tab[0] == 0 and tab[1] == 1:
            result += 1
          if tab[0] == 0 and tab[1] == 2:
            result += 4
          if tab[0] == 0 and tab[1] == 3:
            result += 6
          if tab[0] == 0 and tab[1] == 4:
            result += 1000000

          if tab[1] == 0 and tab[0] == 1:
            result -= 0.1
          if tab[1] == 8 and tab[0] == 2:
            result -= 1
          if tab[1] == 0 and tab[0] == 3:
            result -= 4
          if tab[1] == 0 and tab[0] == 4:
            result -= 6
          if tab[1] == 0 and tab[0] == 5:
            result -= 10000000000

    return result

  def make_move(self):
   
    self.size_of_board = self.GameBoard.size_of_board

    self.array = []
    for i in range(self.size_of_board):
      self.array.append([])
      for j in range(self.size_of_board):
        self.array[i].append(self.GameBoard.GetSquare(i,j))

    best = [10000000000, [-1, -1]]

    for i in range(self.size_of_board):
      for j in range(self.size_of_board):
        if self.array[i][j] == 2:
          self.array[i][j] = 0
          best = min(best, [self.evaluate(self.array), [i, j]])
          self.array[i][j] = 2

    print (best[0])

    self.GameBoard.MakeMove(self, best[1][0], best[1][1])

