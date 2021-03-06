import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from player import Player

class Sidebar(Gtk.Box):

  def __init__(self, Players, GameWindow):
    Gtk.Box.__init__(self)
    self.Players = Players
    self.GameWindow = GameWindow
    
    self.set_orientation(Gtk.Orientation.VERTICAL)
    self.set_spacing(20)

    self.label = Gtk.Label("It's your turn.")
    self.add(self.label)
    self.label.set_size_request(180, -1)

  def update(self):
    if self.Players[0].bot == True:
      self.label.set_text("It's bot's turn. (%s)" % self.Players[0].name)
    else:
      self.label.set_text("It's your turn, %s." % self.Players[0].name)

