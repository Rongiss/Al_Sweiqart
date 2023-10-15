import logging

# logging.disable(logging.CRITICAL)

logging.basicConfig(filename=r'test_DEBAG.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Начало программы')


def factorial(n):
    logging.debug(f'Начало factorial{n}')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i = {str(i)} total = {str(total)}')
    logging.debug(f'Конец factorial {n}')
    return total


print(factorial(10))
logging.debug('Конец программы')
