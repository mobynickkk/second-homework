from utils import compose, tail_recursion, numbers

reversed_numbers_before_dot = dict()
reversed_numbers_after_dot = dict()

for i in numbers:
    if not any([numbers[i] == num for num in reversed_numbers_before_dot.keys()]):
        reversed_numbers_before_dot[numbers[i]] = i

for i in reversed(numbers):
    if not any([numbers[i] == num for num in reversed_numbers_after_dot.keys()]):
        reversed_numbers_after_dot[numbers[i]] = i


postfix = {
    1: 'десятых',
    2: 'сотых',
    3: 'тысячных'
}


get_string_value = compose(str, lambda x: round(x, 3))


def translate(value: float) -> str:
    return read_value(*get_string_value(value).split('.'))


def read_value(value_before_dot: str, value_after_dot: str) -> str:
    if len(value_after_dot) == 0:
        return read_int_value(value_before_dot)
    return read_int_value(value_before_dot) + 'и ' + read_int_value(value_after_dot, True) + postfix[len(value_after_dot)]


@tail_recursion
def read_int_value(value: str, isafterdot: bool = False, position: int = 0, result: str = ''):
    if position == len(value):
        return result
    if isafterdot and value[position] == '0':
        return read_int_value(value, isafterdot, position + 1, result)
    return read_int_value(value, isafterdot, position + 1,
                          result + get_translated_int_value(
                              (int(value[position]) * 10 ** (len(value) - position - 1)), isafterdot) + ' ')


def get_translated_int_value(value: int, isafterdot: bool):
    if isafterdot:
        return reversed_numbers_after_dot[value]
    return reversed_numbers_before_dot[value]
