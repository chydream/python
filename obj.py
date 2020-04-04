# 面向对象
# 类是对象的抽象 对象是类的实例表现
# 封装private  继承 多态:同样的行为产生不同的效果
class Cat(object):
    """
    猫科动物类  __doc__ 文档信息  __module__  __class__  __dict__
    """
    # 类的属性
    tag = 'Cat base'
    # 构造函数
    # self 代表实例
    def __init__(self, name, age, sex = None):
        # 实例化后的属性
        self.name = name
        self.__age = age  #__age 私有变量
        self.sex = sex
    # 析构函数
    def __del__(self):
        pass
    def catch(self):
        print('猫可以捕捉老鼠.')
    def eat(self):
        print('猫喜欢吃鱼')
    def show_info(self):
        print("{0}的年龄是{1}岁".format(self.name, self.__age))
    def set_age(self, age):
        self.__age = age
    def set_name(self, name):
        self.name = name

class Tiger(Cat):
    def eat(self):
        print('eat tig')


if __name__ == '__main__':
    # cat_black = Cat('小黑', 10)
    # cat_black.eat()
    # cat_black.show_info()
    # print(cat_black.name)
    # #print(cat_black.__age) 无法访问私有变量
    # cat_black.name = '嘿嘿'
    # cat_black.__age = 6 #无法操作私有变量
    # cat_black.show_info()
    # cat_black.set_age(7)
    # cat_black.show_info()
    # Cat.tag = 'others'
    # print(Cat.tag)
    # print(cat_black.tag)
    #
    # cat_white = Cat('小白', 10)
    # print(Cat.tag)
    # print(cat_white.tag)
    #
    # #类的实例判断
    # isinstance(cat_black, Cat)
