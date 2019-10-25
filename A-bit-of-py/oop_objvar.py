# coding =  UTF - 8

class Robot:
    """表示有一个带有名字的机器人。"""
    population = 0  # 属于Robot类的类变量

    def __init__(self, name):  # __init__方法会使用一个名字初始化Robot实例。
        """初始化数据"""
        self.name = name  # name属于一个self对象的对象变量
        print("(Initializing {0})".format(self.name))  # 使用self.name来引用对象变量，且值是指定给每个对象的

        # 当有人被创建时，机器人将会增加人口数量
        Robot.population += 1  # 使用Robot.population来引用类变量，或者使用self.__class__.population来引用

    def die(self):
        """我挂了。"""
        print("{0} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{0} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候

        没问题，你做得到。"""
        print("Greetings, my masters call me {0}.".format(self.name))

    @classmethod
    def how_many(cls):  # how_many是一个属于类而非对象的方法，即将其定义为一个classmethod或是一个staticmethod
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3P0")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destory them.")
droid1.die()
droid2.die()

Robot.how_many()