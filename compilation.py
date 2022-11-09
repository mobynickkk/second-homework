from math import sin, cos, tan
from typing import List, Collection

from utils import tail_recursion


def compile(tokens: List[str]) -> float:
    expression = ''.join(compile_tokens(tokens))
    if '(' in expression:
        expression += ')'
    return eval(expression, {'sin': sin, 'cos': cos, 'tan': tan})


@tail_recursion
def compile_tokens(tokens: List[str], position: int = 0, result: Collection[str] = ()) -> List[str]:
    if position == len(tokens):
        return list(result)
    return compile_tokens.call(tokens, position + 1, add_result(result, tokens[position]))


def add_result(result: Collection[str], token: str):
    if token.isdigit() and len(result) > 1 and result[-1] == '.':
        return list(result[:-2]) + [result[-2] + result[-1] + token]
    return list(result) + [token]

