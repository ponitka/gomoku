import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from board import Board
from sidebar import Sidebar
from player import Player

class GameWindow(Gtk.Window):

  def dele(self, abc):
    self.board.game_is_running = False
    Gtk.main_quit()

  def __init__(self, Player1, Player2):
    Gtk.Window.__init__(self, title="Gomoku")
    self.set_border_width(20)
    self.connect("destroy", self.dele)
    self.set_resizable(False)

    gh = Gdk.Geometry()
    gh.min_aspect = 1
    gh.max_aspect = 1
    self.set_geometry_hints(None, gh, Gdk.WindowHints.ASPECT)

    look = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 20)
    self.add(look)

    self.Players = [Player1, Player2]

    self.board = Board(15, self.Players, self)
    look.pack_end(self.board, True, True, 0)

    self.sidebar = Sidebar(self.Players, self)
    look.pack_end(self.sidebar, True, True, 0)
    self.sidebar.update()

    self.connect("key-press-event", self.press)

    if self.Players[0].bot == True:
      self.Players[0].make_move()

  def new_game(self):
    self.board.game_is_running = False
    self.destroy()

    self.Players[0].move_allowed = True
    self.Players[1].move_allowed = True

    self.G = GameWindow(self.Players[0], self.Players[1])
    self.G.show_all()
    Gtk.main()

  def finish_game(self, winner):
    if winner == -1:
      self.sidebar.label.set_label("Game finished - draw.")
    else:
      self.sidebar.label.set_label("%s won!" % winner.name)
    self.Players[0].move_allowed = False
    self.Players[1].move_allowed = False

  def press(self, widget, event):
    keyval = event.keyval
    keyval_name = Gdk.keyval_name(keyval)
    state = event.state

    if keyval_name == "n":
      self.new_game()
