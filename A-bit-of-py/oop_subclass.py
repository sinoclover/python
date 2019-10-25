# coding = UTF - 8

class SchoolMember:
    '''代表任何学校里的成员'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {0})'.format(self.name))

    def tell(self):
        '''告诉我有关我的细节'''
        print('Name:"{0}" Age:"{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''代表一位老师。'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)  #在方法名前面加上基类名作为前缀，再传入变量以调用基类
        self.salary = salary
        print('(Initialized Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''代表一位学生'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('（Initialized Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs.Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()

members = [t, s]
for member in members:
    member.tell()