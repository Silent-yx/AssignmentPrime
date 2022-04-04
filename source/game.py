import pygame
import sys
from start import Start
from supermarket import Supermarket

#pygame 初始化
pygame.init()

#设置主窗口

main_screen = pygame.display.set_mode((1280,960))
pygame.display.set_caption("LOCK-DOWN IN USTC")
image_icon = pygame.image.load("../res/image/icon.png").convert()
pygame.display.set_icon(image_icon)

#开始界面
Start(main_screen)
#商店界面
result = Supermarket.Game1(main_screen)

#结束游戏
pygame.quit()
sys.exit()