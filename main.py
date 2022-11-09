from backward_translation import translate
from translation import extract_tokens
from compilation import compile
from utils import compose

calc = compose(translate, compile, extract_tokens)

if __name__ == '__main__':
    text = 'косинус от сто сорок два и триста тридцать три тысячных в степени четырнадцать и сто пятьдесят пять'
    print(text)
    print(calc(text))
