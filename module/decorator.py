import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        elapsed = end-start
        print(f"{func.__name__} took {round(elapsed*1000000,1)} microseconds.")
        return value
    return wrapper


@timer
def sleep(seconds):
    time.sleep(seconds)


# if __name__ == "__main__":
#     for i in range(1, 3):
#         sleep(i)

