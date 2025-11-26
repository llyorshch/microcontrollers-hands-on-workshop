import ugame
import stage

bank = stage.Bank.from_bmp16("./ball.bmp")

background = stage.Grid(bank, 10, 8)
game = stage.Stage(ugame.display, 12)
game.layers = [background]
game.render_block()

while True:
  pass