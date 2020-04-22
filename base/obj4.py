# 类的静态方法与实例方法与类的方法
class Cat(object):
    tag = "猫科动物"
    def __init__(self, name):
        self.name = name

    @staticmethod
    def breath():
        print("猫都需要呼吸空气")

    @classmethod   # 只能取类的属性，不能取实例属性
    def show_info(cls, name):
        # print('类的属性：{0}，实例的属性：{1}'.format(cls.tag, cls.name))
        return cls(name)

    def show_info2(self):
        print('类的属性：{0}，实例的属性：{1}'.format(self.tag, self.name))

if __name__ == "__main__":
    cat = Cat('小黑')
    # cat.breath()
    # Cat.breath()
    # cat.show_info(Cat, '小属')
    # cat2 = Cat.show_info('小属')
    # cat2.show_info2()
    # Cat.show_info2('')