import pygame
from pygame.locals import *
import time

class Hero():
    def __init__(self,screen_temp):
        self.x = 140
        self.y = 700
        self.image = pygame.image.load('./feiji/hero1.png')
        self.screen = screen_temp
    def display(self):
        self.screen.blit(self.image,(self.x, self.y))
    def move_left(self):
        self.x-=5
    def move_right(self):
        self.x+=5
    def move_up(self):
        self.y-=5
    def move_down(self):
        self.y+=5

def key_control(hero_temp):
    #判断是否是点击了退出按钮
    for event in pygame.event.get():
        # print(event.type)
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                #控制飞机让其向左移动
                hero_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                #控制飞机让其向右移动
                hero_temp.move_right()
            elif event.key == K_w or event.key == K_UP:
                print('')
                #控制飞机让其向上移动
                hero_temp.move_up()
            elif event.key == K_s or event.key == K_DOWN:
                print('')
                #控制飞机让其向下移动
                hero_temp.move_down()
            elif event.key == K_SPACE:
                print('space')
def main():
    #1创建窗口
    screen = pygame.display.set_mode((400,852),0,32)

    #2创建一个背景图片
    background = pygame.image.load('./feiji/background.png')
    
    hero = Hero(screen)
    while True:
        screen.blit(background, (0,0))
        hero.display()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.02)



if __name__ == '__main__':
    main()
