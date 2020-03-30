from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*arguments, **kwargs):
        print('Function Name: ' + func.__name__)
        for i, a in enumerate(arguments):
            print('Argument ' + str(i + 1) + ' = ' + str(a))

        for key, value in kwargs.items():
            print('{0} = {1}'.format(key.value))

        return func(*arguments, **kwargs)

    return wrapper


@decorator
def f(n):
    print(n)
