# 类的继承 issubclass() super(Cat,self)
# 多态

# 继承
class Animal(object):
    tag = '动物'
    def __init__(self,name):
        self.name = name
    def eat(self):
        print('动物都需要吃东西')

    def protected(self):
        print('我是受国家保护的')

class ProtectedMixin(object):
    def protected(self):
        print('我是受保护的')

class Cat(Animal):
    tag = "猫科动物"
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def eat(self):
        super(Cat, self).eat()
        print('猫还喜欢吃鱼')

    def catch(self):
        print('猫可以捕捉老鼠.')

class Panda(Animal, ProtectedMixin):  #多重继承  重名方法 用第一个
    tag = "熊猫"
    def eat(self):
        super(Panda, self).eat()
        print('熊猫喜欢吃竹子')

class HuaCat(Cat):
    tag = "中华猫"
    def eat(self):
        super(HuaCat, self).eat()
        print('中华猫喜欢吃零食')

class DuanCat(Cat):
    tag = "英国短猫"
    def eat(self):
        print('英国短猫喜欢吃短零食')


if __name__ == '__main__':
    cat = HuaCat('中华', '2')
    cat.eat()
    cat_d = DuanCat('短猫', '3')
    cat_d.eat()
    print(issubclass(DuanCat, Cat))
    print(issubclass(DuanCat, Animal))
    print(issubclass(DuanCat, HuaCat))
    pd = Panda('中华')
    pd.protected()