import logging
# logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def test(n):
    logging.info('Start programm')
    for i in range(1, 10):
        n *= i
        logging.info(f'n = {n} i = {i} total = {n}')
    logging.info('Finish')
    # print(n)


if __name__ == '__main__':
    test(7)
