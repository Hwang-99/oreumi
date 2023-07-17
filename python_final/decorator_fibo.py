import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs) # <--- 함수 실행
        elasped = time.time() - t0     # <--- 함수 실행된 시간
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print("[%0.8fs] %s(%s)-> %r" % (elasped, name, arg_str, result))
        return result
    return clocked


@functools.cache
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

# line 23, in <module>
# @functools.cache
# AttributeError: module 'functools' has no attribute 'cache'