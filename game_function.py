import sys
import pygame

def turn(buttons, i, j):
    """游戏规则---点击一个棋子后, 该棋子与其上下左右的棋子都变色"""
    buttons[i][j].statue = not buttons[i][j].statue
    
    if i == 0:
        buttons[i+1][j].statue = not buttons[i+1][j].statue
    elif i == 2:
        buttons[i-1][j].statue = not buttons[i-1][j].statue
    else:
        buttons[i+1][j].statue = not buttons[i+1][j].statue
        buttons[i-1][j].statue = not buttons[i-1][j].statue
    
    if j == 0:
        buttons[i][j+1].statue = not buttons[i][j+1].statue
    elif j == 2:
        buttons[i][j-1].statue = not buttons[i][j-1].statue
    else:
        buttons[i][j+1].statue = not buttons[i][j+1].statue
        buttons[i][j-1].statue = not buttons[i][j-1].statue

def check_game(buttons):
    """检查是否通关"""
    for i in range(3):
            for j in range(3):
                if buttons[i][j].statue == False:
                    return True
    return False

def check_events(buttons):
    # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y =pygame.mouse.get_pos()
                check_button(buttons, mouse_x, mouse_y)

def check_button(buttons, mouse_x, mouse_y):
    """检查鼠标点击的坐标在哪一个按钮上"""
    for i in range(3):
            for j in range(3):
                if buttons[i][j].rect.collidepoint(mouse_x, mouse_y):
                    turn(buttons, i, j)