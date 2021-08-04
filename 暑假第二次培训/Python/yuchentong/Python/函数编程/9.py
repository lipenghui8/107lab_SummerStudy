def log(f):
    def fn(*args, **kwargs):
        print('call ' + f.__name__ + '()...')
        return f(*args, **kwargs)
    return fn