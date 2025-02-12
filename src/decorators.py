import os
from functools import wraps


def log(filename=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                massage = f"{func.__name__} ok"
            except Exception as err:
                massage = f"{func.__name__} error: {err}. Inputs {args}, {kwargs}"
            # Если задан параметр filename
            if filename:
                # Создаем папку logs и записываем сообщение в файл
                os.makedirs("logs", exist_ok=True)
                filepath = os.path.join("logs", f"{filename}")
                with open(filepath, "a", encoding="utf-8") as file:
                    file.write(massage + "\n")
            # Если не задан параметр filename
            else:
                print(massage)
            return result

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
