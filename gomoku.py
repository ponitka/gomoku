import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import sys
sys.path.insert(0, 'bots/')

from game import GameWindow
from hello import HelloWindow
from player import Player
from bot1 import Bot1
from bot2 import Bot2

H = HelloWindow()
H.connect("destroy", Gtk.main_quit)
H.show_all()
Gtk.main()

if H.Name1 == "":
  Player1 = Bot1(H.Color1)
else:
  Player1 = Player(H.Name1, H.Color1)

if H.Name2 == "":
  Player2 = Bot2(H.Color2)
else:
  Player2 = Player(H.Name2, H.Color2)

G = GameWindow(Player1, Player2)
G.show_all()
Gtk.main()
