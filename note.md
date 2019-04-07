#1 模块 p01.py p02.py
- 一个模块是一个包含python代码的文件 .py
- 使用模块原因
    - 程序太大 需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做命名空间使用 避免命名冲突
- 定义模块
    - 就是一个普通模块 可以直接书写
    - 模块的规范
        - 函数 （单一功能）
        - 类 （相似功能的组合 或者类似业务模块）
        - 测试代码
    - 使用模块
        - 模块直接导入
            - 模块名称直接以数字开头 借助importlib
        - 语法
            import module_name
            module_name.function_name
            module_name.class_name
            模块名.class/function
        - import 模块 as 别名 p03.py
            别名.class/function
    - from 模块 import 函数名，类名 （只导入所需）p03
        不需要写模块名直接用
    - from 模块 import * (导入所有)
- if __name__=='__main__':
    - 避免模块代码导入被动执行
    - 建议所有程序入口都以此代码为入口
#2 模块的搜索路径和存储
- 搜索路径
    - 加载模块时，系统会在哪些方法寻找模块
- 系统默认模块搜索路径 p04
    import sys
    sys.path
- 添加搜索路径
    sys.path.append(dir)
- 模块加载顺序
    1. 内存中加载好的模块
    2. python的内置模块
    3. 搜索sys.path路径
 
#3 包
- 包是一种组织管理代码的方式，包里存放模块
- 用于将模块包含在一起的文件夹
- 自定义包的结构
    -   /---包
    -   /---/-- __init__.py
    -   /---/-- 模块1
    -   /---/-- 模块2
- 包的导入操作
    - import package_name
        - 直接导入一个包 可以使用__init__.py中的内容
        - 使用方式
            - package_name.func_name
            - package_name.class_name.func_name()
    - import package_name as p
        - 默认对__init__.py的访问
    - import package.module
        - 导入一个具体的模块
        - 使用方法
            - package.module.func_name
            - package.module.class.fun()
            - package.module.class.var
    - from...import
        - from package import module1,modue2,...
        - 不执行__init__内容
            from pkg01 import p01
            p01.sayHello()
        - from package import *
            - 导入当前包__init__.py内容
            - 使用方法
                func_name()
                class_name.func_name()
                class_name.var
        - from package.module import *
            - 导入包中指定模块的所有内容
                func_name()
                class_name.func_name()
                
- 在开发环境中经常会使用其他模块 也可以直接导入
    - import 完整的包或模块路径
- __all__ 的用法
    - 在使用 from package import * 时
    - __init__.py 中如果文件为空，或者没有__all__,只可以导入__init__内容
    - __init__ 如果设置了__all__,可以按__all__指定的子包或模块导入
    - __all__=['module1','module2','package1'...]
     
# 命名空间
- 区分不同位置不同功能但相同名称的函数或变量的一个特定前缀
- 防止命名冲突
    setName()
    Student.setName()
    Dog.setName()
    
# 异常处理
- 广义上的错误分为错误和异常
- 错误 可以人为避免
- 异常 在语法逻辑正确的前提下，出现的问题
- 在python中 异常是一个类 可以处理和使用
- 异常分类
    - 系统给定的异常 05.py
        FloatingPointError
        IndexError
        KeyboardInterrupt
        NameError
        SyntaxError
        OverflowError
        TypeError
        ZeroDivisionError
- 异常处理模块 除except外else finally可选
    - try:
        尝试某个操作
      except 异常1
        解决方案1
      except 异常2
        解决方案2
      else:
        没有异常执行
      finally:
        有没有异常都要执行
- 用户手动引发异常
    - 用户自己引发一个异常
    - raise关键词 raise 异常类
    - raise 自定义异常
- 自定义异常
    - 自定义发生异常的代码
    - 发生异常后的提示
    - 发生异常的行数
# 常用模块 （除string都要先导入）06.py
- calendar
- time
- datetime
- timeit
- os
- shutil
- zip
- math
- string
# calendar
- 日历相关的
- 属性和方法
    - calendar(y,w,l,c):获取一年的日历字符串 w=每个日期之间的间隔字符数 l=每周占用的行数 c=每个月之间的间隔字符数
    - isleap(y):是否是闰年
    - leapdays(y1,y2)：获取指定年份之间的闰年个数
    - month(y,m):获取某月的日历字符串
    - monthrange(y,m):返回月周几开始和月的总天数
    - monthcalendar(y,m):返回一个月每天的矩阵列表
    - prcal(y):打印日历
    - prmonth(y,m):打印某个月
    - weekday(y,m,d):返回周几
# time
- 时间戳
    - 一个时间表示，语言不同可以是整数也可以是浮点数
    - 从1970年1月1日0时0分0秒到现在经历的秒数
    - 如果时间是以前或者很远的未来 可能出现异常
    - 32位操作系统可以支持到2038年
- UTC时间
    - 国际标准时间
    - 中国 UTC+8 东八区
- 夏令时
    - 夏天时间调快一小时
- 时间元组
    - 一个包含时间内容的普通元组
    - 年 月 日 时 分 秒 周几 第几天 夏令时
    - 属性方法
        - timezone :当前时区和UTC时间相差的秒数 没有夏令时的情况
        - altzone: 同上 有夏令时
        - daylight: 测当前是否是夏令时状态
        - time():得到时间戳
        - localtime():当前时间 类型为时间元组 可以用.获取相应属性
        - asctime(t):正常字符串化之后的时间格式
        - ctime: 获取字符串化的当前时间
        - mktime(t):使用时间元组获取对应的时间戳
        - clock():获取cpu时间 3.0-3.3
        - sleep(n):使程序进入睡眠 n秒后继续
        - strftime:将时间元组转化为自定义的字符串
            - %d %H %m %M......
# datetime
- 提供日期和时间的运算和表示
- 属性和方法
    - date(y,m,d):日期 
    - time(h,m,s):时间
    - datetime:提供日期和时间组合
    - timedelta:时间差 时间长度
    - today
    - now
    - utcnow
    - fromtimestamp
# timeit-时间测量工具
- 测量程序运行时间间隔
