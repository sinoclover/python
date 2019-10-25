# # 第一次发出声音
# import pygame, sys
#
# pygame.init()
# pygame.mixer.init()
#
# screen = pygame.display.set_mode([640, 480])
# pygame.time.delay(1000)
#
# splat = pygame.mixer.Sound('splat.wav')
# splat.play()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# # 播放第一首音乐
# import pygame, sys
#
# pygame.init()
# pygame.mixer.init()
#
# screen = pygame.display.set_mode([640, 480])
# pygame.time.delay(1000)
#
# pygame.mixer.music.load('bg_music.mp3')
# pygame.mixer.music.play()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# # 调节BGM的音量
# import pygame, sys
#
# pygame.init()
# pygame.mixer.init()
#
# screen = pygame.display.set_mode([640, 480])
# pygame.time.delay(1000)
#
# pygame.mixer.music.load('bg_music.mp3')
# pygame.mixer.music.set_volume(0.30)
# pygame.mixer.music.play()
# splat = pygame.mixer.Sound('splat.wav')
# splat.set_volume(0.50)
# splat.play()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

# 等待歌曲结束
import pygame, sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640, 480])
pygame.time.delay(1000)

pygame.mixer.music.load('bg_music.mp3')
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play()
splat = pygame.mixer.Sound('splat.wav')
splat.set_volume(0.50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if not pygame.mixer.music.get_busy():
            splat.play()
            pygame.time.delay(1000)
            sys.exit()