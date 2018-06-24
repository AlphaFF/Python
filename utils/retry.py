import functools
import traceback

import requests


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


def retry(retries=3):
    """一个失败请求重试，或者使用下边这个功能强大的retrying
    pip install retrying
    https://github.com/rholder/retrying

    :param retries: number int of retry times.
    """
    def _retry(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            index = 0
            while index < retries:
                index += 1
                try:
                    response = func(*args, **kwargs)
                    if response.status_code == 404:
                        print(404)
                        break
                    elif response.status_code != 200:
                        print(response.status_code)
                        continue
                    else:
                        break
                except Exception as e:
                    traceback.print_exc()
                    response = None
            return response
        return _wrapper
    return _retry


@retry(retries=5)
def get(*args, **kwargs):
    url = 'https://httpbin.org/ip'
    response = requests.get(url, verify=False)
    print(response.status_code)
    return response


if __name__ == '__main__':
    get()
