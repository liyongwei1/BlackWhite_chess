import sys
import pygame
import random
import time

import game_function as gf
from button import Button

def run_game():
    # 初始化pygame, 设置和屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("黑白棋")

    # 创建一个用于存储黑白块的编组
    buttons = [[Button(screen, 0, 0), Button(screen, 1, 0), Button(screen, 2, 0)], [Button(screen, 0, 1), Button(screen, 1, 1), Button(screen, 2, 1)], [Button(screen, 0, 2), Button(screen, 1, 2), Button(screen, 2, 2)]]


    # 开始游戏的主循环
    while True:

        # 随机化棋子
        for i in range(3):
            for j in range(3):
                buttons[i][j].statue = random.choice([True, False])
                
        # 操作循环
        while gf.check_game(buttons):
            
            time.sleep(0.1)
            gf.check_events(buttons)

            # 绘制图像
            screen.fill((102,102,102))
            for i in range(3):
                for j in range(3):
                    Button.draw_button(buttons[i][j])
            
            # 让最近绘制的屏幕可见
            pygame.display.flip()
        
        # 通关后刷新, 并且继续游戏
        time.sleep(0.5)
        screen.fill((51,51,51))
        pygame.display.flip()
        time.sleep(0.5)

run_game()