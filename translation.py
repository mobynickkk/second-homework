from typing import List, Tuple

from utils import tail_recursion, numbers


class TranslationResult:
    """Структура для хранения результатов перевода в токены"""

    def __init__(self, tokens=(), processing_number: bool = False):
        self.tokens = list(tokens)
        self.processing_number = processing_number


def extract_tokens(expression: str) -> List[str]:
    words = expression.split(' ')
    return words2tokens(words)


@tail_recursion
def words2tokens(words: List[str], result: TranslationResult = TranslationResult()) -> List[str]:
    if not words:
        return result.tokens
    return words2tokens.call(*process_word(words, result))


def process_word(words: List[str], result: TranslationResult) -> Tuple[List[str], TranslationResult]:
    if not words:
        return words, result
    match words[0]:
        case 'в':
            return get_actual_words(words), result
        case 'на':
            return get_actual_words(words), result
        case 'от':
            return get_actual_words(words), result
        case 'синус':
            return add_result_token(words, result, 'sin(')
        case 'косинус':
            return add_result_token(words, result, 'cos(')
        case 'тангенс':
            return add_result_token(words, result, 'tan(')
        case 'степени':
            return add_result_token(words, result, '**')
        case 'плюс':
            return add_result_token(words, result, '+')
        case 'минус':
            return add_result_token(words, result, '-')
        case 'умножить':
            return add_result_token(words, result, '*')
        case 'разделить':
            return add_result_token(words, result, '/')
        case 'и':
            return add_result_token(words, result, '.')
        case x if is_number(x):
            return add_result_token(words, result, x, True)
        case x if x in ['десятых', 'сотых', 'тысячных']:
            return get_actual_words(words), result
        case y:
            raise Exception("Неизвестная команда" + y)


def add_result_token(words: List[str],
                     result: TranslationResult,
                     token: str,
                     isdigit: bool = False) -> Tuple[List[str], TranslationResult]:
    if isdigit and result.processing_number:
        return get_actual_words(words), TranslationResult(
            [str(int(tkn) + int(numbers[token])) if i == len(result.tokens) - 1 else tkn for i, tkn in enumerate(result.tokens)],
            True)
    return get_actual_words(words), TranslationResult(result.tokens + [str(numbers[token]) if isdigit else token], isdigit)


def get_actual_words(words: List[str]) -> List[str]:
    if len(words) < 2:
        return []
    return words[1:]


def is_number(word: str) -> bool:
    return any([word == num for num in numbers.keys()])
