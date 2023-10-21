
from pygame import *
from random import randint



win_wight = 1200
win_hight = 800
FPS = 60
clock = time.Clock()

window = display.set_mode((win_wight, win_hight))
display.set_caption('Horror')
background1 = transform.scale(image.load('1.jpg'), (win_wight, win_hight))
background2 = transform.scale(image.load('2.jpg'), (win_wight, win_hight))
background3 = transform.scale(image.load('3.jpg'), (win_wight, win_hight))
background4 = transform.scale(image.load('rec.jpeg'), (win_wight, win_hight))
font.init()
font1 = font.SysFont('Arial', 36)
win = font1.render('Выбери дверь, левая(нажми на 1) правая(нажми 2)', True, (255, 255, 255))
win1 = font1.render('Выбери дверь, левая(нажми на 3) правая(нажми 4)', True, (255, 255, 255))
win2 = font1.render('Выбери дверь, левая(нажми на 5) правая(нажми 6)', True, (255, 255, 255))

run = True

rec = 0
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_1:
                rec = 1
            elif e.key == K_2:
                rec = 2
        
    if rec==0:
        window.blit(background1,(0, 0))
        window.blit(win,(200, 200))
    elif rec==1:
        window.blit(background2,(0, 0))
        window.blit(win1,(200, 200))
    elif rec==2:
        window.blit(background3,(0, 0))
        window.blit(win2,(200, 200))

    clock.tick(FPS)
    display.update()


            
    