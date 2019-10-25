# # 键盘控制
# import pygame, sys
#
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# background = pygame.Surface(screen.get_size())
# background.fill([255, 255, 255])
# clock = pygame.time.Clock()
#
# class Ball(pygame.sprite.Sprite):
#     def __init__(self, image_file, speed, location):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location
#         self.speed = speed
#
#     def move(self):
#         if self.rect.left <= screen.get_rect().left or \
#             self.rect.right >= screen.get_rect().right:
#             self.speed[0] = - self.speed[0]
#         newpos = self.rect.move(self.speed)
#         self.rect = newpos
#
# my_ball = Ball('shun2.png', [10, 0], [20, 20])
#
# delay = 1  # 开始重复之前的等待时间
# interval = 10  # 多长时间重复一次
# pygame.key.set_repeat(delay, interval)  # 生成多个KEYDOWN事件
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 my_ball.rect.top = my_ball.rect.top - 10
#             elif event.key == pygame.K_DOWN:
#                 my_ball.rect.top = my_ball.rect.top + 10
#
#     clock.tick(30)
#     screen.blit(background, (0, 0))
#     my_ball.move()
#     screen.blit(my_ball.image, my_ball.rect)
#     pygame.display.flip()

# # 鼠标控制
# import pygame, sys
#
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# background = pygame.Surface(screen.get_size())
# background.fill([255, 255, 255])
# clock = pygame.time.Clock()
#
# class Ball(pygame.sprite.Sprite):
#     def __init__(self, image_file, speed, location):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location
#         self.speed = speed
#
#     def move(self):
#         if self.rect.left <= screen.get_rect().left or \
#         self.rect.right >= screen.get_rect().right:
#             self.speed[0] = - self.speed[0]
#         newpos = self.rect.move(self.speed)
#         self.rect = newpos
#
# my_ball = Ball('shun2.png', [10, 0], [20, 20])
#
# hold_down = False # 鼠标是否按下
#
# delay = 1  # 开始重复之前的等待时间
# interval = 10  # 多长时间重复一次
# pygame.key.set_repeat(delay, interval)  # 生成多个KEYDOWN事件
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         # elif event.type == pygame.MOUSEMOTION:
#         #     my_ball.rect.center = event.pos
#
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             hold_down = True
#         elif event.type == pygame.MOUSEBUTTONUP:
#             hold_down = False
#         elif event.type == pygame.MOUSEMOTION:
#             if hold_down == True:
#                 my_ball.rect.center = event.pos
#
#
#     clock.tick(30)
#     screen.blit(background, (0, 0))
#     my_ball.move()
#     screen.blit(my_ball.image, my_ball.rect)
#     pygame.display.flip()

# 定时器控制
import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640, 480])
background = pygame.Surface(screen.get_size())
background.fill([255, 255, 255])
clock = pygame.time.Clock()

class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        if self.rect.left <= screen.get_rect().left or \
        self.rect.right >= screen.get_rect().right:
            self.speed[0] = - self.speed[0]
        newpos = self.rect.move(self.speed)
        self.rect = newpos

my_ball = Ball('shun2.png', [10, 0], [20, 20])

pygame.time.set_timer(pygame.USEREVENT, 100)
direction = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.USEREVENT:
            my_ball.rect.centery = my_ball.rect.centery + (30 * direction)
            if my_ball.rect.top <= screen.get_rect().top or \
            my_ball.rect.bottom >= screen.get_rect().bottom:
                direction = - direction

    clock.tick(30)
    screen.blit(background, (0, 0))
    my_ball.move()
    screen.blit(my_ball.image, my_ball.rect)
    pygame.display.flip()