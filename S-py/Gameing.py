# # 绘制圆和方
# import pygame
# import sys
#
# pygame.init()
#
# screen = pygame.display.set_mode([640, 480])
# screen.fill([159, 120, 80])
#
# pygame.draw.circle(screen, [255, 0, 0], [320, 240], 50, 5)
#
# pygame.draw.rect(screen, [0, 255, 0], [250, 150, 300, 200], 5)
# my_list =[100, 50, 200, 50]
# pygame.draw.rect(screen, [0, 0, 255], my_list, 5)
# my_rect = pygame.Rect(300, 400, 50, 50)
# pygame.draw.rect(screen, [0, 0, 0], my_rect, 5)
#
# pygame.display.flip()  #  翻转刷新，更新屏幕
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# # 现代几何艺术
# import pygame, sys, random
#
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# for i in range(100):
#     width = random.randint(0, 250)
#     height = random.randint(0, 100)
#     top = random.randint(0, 400)
#     left = random.randint(0, 500)
#     my_list = [left, top, width, height]
#     pygame.draw.rect(screen, [0, 0, 0], my_list, 1)
# pygame.display.flip()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# # 现代几何艺术2
# import pygame, sys, random
# from pygame.color import THECOLORS
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# for i in range(100):
#     width = random.randint(0, 250)
#     height = random.randint(0, 100)
#     top = random.randint(0, 400)
#     left = random.randint(0, 500)
#     color_name = random.choice(list(THECOLORS.keys()))
#     #  python2  color_name = random.choice(THECOLORS.keys())
#     color = THECOLORS[color_name]
#     line_width = random.randint(1, 3)
#     my_list = [left, top, width, height]
#     pygame.draw.rect(screen, color, my_list, line_width)
# pygame.display.flip()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# # 使用矩形画曲线
# import pygame, sys
# import math
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# for x in range(0, 640):
#     y = int(math.sin(x / 640 * 4 * math.pi) * 200 + 240)
#     pygame.draw.rect(screen, [0, 0, 0], [x, y, 1, 1], 1)
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# # 使用矩形画曲线
# import pygame, sys
# import math
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# plotPoints = []
# for x in range(0, 640):
#     y = int(math.sin(x / 640 * 4 * math.pi) * 200 + 240)
#     plotPoints.append([x, y])
# pygame.draw.lines(screen, [0, 0, 0], False, plotPoints, 2)
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# # 逐点绘制
# import pygame, sys
# import math
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# for x in range(0, 640):
#     y = int(math.sin(x / 640 * 4 * math.pi) * 200 + 240)
#     screen.set_at([x, y], [0, 0, 0])
# pygame.display.flip()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()