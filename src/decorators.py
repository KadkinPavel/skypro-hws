def log(filename=None):
    """Декоратор для логирования вызовов функции и их результатов"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            # Определяем, куда писать логи
            def write_log(message):
                if filename:
                    with open(filename, 'a') as f:
                        f.write(message + '\n')
                else:
                    print(message)

            try:
                # Выполняем функцию и сохраняем результат
                result = func(*args, **kwargs)
                # Записываем успешный результат
                write_log(f"{func.__name__} ok")
                return result
            except Exception as e:
                # Формируем сообщение об ошибке
                error_type = type(e).__name__
                error_msg = (
                    f"{func.__name__} error: {error_type}. "
                    f"Inputs: {args}, {kwargs}"
                )
                write_log(error_msg)
                raise  # Перебрасываем исключение дальше

        return wrapper

    return decorator
