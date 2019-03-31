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