import pygame

class Button():
    def __init__(self, screen, x, y):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # 设置按钮的尺寸和其他属性  
        self.width = 100 
        self.height = 100
        self.statue = False
        
        # 标记按钮的位置
        self.x = x
        self.y = y

        # 创建按钮的rect对象
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.left = self.x * self.width + self.x + 49
        self.rect.top = self.y * self.height + self.y + 49

    def draw_button(self):
        # 绘制一个用颜色填充的按钮
        if self.statue:
            self.screen.fill((255, 255, 255), self.rect)
        else:
            self.screen.fill((0, 0, 0), self.rect)