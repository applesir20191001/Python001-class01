# 容器序列：list、tuple、collections.deque、dict
# 扁平序列：str
# 可变序列：list、dict、collections.deque
# 不可变序列：str、tuple


import functools
import time
from functools import wraps

# @timer 装饰器


def timer(func):
    # 结构不变增加wraps
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        time.sleep(1)
        end = time.time()
        print(f'{func.__name__} 耗时: {end-start}')
        return ret
    return inner


@timer
def foo(a, b, c):
    return (a+b+c)


print(foo(1, 2, 3))

# 实现 map() 函数的功能


@timer
def my_map(func, iter_list):
    for i in iter_list:
        yield func(i)


@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


print(list(my_map(fibonacci, [1, 2, 3])))
