import operation


def calc(operator, args):
    if operator == 'sum':
        return operation.f_sum(args[0], args[1])
    elif operator == 'sub':
        return operation.sub(args[0], args[1])
    elif operator == 'mult':
        return operation.mult(args[0], args[1])
    elif operator == 'div':
        return operation.div(args[0], args[1])
    elif operator == 'pow':
        return operation.pow_c(args[0], args[1])
    elif operator == 'sqrt':
        return operation.sqrt(args[0])
    else:
        return None