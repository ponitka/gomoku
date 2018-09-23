# gomoku
Implemented in Python 3 using GTK+ library. <br />

It's an extended version of a popular Tic-Tac-Toe game. Players alternate turns picking an empty square. The winner is the first player to form an unbroken chain of five squares horizontally, vertically, or diagonally. <br />

Game rules and controls:
<ul>
  <li>If you leave name of a player blank, bot will automatically play for that player.</li>
  <li>Click N if you want to start a new game (with the same settings).</li>
  <li>Click a square you want to choose for the player whose turn is now.</li>
</ul>


To start the game run <code>gomoku.py</code> in Python 3 (<code>$ python3 gomoku.py</code>)

To install GTK+ on Ubuntu execute: <br />
<code>$ sudo apt install python-gi python-gi-cairo python3-gi python3-gi-cairo gir1.2-gtk-3.0</code>. <br />
For other platforms follow the instructions from https://pygobject.readthedocs.io/en/latest/getting_started.html.
