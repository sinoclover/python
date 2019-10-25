# 导入pygame, sys, random模块
import Gameing
import sys
import random

# 使用图片素材创建列表便于使用
skier_images = ['skier_down.png', 'skier_right1.png', 'skier_right2.png',
                'skier_left2.png', 'skier_left1.png']  # 包括滑雪人物的五个动作，并对应0， 1， 2， -2， -1下标

# 创建滑雪者类，并以精灵类作为基类继承
class SkierClass(Gameing.sprite.Sprite):
    # 创建滑雪者
    def __init__(self):
        # 初始化数据
        Gameing.sprite.Sprite.__init__(self)  # 调用__init__方法进行操作对象实例化和初始化操作
        self.image = Gameing.image.load('skier_down.png')  # 调用图片以显示滑雪者
        self.rect = self.image.get_rect()  # 用图片矩形大小定义显示范围
        self.rect.center = [320, 100]  # 定义图片显示的初始中心
        self.angle = 0  # 初始角度为0

    # 滑雪者转向
    def turn(self, direction):
        # 方法中接收方向参数
        self.angle = self.angle + direction
        # 角度限定在-2至2之间
        if self.angle < -2:
            self.angle = -2
        if self.angle > 2:
            self.angle = 2
        # center = self.rect.center
        self.image = Gameing.image.load(skier_images[self.angle])  # 根据角度变换调用滑雪者姿态列表
        # self.rect.center = center
        speed = [self.angle, 6 - abs(self.angle) * 2]  # 角度与速度对应关系，0-6,1-4,2-2
        return speed  # 返回速度列表

    # 滑雪者左右移动
    def move(self, speed):
        # 方法中接收速度参数
        self.rect.centerx = self.rect.centerx + speed[0]  # 滑雪者对象图片的中点横坐标根据角度不断变化
        # 滑雪者图片中心左右限定在20至620之间
        if self.rect.centerx < 20:
            self.rect.centerx = 20
        if self.rect.centerx > 620:
            self.rect.centerx = 620

# 创建障碍物类，并以精灵类作为基类继承
class ObstacleClass(Gameing.sprite.Sprite):
    # 创建树和小旗
    def __init__(self, image_file, location, type):
        # 接收图片素材参数、位置参数和类型参数
        Gameing.sprite.Sprite.__init__(self)  # 调用__init__方法进行操作对象实例化和初始化操作
        self.image_file = image_file  # 导入图片库参数
        self.image = Gameing.image.load(image_file)  # 使用图片库参数显示
        self.location = location  # 使用位置参数对对象进行定位
        self.rect = self.image.get_rect()  # 获取图片矩形大小定义显示范围
        self.rect.center = location  # 使用位置参数定位图片
        self.type = type  #  使用类型参数对类型进行初始化
        self.passed = False

    # 让场景向上滚
    def scroll(self, t_ptr):
        self.rect.centery = self.location[1] - t_ptr  # 根据障碍物图片中心纵坐标？

# 创建窗口，包含随机的树和小旗的创建方法
def create_map(start, end):
    obstacles = Gameing.sprite.Group()
    #  使用精灵组生成障碍物集
    # gates = pygame.sprite.Group()
    locations = []  # 建立位置集的空列表
    for i in range(10):  # 循环10次，即每次调用方法创建10个物体
        row = random.randint(start, end)  # 接收参数作为行坐标任意数的范围
        col = random.randint(0, 9)  # 以0-9作为列坐标任意数的范围
        location = [col * 64 + 20, row * 64 + 20]  # 定位物体行列坐标
        if not (location in locations):
            locations.append(location)  # 如果新坐标不在坐标位置集的列表中则将其添加进列表
            type = random.choice(['tree', 'flag'])  # 随机选择物体的类别
            if type == 'tree':
                img = 'skier_tree.png'
            elif type == 'flag':
                img = 'skier_flag.png'
            obstacle = ObstacleClass(img, location, type) # 应用类方法创建物体
            obstacles.add(obstacle)  # 在障碍物集中添加物体
    return obstacles  # 返回障碍物集

# 有移动时重绘屏幕
def animate():
    screen.fill([255, 255, 255])  # 屏幕填充白色
    Gameing.display.update(obstacles.draw(screen))  # 更新指定的部分，即画到屏幕上的障碍物
    screen.blit(skier.image, skier.rect)  # 将对象的图片置于屏幕上
    screen.blit(score_text, [10, 10])  # 将得分技术表置于屏幕上
    Gameing.display.flip()  # 更新整个画面显示到屏幕

# 切换到场景的下一屏
def updateObstacleGroup(map0, map1):
    obstacles = Gameing.sprite.Group()
    for ob in map0:
        obstacles.add(ob)
    for ob in map1:
        obstacles.add(ob)
    return obstacles

# 游戏准备
Gameing.init()
screen = Gameing.display.set_mode([640, 640])
clock = Gameing.time.Clock()
skier = SkierClass()
speed = [0, 6]
map_position = 0
points = 0
map0 = create_map(20, 29)
map1 = create_map(10, 19)
activeMap = 0
obstacles = updateObstacleGroup(map0, map1)
font = Gameing.font.Font(None, 50)

# 开始主循环
while True:
    clock.tick(30)  # 每秒更新30次图形
    # 检查按键或窗口是否关闭
    for event in Gameing.event.get():
        if event.type == Gameing.QUIT:
            sys.exit()
        if event.type == Gameing.KEYDOWN:
            if event.key == Gameing.K_LEFT:
                speed = skier.turn(-1)
            elif event.key == Gameing.K_RIGHT:
                speed = skier.turn(1)
    skier.move(speed)  # 移动滑雪者
    map_position += speed[1]  # 滚动场景

    # 从场景的一个窗口切换到下一个窗口
    if map_position >= 640 and activeMap == 0:
        activeMap = 1
        map0 = create_map(20, 29)
        obstacles = updateObstacleGroup(map0, map1)
    if map_position >= 1280 and activeMap == 1:
        activeMap = 0
        for ob in map0:
            ob.location[1] = ob.location[1] - 1280
        map_position = map_position - 1280
        map1 = create_map(10, 19)
        obstacles = updateObstacleGroup(map0, map1)

    # 检测是否碰到树或得到小旗
    for obstacle in obstacles:
        obstacle.scroll(map_position)
    hit = Gameing.sprite.spritecollide(skier, obstacles, False)
    if hit:
        if hit[0].type == 'tree' and not hit[0].passed:
            points = points - 100
            skier.image = Gameing.image.load('skier_crash.png')
            animate()
            Gameing.time.delay(1000)
            skier.image = Gameing.image.load('skier_down.png')
            skier.angle = 0
            speed = [0, 6]
            hit[0].passed = True
        elif hit[0].type == 'flag' and not hit[0].passed:
            points += 10
            obstacles.remove(hit[0])

    score_text = font.render('Score: ' +str(points), 1, (0, 0, 0))
    animate()



