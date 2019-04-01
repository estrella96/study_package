l=[1,2,3,4,5]
# print(l[10]) #IndexError
# print(l.a)#AttributeError
# num=int(input("please input youor num:"))
# print(100/num) #ZeroDivisionError
'''
#异常处理
try:
    num = int(input("please input youor num:"))
    rst=100/num
    print("result is {0}".format(rst))
#捕获异常之后，把异常实例化，出错信息会在实例里
except ZeroDivisionError as e:
    print("input is wrong ")
    print(e)

    exit()



# 批异常处理
try:
    num = int(input("please input youor num:"))
    rst=100/num
    print("result is {0}".format(rst))
#捕获异常之后，把异常实例化，出错信息会在实例里
#可能多种异常 具体的放在前面
#处理异常一旦捕获到一个异常 不会再继续查看 直接进入finally
except ZeroDivisionError as e:
    print("input is wrong ")
    print(e)

    exit()
except NameError as e:
    print("name is wrong")
    print(e)
    exit()
except AttributeError as e:
    print("attr is wrong")
    print(e)
    exit()
#所有异常继承自Exception 放在except的最后
except Exception as e:
    print ("I don't know")
    print(e)
    exit()
'''
#raise案例 用户引发日常
#自定义异常 必须是系统异常的子类
class DanaError(ValueError):
    pass

try:
    print("i love book")
    print(3.14159)
    #手动引发一个异常
    raise DanaError
    print(" value wrong")
except NameError as e:
    print("name error")
except DanaError as e:
    print("dana error")
except ValueError as e:
    print("value error")
except Exception as e:
    print(" exception")
finally:
    print("dddd")





