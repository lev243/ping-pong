from pygame import *

window = display.set_mode((900, 800))
game = True
finish = False
timer = time.Clock()
color_fon = (135, 206, 250)

while game:
    window.fill(color_fon)
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    timer.tick(60)