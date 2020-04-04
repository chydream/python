# 类的高级特性
# @property 将类的方法当做属性来使用
# __slots__:  为指定的类设置一个静态属性列表 节约内存空间
class PetCat(object):
    __slots__ = ('name', '__age', 'color') #不允许添加属性 方法
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            print('年龄只能是整数')
            return 0
        if value < 0 or value > 100:
            print('年龄只能介于0-100之间')
            return 0
        self.__age = value

    @property
    def show_info(self):
        return '我叫：{0},今年{1}岁'.format(self.name, self.age)
    def __str__(self):
        return '我的对象：{0}'.format(self.name)

def eat():
    print("我喜欢吃鱼")

class HuaCat(PetCat):
    __slots__ = ('name', )
    pass

if __name__ == '__main__':
    cat_black = PetCat('小黑', 2)
    rest = cat_black.show_info
    # print(rest)
    # print(cat_black)
    # cat_black.age(6)
    # print(cat_black.age)
    cat_black.color = '白色'
    print(cat_black.color)
    # cat_black.eat = eat
    # cat_black.eat()
    cat_white = HuaCat('小白', 3)
    rest = cat_white.show_info
    print(rest)
    # cat_white.sex = 'male'
    # print(cat_white.sex)
    cat_white.name = 'male'
    print(cat_white.name)