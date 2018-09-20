import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import random
from datetime import datetime

import sys
sys.path.insert(0, '..')

from player import Player

class Bot2(Player):

  def __init__(self, color):
    Player.__init__(self, "Bot2", color)
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
            result += 500
          if tab[0] == 0 and tab[1] == 4:
            result += 1000000

          if tab[1] == 0 and tab[0] == 1:
            result -= 0.05
          if tab[1] == 8 and tab[0] == 2:
            result -= 2
          if tab[1] == 0 and tab[0] == 3:
            result -= 10
          if tab[1] == 0 and tab[0] == 4:
            result -= 20
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

    best_eva = 10000000000
    solutions = []

    for i in range(self.size_of_board):
      for j in range(self.size_of_board):
        if self.array[i][j] == 2:
          self.array[i][j] = 0
          my_eva = self.evaluate(self.array)
          if my_eva < best_eva:
            solutions.clear()
            best_eva = my_eva
          if best_eva == my_eva:
            solutions.append([i, j])
          self.array[i][j] = 2

    random.seed(datetime.now())
    index = random.randint(0, len(solutions)-1)

    self.GameBoard.MakeMove(self, solutions[index][0], solutions[index][1])
