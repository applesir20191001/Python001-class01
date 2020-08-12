学习笔记

一、序列分类 
• 容器序列：可以存放不同类型的数据。即可以存放任意类型对象的引用。
• 扁平序列：只能容纳一种类型。也就是说其存放的是值而不是引用。换句话说扁平序列其实是一段连续的内存空间，由此可见扁平序列其实更加紧凑。但是它里面只能存放诸如字符、字节和数值这种基础类型。


容器序列存在深拷贝、浅拷贝问题 
• 注意：非容器（数字、字符串、元组）类型没有拷贝问题

容器序列：list、tuple、collections.deque
扁平序列：str、dict、bytes、bytearray、memoryview (内存视图)、array.array 


另一种分类方式 
• 可变序列list、bytearray、array.array、collections.deque 和memoryview。
• 不可变序列tuple、str 和bytes。 

二、函数工具与高阶函数

functools 和 itertools

三、functools.lru_cache

functools.lru_cache(maxsize=128, typed=False)有两个可选参数
maxsize代表缓存的内存占用值，超过这个值之后，就的结果就会被释放
typed若为True，则会把不同的参数类型得到的结果分开保存

四、functools.wraps

 @wraps接受一个函数来进行装饰
 并加入了复制函数名称、注释文档、参数列表等等的功能
 在装饰器里面可以访问在装饰之前的函数的属性
 @functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
 用于在定义包装器函数时发起调用 update_wrapper() 作为函数装饰器。 
 它等价于 partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)。