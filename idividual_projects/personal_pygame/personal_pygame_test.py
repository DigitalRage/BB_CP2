# test_game.py
import standard_pygame as sp

engine = sp.Engine(120, 60)

# Make sure player.png exists and that its top-left pixel is your "background" color
player = sp.Image("player.png").size(40)
engine.add(player, 10, 10)

engine.run()
