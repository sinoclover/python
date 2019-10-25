# # 显示球
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load('beach_ball.png')
# screen.blit(my_ball, [50, 50])  # 将像素从一个表面复制到另一个表面
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# # 移动球
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load('beach_ball.png')
# screen.blit(my_ball, [50, 50])
# pygame.display.flip()
# pygame.time.delay(2000)
# screen.blit(my_ball, [150, 50])
# pygame.draw.rect(screen, [255, 255, 255], [50, 50, 90, 90], 0) # 利用图层覆盖以擦除原位置
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# # 移动球更流畅
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load('beach_ball.png')
# x = 50
# y = 50
# screen.blit(my_ball, [x, y])
# pygame.display.flip()
# for looper in range(1, 100):
#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
#     x += 5
#     screen.blit(my_ball, [x, y])
#     pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# # 反弹球
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load('shun2.png')
# x = 50
# y = 50
# x_speed = 5
# screen.blit(my_ball, [x, y])
# pygame.display.flip()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
#     x = x + x_speed
#     if x > screen.get_width() - 90 or x < 0:
#         x_speed = - x_speed
#     screen.blit(my_ball, [x, y])
#     pygame.display.flip()

# # 2D反弹球
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load('shun2.png')
# x = 50
# y = 50
# x_speed = 5
# y_speed = 5
# screen.blit(my_ball, [x, y])
# pygame.display.flip()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0) # 先覆盖掉原位置再生成新位置后刷新屏幕
#     x = x + x_speed
#     y = y + y_speed
#     if x > screen.get_width() - 90 or x < 0:
#         x_speed = - x_speed
#     if y > screen.get_height() - 90 or y < 0:
#         y_speed = - y_speed
#     screen.blit(my_ball, [x, y])
#     pygame.display.flip()

# # 翻转球
# import pygame, sys
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load('shun2.png')
# x = 50
# y = 50
# x_speed = 5
# screen.blit(my_ball, [x, y])
# pygame.display.flip()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
#     x = x + x_speed
#     if x > screen.get_width() - 90:
#         x = -90
#     screen.blit(my_ball, [x, y])
#     pygame.display.flip()

