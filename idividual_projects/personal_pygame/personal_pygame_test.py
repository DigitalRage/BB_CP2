import standard_pygame as sp

engine = sp.Engine(300, 60)

bg = sp.Image("background.png").size(800)
engine.add(bg, 0, 0, layer=0)

player = sp.Image("player.png").size(20)
engine.add(player, 150, 45, layer=5)

engine.run()
