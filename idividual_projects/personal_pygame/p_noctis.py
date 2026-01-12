import standard_pygame as sp

engine = sp.Engine(300, 60)
bg = sp.Image("Noctis Shirt.png").size(300)
engine.add(bg, 0, 0, layer=0)

engine.run()