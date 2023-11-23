def logged(function):
    def wrapper(*args, **kwargs):
        res = function(*args, **kwargs)
        args_in_func_name = tuple(x for x in args)
        return f"you called {function.__name__}{args_in_func_name}\nit returned {res}"
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))
print()


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
