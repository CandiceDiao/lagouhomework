import string
import yaml

class Animal:
    name:string ="default"
    color:string="default"
    age:int = 20
    gender:string="M"

    def __init__(self, kwargs):
        self.name = kwargs['name']
        self.clolr = kwargs['clor']
        self.age = kwargs['age']
        self.gender = kwargs['gender']


    def canCall(self):
        print("animal can call")
        return "call"

    def canRun(self):
        return "animal can run"

class Cat(Animal):

    # def __init__(self,name,color,age,gender,fur="short"):
    #     self.name = name
    #     self.clolr = color
    #     self.age = age
    #     self.gender=gender
    #     self.fur=fur
    def __init__(self, kwargs):
        self.name = kwargs['name']
        self.clolr = kwargs['clor']
        self.age = kwargs['age']
        self.gender = kwargs['gender']
        self.fur = "short"

    def catchMonley(self):
        return("捉到了老鼠")

    def canCall(self):
        print("cat call like miao miao")

class Dog(Animal):

    # def __init__(self,name,color,age,gender,fur="long"):
    #     self.name = name
    #     self.clolr = color
    #     self.age = age
    #     self.gender=gender
    #     self.fur=fur

    def __init__(self, kwargs):
        self.name = kwargs['name']
        self.clolr = kwargs['clor']
        self.age = kwargs['age']
        self.gender = kwargs['gender']
        self.fur = "long"

    def home(self):
        print("dog can keep home security")

    def canCall(self):
        return "dog call like wang wang"

def printInfo(kwargs):
    return ("姓名:{name}，颜色：{clor},年龄：{age}，性别：{gender}，毛发：{fur}".format(**kwargs))

if __name__ == '__main__':
    with open("animal") as f:
        data = yaml.safe_load(f)

    dataCat = data['cat']
    cat =Cat(dataCat)
    cat.catchMonley()
    print('猫猫的'+printInfo(dataCat)+','+cat.catchMonley())

    dataDog = data['dog']
    dog = Dog(dataDog)
    dog.home()
    print('狗狗的'+printInfo(dataDog))










