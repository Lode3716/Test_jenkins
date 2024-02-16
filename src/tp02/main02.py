"""
   
 auth : l.devigne

"""


def do_log(func):
    def wrapper(*args, **kwargs):
        print("LOG ", func, args, kwargs)
        r = func(*args, **kwargs)
        print("LOG Après ", func, r)
        return r

    return wrapper


def do_log(func):
    def wrapper_func(func):
        def wrapper(*args, **kwargs):
            print("LOG ", func, args, kwargs)
            r = func(*args, **kwargs)
            print("LOG Après ", func, r)
            return r

        return wrapper

    return wrapper_func


@do_log('Hello 2 ')
# @do_log premier do log
def say_hello(name):
    return f"Hello {name}"


def main():
    r = say_hello("Laurent")
    print(r)


if __name__ == '__main__':
    main()
