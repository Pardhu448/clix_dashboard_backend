from functools import wraps
def my_decorator(f):
 @wraps(f)
 def wrapper(*args, **kwds):
    print('Calling decorated function')
    return f(*args, **kwds)
 return wrapper

@my_decorator
def example():
 """Docstring"""
 print('Called example function')

if __name__ == '__main__':
    example()
    print(example.__name__)
    print(example.__doc__)
