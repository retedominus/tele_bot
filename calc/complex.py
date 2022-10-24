import operation


def calc(operator, args):
    if operator == 'Сложение':
        return operation.f_sum(args[0], args[1])
    elif operator == 'Вычетание':
        return operation.sub(args[0], args[1])
    elif operator == 'Умножение':
        return operation.mult(args[0], args[1])
    elif operator == 'Деление':
        return operation.div(args[0], args[1])
    elif operator == 'Возведение в степень':
        return operation.pow_c(args[0], args[1])
    elif operator == 'Извлечение корня':
        return operation.sqrt(args[0])
    else:
        return None