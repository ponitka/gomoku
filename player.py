import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Player:

  def __init__(self, name, color):

    self.move_allowed = True
    self.GameBoard = -1
    self.color = color

    self.name = name
    if name == "":
      self.bot = True
    else:
      self.bot = False

  def make_move():
    print("siema")
    pass
