import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
import time
import threading

from square import Square

class Board(Gtk.Box):
  
  game_is_running = True
  turn_of_bot = GObject.Property(type=bool, default=False)
  def bots_turn(self):
    if self.game_is_running == False:
      return False
    if self.get_property("turn_of_bot") == True:
      self.set_property("turn_of_bot", False)
      self.Players[0].make_move()
    return True

  def __init__(self, size_of_board, Players, GameWindow):
    Gtk.Box.__init__(self)
    GObject.GObject.__init__(self)

    self.size_of_board = size_of_board
    self.Players = Players
    self.GameWindow = GameWindow

    self.Players[0].GameBoard = self
    self.Players[1].GameBoard = self
 
    GObject.timeout_add(1000, self.bots_turn)

    self.__array = []
    for i in range(self.size_of_board):
      self.__array.append([])
      for j in range(self.size_of_board):
        self.__array[i].append(Square(i, j, self.Players, self))

    self.set_homogeneous(True)
    self.set_spacing(10)
    for i in range(self.size_of_board):
      box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10)
      for j in range(self.size_of_board):
        box.pack_start(self.__array[i][j], True, True, 0)
      box.set_homogeneous(True)
      self.pack_start(box, True, True, 0)

  def GetSquare(self, i, j):
    foo = self.__array[i][j].Occupant
    if foo == self.Players[0]:
      return 0
    if foo == self.Players[1]:
      return 1
    return 2

  def CHECK(self):
    winner = -1
    number_of_empty_squares = self.size_of_board ** 2

    for i in range(self.size_of_board):
      for j in range(self.size_of_board):     
        if self.__array[i][j].Occupant != -1:
          number_of_empty_squares -= 1
          for x in [[1, 0], [0, 1], [1, 1], [1, -1]]:
            wheter = 1
            for r in range(5):
              if i+r*x[0] >= self.size_of_board or i+r*x[0] < 0:
                wheter = 0
                break
              if j+r*x[1] >= self.size_of_board or j+r*x[1] < 0:
                wheter = 0
                break
              if self.__array[i][j].Occupant != self.__array[i+r*x[0]][j+r*x[1]].Occupant:
                wheter = 0
                break
            if wheter == 1:
              winner = self.__array[i][j].Occupant
              break
  
    if winner != -1 or number_of_empty_squares == 0:
      self.GameWindow.finish_game(winner)
    else:
      self.Players[0], self.Players[1] = self.Players[1], self.Players[0]
      self.GameWindow.sidebar.update()

      if self.Players[0].bot == True:
        self.set_property("turn_of_bot", True)
      else:
        self.set_property("turn_of_bot", False)

  def MakeMove(self, Player, i, j):
    if Player != self.Players[0] or Player.move_allowed == False:
      return False

    if isinstance(i, int) == False or isinstance(j, int) == False:
      return False
    if i < 0 or i >= self.size_of_board or j < 0 or j >= self.size_of_board:
      return False

    if self.__array[i][j].MakeMove(Player) == True:
      return True
    else:
      return False
        
