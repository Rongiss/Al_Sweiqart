import pyinputplus as pyip


def test():
    aa = ['cat', 'dog', 'bird']
    try:
        a = pyip.inputMenu(aa, numbered=True, timeout=20)
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
