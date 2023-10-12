import time

import pyinputplus as pyip
import random


def main():
    """
    daraka check function
    :return:
    """
    while True:
        pr = 'Хотите узнать, как занять дурака на несколько часов?\n'
        result = pyip.inputYesNo(pr, yesVal='да', noVal='нет')
        if result == 'нет':
            print('Спасибо! Желаю хорошего дня.')
            break


def multiplication_check():
    """
    multiplication test with a specified number of questions
    :return:
    """
    correctAnswers = 0
    how_many_tests = pyip.inputInt(prompt='Введите количество тестов: ')
    for i in range(1, how_many_tests + 1):
        num_1 = random.randint(0, 10)
        num_2 = random.randint(0, 10)
        promt = f'{i}) {num_1} * {num_2} = '
        try:
            pyip.inputStr(promt, allowRegexes=['^%s$' % (num_1 * num_2)], blockRegexes=[('.*', 'Неправильно!')],
                          timeout=8, limit=3)
        except pyip.TimeoutException:
            print('Time out')
        except pyip.RetryLimitException:
            print('kdkk')
        else:
            correctAnswers += 1
            time.sleep(1)
    print(f'Количество верных ответов - {correctAnswers}')


if __name__ == '__main__':
    # main()

    multiplication_check()
