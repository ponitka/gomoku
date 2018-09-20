import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import sys
sys.path.insert(0, '..')

from player import Player

## Usage:
##  name your class either Bot1 or Bot2:
##   depending on wheter you want your bot to move first
##  name your file bot1.py or bot2.py accordingly

## Functions:
##  self.GameBoard.GetSquare(i,j) -- 0 for you, 1 for opponent, 2 for empty
##  self.GameBoard.MakeMove(self, i, j) 

class SampleBot(Player):

  def __init__(self, color):
    Player.__init__(self, "Edek", color) ## bot's name
    self.bot = True

  def make_move(self):

    if self.GameBoard == -1:
      print("i don't have any board")
    else:
      for i in range(0, self.GameBoard.size_of_board):
        for j in range(0, self.GameBoard.size_of_board):
          if self.GameBoard.MakeMove(self, i, j) == True:
            return

