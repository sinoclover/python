import pygame, sys

# 初始化程序
pygame.init()
screen = pygame.display.set_mode([400, 600])
screen.fill([0, 0, 0])
ship = pygame.image.load('lunarlander.png')
moon = pygame.image.load('moonsurface.png')
ground = 1000 #
start = 90  # 初始飞船高度
clock = pygame.time.Clock()  # 控制帧速率,即控制每个循环多长时间运行一次
ship_mass = 5000.0  # 飞船质量
fuel = 5000.0  # 燃料
velocity = -100.0  # 初始速度
gravity = 10  # 重力
height = 2000  # 初始高度
thrust = 0  # 推力
delta_v = 0  # 速度变化量
y_pos = 90  #
held_down = False


# 推进器操纵杆的精灵类
class ThrottleClass(pygame.sprite.Sprite):
    def __init__(self, location = [0, 0]):
        pygame.sprite.Sprite.__init__(self)  # 初始化精灵类
        image_surface = pygame.surface.Surface([30, 10])  # 操纵杆大小
        image_surface.fill([0, 0, 255])  # 操纵杆色彩
        self.image = image_surface.convert()  # 将绘制表面转化为图片像素
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = location


# 计算高度、速度、加速度和燃料
def calculate_velocity():
    global thrust, fuel, velocity, delta_v, height, y_pos
    delta_t = 1 / fps  # 将一帧作为变化的时间
    thrust = (500 - myThrottle.rect.centery) * 5.0  # 推力计算公式
    fuel -= thrust / (10 * fps)  # 根据推力减少燃料
    if fuel < 0:
        fuel = 0.0
    if fuel < 0.1:
        thrust = 0.0
    delta_v = delta_t * (-gravity + 200 * thrust / (ship_mass + fuel))
    velocity = velocity + delta_v  # 一帧时间内速度的变化
    delta_h = velocity * delta_t  # 一帧时间内走过的路程
    height = height + delta_h  # 一帧时间高度的变化
    y_pos = ground - (height * (ground - start) / 2000) - 90


# 使用字体对象显示统计信息
def display_stats():
    v_str = "velocity: %i m/s" % velocity
    h_str = "height:   %.1f" % height
    t_str = "thrust:   %i" % thrust
    a_str = "acceleration: %.1f" % (delta_v * fps)
    f_str = "fuel:  %i" % fuel

    v_font = pygame.font.Font(None, 26)
    v_surf = v_font.render(v_str, 1, (255, 255, 255))
    screen.blit(v_surf, [10, 50])

    a_font = pygame.font.Font(None, 26)
    a_surf = a_font.render(a_str, 1, (255, 255, 255))
    screen.blit(a_surf, [10, 100])

    h_font = pygame.font.Font(None, 26)
    h_surf = h_font.render(h_str, 1, (255, 255, 255))
    screen.blit(h_surf, [10, 150])

    t_font = pygame.font.Font(None, 26)
    t_surf = t_font.render(t_str, 1, (255, 255, 255))
    screen.blit(t_surf, [10, 200])

    f_font = pygame.font.Font(None, 26)
    f_surf = f_font.render(f_str, 1, (255, 255, 255))
    screen.blit(f_surf, [60, 300])


# 使用两个三角形作为火焰
def display_flames():
    flames_size = thrust / 15
    for i in range(2):
        startx = 252 - 10 + i * 19
        starty = y_pos + 83
        pygame.draw.polygon(screen, [255, 109, 14], [(startx, starty),
                                    (startx + 4, starty + flames_size),(startx + 8, starty)], 0)


# 游戏结束时显示最终统计信息
def display_final():
    final1 = "Game over"
    final2 = "You landed at %.1f m/s" % velocity
    if velocity > -5:
        final3 = "Nice landing!"
        final4 = "I hear NASA is hiring!"
    elif velocity > -15:
        final3 = "Ouch!  A bit rough, but you survived."
        final4 = "You'll do better next time."
    else:
        final3 = "Yikes!  You crashed a 30 Billion dollar ship."
        final4 = "How are you getting home?"
    pygame.draw.rect(screen, [0, 0, 0], [5, 5, 350, 280],0)
    f1_font = pygame.font.Font(None, 70)
    f1_surf = f1_font.render(final1, 1, (255, 255, 255))
    screen.blit(f1_surf, [20, 50])
    f2_font = pygame.font.Font(None, 40)
    f2_surf = f2_font.render(final2, 1, (255, 255, 255))
    screen.blit(f2_surf, [20, 110])
    f3_font = pygame.font.Font(None, 26)
    f3_surf = f3_font.render(final3, 1, (255, 255, 255))
    screen.blit(f3_surf, [20, 150])
    f4_font = pygame.font.Font(None, 26)
    f4_surf = f4_font.render(final4, 1, (255, 255, 255))
    screen.blit(f4_surf, [20, 180])
    pygame.display.flip()


myThrottle = ThrottleClass([15, 500])

# 主循环
while True:
    clock.tick(30)
    fps = clock.get_fps()
    if fps < 1:
        fps = 30
    if height > 0.01:
        calculate_velocity()  # 先计算参数
        screen.fill([0, 0, 0])  # 背景颜色
        display_stats()  # 显示统计信息
        pygame.draw.rect(screen, [0, 0, 255], [80, 350, 24, 100], 2)  # 画出燃料表
        fuelbar = 96 * fuel / 5000
        pygame.draw.rect(screen, [0, 255, 0], [84, 448 - fuelbar, 18, fuelbar], 0)
        pygame.draw.rect(screen, [255, 0, 0], [25, 300, 10, 200], 0)  # 画出推进器滑轨
        screen.blit(moon, [0, 500, 400, 100])  # 画出月球
        pygame.draw.rect(screen, [60, 60, 60], [220, 535, 70, 5], 0)  # 着陆板
        screen.blit(myThrottle.image, myThrottle.rect)  # 画出推力操纵杆
        display_flames()  # 显示尾部火焰
        screen.blit(ship, [230, y_pos, 50, 90])  # 画出飞船

        instruct1 = "Land softly without running out of fuel"
        instruct2 = "Good landing: < 15 m/s    Great landing:  < 5m/s"
        inst1_font = pygame.font.Font(None, 24)
        inst1_surf = inst1_font.render(instruct1, 1, (255, 255, 255))
        screen.blit(inst1_surf, [50, 550])
        inst2_font = pygame.font.Font(None, 24)
        inst2_surf = inst1_font.render(instruct2, 1, (255, 255, 255))
        screen.blit(inst2_surf, [20, 575])
        pygame.display.flip()

    else:  # 游戏结束
        display_final()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            held_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            held_down = False
        elif event.type == pygame.MOUSEMOTION:
            if held_down:
                myThrottle.rect.centery = event.pos[1]
                if myThrottle.rect.centery < 300:
                    myThrottle.rect.centery = 300
                if myThrottle.rect.centery > 500:
                    myThrottle.rect.centery = 500
