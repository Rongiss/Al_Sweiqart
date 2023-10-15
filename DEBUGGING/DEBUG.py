import traceback
def box_print(symbol, width, heigth):
    # print(len(symbol))
    if len(symbol) != 1:
        raise Exception('Переменная symbol должна содержать один символ.')
    if width <= 2:
        raise Exception('Значение width должно превышать 2.')
    if heigth <= 2:
        raise Exception('Значение heigth должно превышать 2.')
    print(symbol * width)
    for i in range(heigth - 2):
        print(symbol, ' ' * (width - 2), symbol, sep='')
    print(symbol * width)


if __name__ == '__main__':
    for sym, w, h in (('*', 4, 4), ('#', 20, 5), ('x', 1, 3)):
        try:
            box_print(symbol=sym, width=w, heigth=h)
        except Exception as err:
            error_file = open('error_info.txt', 'w')
            error_file.write(traceback.format_exc())
            error_file.close()
            print('Данные об ошибке занесены в файл')
            # print(f'Возникло исключение: {str(err)}')
