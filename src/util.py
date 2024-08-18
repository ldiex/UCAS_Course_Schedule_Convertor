import functools
import json

# 在exception中增加函数名的装饰器
def detailException(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # 获取函数名称
            func_name = func.__name__
            # 创建新的异常信息
            new_message = f"in '{func_name}': {str(e)}"
            # 抛出新的异常
            raise RuntimeError(new_message) from e
    return wrapper
