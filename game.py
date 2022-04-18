from turtle import speed
import pygame
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, mixer
import os
import time
import random

WIDTH,HEIGHT=900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Target Practice")
target_img=pygame.image.load(os.path.join('img','tar.png'))
target_img_resize=pygame.transform.scale(target_img,(150,150))
bg_img=pygame.image.load(os.path.join('img','bg.png'))
bg_img_resize=pygame.transform.scale(bg_img, (900,500))


FPS = 60
num_bots = 1
bot_L = []
bot_S = []
target_speedX = 6

def spawn(event):
    global target_speedX
    
    x_val = random.randint(0,400)
    y_val = random.randint(0,800)

  
    tar_box = pygame.Rect(y_val, x_val, (target_img_resize.get_width()), (target_img_resize.get_height()))
    tbox = pygame.Rect(y_val+40, x_val+10, target_img_resize.get_width()-70,(target_img_resize.get_height()-15))
    
    for i in range (num_bots):

        bot_S.append(tbox)
        bot_L.append(tar_box)

        if event.type==MOUSEBUTTONDOWN:
            if event.button==1:
                if bot_S[i].collidepoint(event.pos):
                    bot_S.remove(bot_S[i])
                    bot_L.remove(bot_L[i])


        bot_S[i].x+=target_speedX
        bot_L[i].x+=target_speedX

        if bot_S[i].x<=0:
            target_speedX=6
        elif bot_S[i].x>=825:
            target_speedX=-6

            
        pygame.draw.rect(WIN, (255,0,0), bot_S[i], 1)
        pygame.draw.rect(WIN,(0,255,0),bot_L[i],1)
        WIN.blit(target_img_resize, bot_L[i])
        




def main():
        
    clock=pygame.time.Clock()
    run = True
    score=0

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
    

        WIN.blit(bg_img_resize,(0,0))
        spawn(event)

        pygame.display.update()


    pygame.quit()


if __name__=="__main__":
    main()