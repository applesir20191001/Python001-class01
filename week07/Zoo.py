from abc import ABCMeta, abstractmethod

# 动物园类
class Zoo(object):

    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, instance):
        if id(instance) in self.animals:
            raise ValueError('该小动物已经在本动物园里报名了！')    
        self.animals[id(instance)] = instance.__class__.__name__
        
    #用于判断是否有猫
    def __getattr__(self, item):
        for value in self.animals.values():
            #print(value)
            if value == item:
                return True
        return False
        
# 动物类
class Animal(metaclass=ABCMeta):
    
    def __init__(self,cut, shape, nature):
        # cut：类型  shape：体型 nature：性格
        if shape == '小':
            self.shape = 100 
        elif shape == '中等':
            self.shape = 200 
        else:
            self.shape = 300
        self.cut = cut 
        self.nature = nature 
    
    #把函数改成属性
    @property
    def is_terrible(self):
        if (self.shape >= 200 and self.cut == '食肉类型' and self.nature == '性格凶猛'):
            return True
        else:
            return False

# 猫类
class Cat(Animal):
    _call = "miao miao"
    def __init__(self, name, cut, shape, nature):
        self.name = name
        super().__init__(cut,shape,nature)
        
    def is_no_terrible(self):
        if super().is_terrible:
            return False
        return True    

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    #猫的名字
    print('猫的名字：' + cat1.name)
    #猫的叫声
    print('猫的叫声：' +cat1._call)
    #猫是否适合作为宠物
    print('是否适合作为宠物：：%s' %cat1.is_no_terrible())
    # 增加一只猫到动物园
    z.add_animal(cat1)
    #再添加就报错了
    #z.add_animal(cat1)
    cat2 = Cat('大花猫 2', '食肉类型', '中等', '性格凶猛')
    #猫的名字
    print('猫的名字：' + cat2.name)
    #猫的叫声
    print('猫的叫声：' + cat2._call)
    #猫是否适合作为宠物
    print('是否适合作为宠物：：%s' %cat2.is_no_terrible())
    # 增加一只猫到动物园
    z.add_animal(cat2)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    print('动物园是否有猫这种动物：%s' %have_cat)
    # 动物园是否有狗这种动物
    have_dog = getattr(z, 'Dog')
    print('动物园是否有狗这种动物：%s' %have_dog)
