import pyinputplus as pyip


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


if __name__ == '__main__':
    main()
