"""

Шифр Цезаря заключается в замене каждого символа входной строки на символ, находящийся на несколько позиций левее или правее его в алфавите.

Для всех символов сдвиг один и тот же. Сдвиг циклический, т.е. если к последнему символу алфавита применить единичный сдвиг, то он заменится на первый символ, и наоборот.

Напишите программу, которая шифрует текст шифром Цезаря.

Используемый алфавит − пробел и малые символы латинского алфавита: ' abcdefghijklmnopqrstuvwxyz'

Формат ввода:
На первой строке указывается используемый сдвиг шифрования: целое число. Положительное число соответствует сдвигу вправо. На второй строке указывается непустая фраза для шифрования. Ведущие и завершающие пробелы не учитывать.

Формат вывода:
Единственная строка, в которой записана фраза: Result: "..." , где вместо многоточия внутри кавычек записана зашифрованная последовательность.

Sample Input 1:

3
i am caesar
Sample Output 1:

Result: "lcdpcfdhvdu"
Sample Input 2:

-2
az
Sample Output 2:

Result: "zx"
Sample Input 3:

27
abc
Sample Output 3:

Result: "abc"
"""

import sys


def main():
    reader = (line for line in sys.stdin)
    d, fraze = int(next(reader)), next(reader).strip()
    s = ' abcdefghijklmnopqrstuvwxyz'
    alphabet = {s[index]:index for index in range(len(s))}
    result = ''
    length = len(alphabet)
    for symbol in fraze:
        result += s[(alphabet[symbol] + d)%length]
    print('Result: \"%s\"' % result)


if __name__ == '__main__':
    main()
    
