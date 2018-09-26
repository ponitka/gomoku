import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from player import Player

class Square(Gtk.Box):

  def __init__(self, row, column, Players, Board):
    Gtk.Box.__init__(self)

    self.Players = Players
    self.Board = Board
    self.Occupant = -1

    self.button = Gtk.Button()
    self.label = Gtk.Label()
    self.label2 = Gtk.Label()
    self.button.add(self.label2)

    self.button.set_relief(Gtk.ReliefStyle.NONE)

    self.change_color("white", self.label)
    self.change_color("white", self.label2)

    self.overlay = Gtk.Overlay()
    self.add(self.overlay)
    self.overlay.add_overlay(self.button)
    self.overlay.add(self.label)

    self.button.connect("clicked", self.on_button_clicked)
    self.button.connect("enter", self.on_button_mouse, True)
    self.button.connect("leave", self.on_button_mouse, False)

    Gtk.Widget.set_size_request(self, 30, 30)
    self.label.set_property("width-request", 30)
    self.label.set_property("height-request", 30)

  def change_color(self, color, label):
    coolor = Gdk.color_parse(color)
    rgba = Gdk.RGBA.from_color(coolor)
    label.override_background_color(0, rgba)

  def change(self, Player):
    self.change_color( Player.color, self.label )
    self.change_color( Player.color, self.label2 )
    self.Occupant = Player

  def on_button_clicked(self, widget):   
    if self.Players[0].bot == True:
      return

    self.MakeMove(self.Players[0])

  def on_button_mouse(self, widget, ok):
    if self.Occupant != -1:
      return

    if ok == False:
      self.change_color("white", self.label2)

    if self.Players[0].move_allowed == False or self.Players[0].bot == True:
      return

    if ok == True:
      self.change_color(self.Players[0].color, self.label2)

  def MakeMove(self, Player):
    if Player.move_allowed == False or self.Occupant != -1:
      return False

    self.change(Player)
    self.Board.CHECK()

    return True
