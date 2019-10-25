# # 基本函数
# def printMyAddress():
#     print('Warren Sande')
#     print('123 Main Street')
#     print('Ottawa, Ontario, Canada')
#     print('K2M 2E9')
#     print()
#
# printMyAddress()

# # 向函数传递参数
# def printMyAddress(myName):
#     print(myName)
#     print('123 Main Street')
#     print('Ottawa, Ontario, Canada')
#     print('K2M 2E9')
#     print()
#
# printMyAddress('Edward Chang')

# # 带有返回值的函数
# def calculateTax(price, tax_rate):
#     total = price + (price * tax_rate)
#     return total
#
# my_price = float(input('Enter a price: '))
#
# totalPrice = calculateTax(my_price, 0.06)
# print('Price =', my_price, 'Total price =', totalPrice)

# # 打印局部变量
# def calculateTax(price, tax_rate):
#     total = price + (price * tax_rate)
#     return total
#
# my_price = float(input('Enter a price: '))
#
# totalPrice = calculateTax(my_price, 0.06)
# print('Price =', my_price, 'Total price =', totalPrice)
# print(price)  # price是局部变量存在于函数体中

# # 使用全局变量
# def calculateTax(price, tax_rate):
#     total = price + (price * tax_rate)
#     print(my_price)
#     return total
#
# my_price = float(input('Enter a price: '))
#
# totalPrice = calculateTax(my_price, 0.06)
# print('Price =', my_price, 'Total price =', totalPrice)

# # 在函数体中试图修改全局变量
# def calculateTax(price, tax_rate):
#     total = price + (price * tax_rate)
#     my_price = 10000
#     print('my_price (inside function) = ', my_price)  # 在试图修改全局变量时生成了名字相同的局部变量
#     return total
#
# my_price = float(input('Enter a price: '))
#
# totalPrice = calculateTax(my_price, 0.06)
# print('Price =', my_price, 'Total price =', totalPrice)
# print('my_price (outside function) = ', my_price)

# #  使用类
# class Ball:
#     def bounce(self):
#         if self.direction == 'down':
#             self.direction = 'up'
# myBall = Ball()
# myBall.direction = 'down'
# myBall.color = 'red'
# myBall.size = 'small'
#
# print('I just created a ball.')
# print('My ball is', myBall.size)
# print('My ball is', myBall.color)
# print("My ball's direction is", myBall.direction)
# print("Now I'm going to bounce the ball")
# print()
# myBall.bounce()
# print("Now the ball's direction is", myBall.direction)

# # __init__()方法初始化
# class Ball:
#     def __init__(self, color, size, direction):
#         self.color = color
#         self.size = size
#         self.direction = direction
#
#     def bounce(self):
#         if self.direction == 'down':
#             self.direction = 'up'
#
# myBall = Ball('red', 'small', 'down')
# print('I just created a ball.')
# print('My ball is', myBall.size)
# print('My ball is', myBall.color)
# print("My ball's direction is", myBall.direction)
# print("Now I'm going to bounce the ball")
# print()
# myBall.bounce()
# print("Now my ball's direction is", myBall.direction)

# # 使用__str__()改变打印对象的方式
# class Ball:
#     def __init__(self, color, size, direction):
#         self.color = color
#         self.size = size
#         self.direction = direction
#
#     def __str__(self):
#         msg = 'Hi, I am a ' + self.size + ' ' + self.color + ' ball!'
#         return msg
#
# myBall = Ball('red', 'small', 'down')
# print(myBall)

# #  热狗
# class  HotDog:
#     def __init__(self):
#         self.cooked_level = 0
#         self.cooked_string = 'Raw'
#         self.condiments = []
#
#     def __str__(self):
#         msg = 'hot dog'
#         if len(self.condiments) > 0:
#             msg = msg + ' with '
#         for i in self.condiments:
#             msg = msg+i+', '
#         msg = msg.strip(', ')
#         msg = self.cooked_string + ' ' + msg + '.'
#         return msg
#
#     def cook(self, time):
#         self.cooked_level = self.cooked_level + time
#         if self.cooked_level > 8:
#             self.cooked_string = 'Charcoal'
#         elif self.cooked_level > 5:
#             self.cooked_string  = 'Well-done'
#         elif self.cooked_level > 3:
#             self.cooked_string = 'Medium'
#         else:
#             self.cooked_string = 'Raw'
#     def addCondiment(self, condiment):
#         self.condiments.append(condiment)
#
# myDog = HotDog()
# print(myDog)
# print('Cooking hot dog for 4 minutes...')
# myDog.cook(4)
# print(myDog)
# print('Cooking hot dog for 3 minutes... ')
# myDog.cook(3)
# print(myDog)
# print('What happens if I cook it for 10 more minutes? ')
# myDog.cook(10)
# print(myDog)
# print('Now, I am going to add some stuff on my hot dog')
# myDog.addCondiment('ketchup')
# myDog.addCondiment('mustard')
# print(myDog)

# # 银行账户
# class BankAccount:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#         self.money = 0.0
#
#     def showMoney(self):
#         print('The accont balance is', self.money)
#
#     def addMoney(self, number):
#         self.money += number
#         print('You deposited', number)
#         print('The new balance is:', self.money)
#
#     def spendMoney(self, number):
#         if self.money >= number:
#             self.money -= number
#             print('You withdrew', number)
#             print('The new balance is:', self.money)
#         else:
#             print('You tried to withdraw', number)
#             print('The account balance is:', self.money)
#             print('Withdrawal denied. Not enough funds.')
#
#
# class InterestAccount(BankAccount):
#
#     def addInterest(self, rate):
#         interest = self.money * rate
#         print('Adding interest to the account,',rate * 100, 'percent')
#         self.addMoney(interest)
#
# myAccount = BankAccount('Edward Chang', 123456)
# print('Account name:', myAccount.name)
# print('Accountt id:', myAccount.id)
# myAccount.showMoney()
#
# myAccount.addMoney(100.5)
# myAccount.spendMoney(90.32)
# myAccount.spendMoney(20.98)
#
# myAccount = InterestAccount('Edward Chang', 123456)
# print('Account name:', myAccount.name)
# print('Accountt id:', myAccount.id)
# myAccount.showMoney()
# myAccount.addMoney(89.25)
# myAccount.addInterest(0.12)

