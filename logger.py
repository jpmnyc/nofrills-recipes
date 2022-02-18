def log(func):
    def wrapper(*args, **kwargs):
        name = func.__name__
        print(f"Staring {name}")
        result = func(*args, **kwargs)
        print(f"Finished {name}")
        return result
    return wrapper

