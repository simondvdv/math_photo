def evaluate_expression(math_string):
    math_string = math_string.replace(' ', '')
    # print('строка ', math_string)
    if '(' in math_string:
        left_index = math_string.find('(')
        for i in math_string[left_index + 1:]:
            if i == '(':
                left_index = math_string[left_index + 1:].find('(') + left_index + 1
                # print('Левый индекс', left_index)
            if i == ')':
                right_index = math_string.find(')')
                # print('Правый индекс', right_index)
                # print(math_string[:left_index])
                # print(math_string[left_index+1:right_index])
                # print(math_string[right_index + 1:])
                # break
                return evaluate_expression(math_string[:left_index] + linear_calc(math_string[left_index+1:right_index])
                                           + math_string[right_index + 1:])
    else:
        return linear_calc(math_string)
    pass


def linear_calc(split_math_string):
    split_math_string = split_math_string.replace(' ', '')
    if '*' in split_math_string:
        operation_index = split_math_string.find('*')
        left_index, right_index = number_creator(operation_index, split_math_string)
        calc_part = str(int(split_math_string[left_index: operation_index]) *
                        int(split_math_string[operation_index+1: right_index+1]))
        return linear_calc(split_math_string[:left_index] + calc_part + split_math_string[right_index + 1:])
    elif '/' in split_math_string:
        operation_index = split_math_string.find('/')
        left_index, right_index = number_creator(operation_index, split_math_string)
        if int(split_math_string[operation_index+1: right_index+1]) == 0:
            return 'На нуль делить нельзя'
        calc_part = str(int(split_math_string[left_index: operation_index]) /
                        int(split_math_string[operation_index+1: right_index+1]))
        return linear_calc(split_math_string[:left_index] + calc_part + split_math_string[right_index + 1:])
    elif '+' in split_math_string:
        operation_index = split_math_string.find('+')
        left_index, right_index = number_creator(operation_index, split_math_string)
        calc_part = str(int(split_math_string[left_index: operation_index]) +
                        int(split_math_string[operation_index+1: right_index+1]))
        return linear_calc(split_math_string[:left_index] + calc_part + split_math_string[right_index + 1:])
    elif '-' in split_math_string:
        operation_index = split_math_string.find('-')
        left_index, right_index = number_creator(operation_index, split_math_string)
        calc_part = str(int(split_math_string[left_index: operation_index]) -
                        int(split_math_string[operation_index+1: right_index+1]))
        return linear_calc(split_math_string[:left_index] + calc_part + split_math_string[right_index + 1:])
    else:
        return split_math_string


def number_creator(index, math_string):
    # print(math_string)
    left_index = index - 1
    right_index = index + 1
    while math_string[left_index - 1].isdigit():
        if left_index == 0:
            break
        left_index -= 1
    try:
        while math_string[right_index + 1].isdigit():
            if right_index == len(math_string) - 1:
                break
            right_index += 1
    except IndexError:
        return left_index, right_index
    return left_index, right_index
