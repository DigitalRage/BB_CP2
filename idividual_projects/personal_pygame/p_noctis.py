import standard_pygame as sp

engine = sp.Engine(500, 150)
bg = sp.Image("Noctis Shirt.png").size(600)
engine.add(bg, 0, 0, layer=0)

engine.run()