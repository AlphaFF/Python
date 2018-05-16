# 参数化装饰器
def retry(attempt):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*arg, **kw):
            att = 0
            while att < attempt:
                try:
                    return func(*arg, **kw)
                except Exception as e:
                    att += 1
        return wrapper
    return decorator


# 重试次数
@retry(attempt=3)
def get_response(url):
    r = requests.get(url)
    print(r.status_code, r.url)
    return r.status_code