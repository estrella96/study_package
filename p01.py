# 模块
# 包含一个学生类 一个sayhello函数 一个打印语句

class Student():
    def __init__(self,name="NoName",age=18):
        self.name=name
        self.age=age
    def say(self):
        print("My name is {0}".format(self.name))
def sayHello():
    print("hi,welcome to bj")
#单独作为文件运行输出这一句 作为模块不执行
if __name__=='__main__':
    print("this is a module")