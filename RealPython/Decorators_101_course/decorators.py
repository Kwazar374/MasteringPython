import functools
import time

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # before
        value = func(*args, **kwargs)
        # after
        return value
    return wrapper_decorator

def timer(func):
    """Print the runtime if the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        """Print the function signature and return value"""
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}= {v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

""" @do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hello {name}"

print(return_greeting('Adam')) """