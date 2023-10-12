from pygame import *
from random import randint



win_wight = 1200
win_hight = 800
FPS = 60
clock = time.Clock()



window = display.set_mode((win_wight, win_hight))
display.set_caption('Horror')
background1 = transform.scale(image.load('maxresdefault-1-1280x620.jpg'), (win_wight, win_hight))
'''background2 = transform.scale(image.load('ceec42a3eadf946_730x400.jpg'), (win_wight, win_hight))
background3 = transform.scale(image.load('horror-kvest-13-2.jpg'), (win_wight, win_hight))'''



run = True



while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background1,(0, 0))
    

    clock.tick(FPS)
    display.update()   
