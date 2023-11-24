def tags(tag):
    def decorator(func):
        def wrapper(*args):
            start_tag = f"<{tag}>"
            end_tag = f"</{tag}>"
            return f"{start_tag}{func(*args)}{end_tag}"
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
