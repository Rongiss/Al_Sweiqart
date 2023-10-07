import pyinputplus as pyip


def test():
    try:
        a = pyip.inputMenu(['cat', 'dog', 'bird'], numbered=True, timeout=2)
        match a:
            case 'cat':
                print('cat lal')
            case 'dog':
                print('dog --- ')
            case 'bird':
                print('bird -- === ')
            case 'end':
                print('end')
    except pyip.TimeoutException:
        print('Timeout')
    except pyip.RetryLimitException:
        print('blabla')


if __name__ == '__main__':
    test()
