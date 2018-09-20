import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from player import Player

class Square(Gtk.Button):

  def __init__(self, row, column, Players, Board):
    Gtk.Button.__init__(self)

    self.Players = Players
    self.Board = Board

    self.Occupant = -1

    self.label = Gtk.Label()
    #self.label.set_label("%d, %d" % (row, column))
    self.add(self.label)

    self.connect("clicked", self.on_button_clicked)

    Gtk.Widget.set_size_request(self, 20, 20)

  def change_color(self, color):
    coolor = Gdk.color_parse(color)
    rgba = Gdk.RGBA.from_color(coolor)
    self.label.override_background_color(0, rgba)

  def change(self, Player):
    #self.set_label( Player.name )
    self.change_color( Player.color )
    self.Occupant = Player

  def on_button_clicked(self, widget):   
    if self.Players[0].bot == True:
      return

    self.MakeMove(self.Players[0])

  def MakeMove(self, Player):
    if Player.move_allowed == False or self.Occupant != -1:
      return False

    self.change(Player)
    self.Board.CHECK()

    return True
