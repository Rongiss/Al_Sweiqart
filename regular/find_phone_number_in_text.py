import re, pyperclip


def get_number_phone_in_text(text: str):
    or_phone = re.compile(r'\d{3}-\d{3}-\d{4}')
    phone = or_phone.search(text)
    print('Найден номер телефна -', phone.group())


def get_number_phone_in_text_with_group(text: str):
    or_phone = re.compile(r'(\d{3})-(\d{3}-\d{4})')
    phone = or_phone.search(text)
    kod, number = phone.groups()
    print(f'Найден номер телефна - код {kod} номер {number}')


def get_number_phone_in_text_with_group_2(text: str):
    or_phone = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
    phone = or_phone.search(text)
    kod, number = phone.groups()
    print(f'Найден номер телефна - код {kod} номер {number}')


### Chanal | or pipe in ragular###

def find_wirh_pipe(text: str):
    find_str_Regex = re.compile(r'Бэтмен|Тина Фей')
    result = find_str_Regex.search(text)
    print(result.group())


def find_wirh_pipe_more(text: str):
    find_str_Regex = re.compile(r'Бэт(мен|мобиль|коптер|бэт)')
    result = find_str_Regex.search(text)
    print(result.group())

    # with '?'


def find_wirh_pipe_more_2(text: str):
    find_str_Regex = re.compile(r'Бэт(ву)?мен')
    result = find_str_Regex.search(text)
    print(result.group())


def find_wirh_pipe_more_3(text: str):
    find_str_Regex = re.compile(r'Бэт(ву)*мен')
    result = find_str_Regex.search(text)
    print(result.group())


def find_wirh_pipe_more_4(text: str):
    find_str_Regex = re.compile(r'Бэт(ву)+мен')
    result = find_str_Regex.search(text)
    print(' Нет результатов ' if result == None else result.group())

def class_regular(text: str):
    cl = re.compile(r'[abcd]')
    result = cl.findall(text)
    print(result)

def test():
    a = str(pyperclip.paste())
    print(a)
    pyperclip.copy(a.upper())



if __name__ == '__main__':
    # get_number_phone_in_text(
    #     '''Позвони мне завтра по номеру 415-555-1011. 415-555-9999 - это номер телефона моего офиса.''')
    # get_number_phone_in_text_with_group('''Позвони мне завтра по номеру 415-555-1011. (415) 555-9999 - это номер телефона моего офиса.''')
    # get_number_phone_in_text_with_group_2(
    #     '''Позвони мне завтра по номеру 415-555-1011. (415) 555-9999 - это номер телефона моего офиса.''')
    # find_wirh_pipe('Бэтмен и Тина Фей.')
    # find_wirh_pipe_more('Бэтмобиль потерял колесо')
    # find_wirh_pipe_more_2('Мой герой - Бэтмен')
    # find_wirh_pipe_more_2('Моя героиня - Бэтвумен')
    # find_wirh_pipe_more_3('Моя героиня - Бэтвувувувумен')
    # find_wirh_pipe_more_4('Моя героиня - Бэтвувувувумен')
    # find_wirh_pipe_more_4('Мой герой - Бэтмен')
    # class_regular('asdfkkjdfg[awsdjdsc')
    test()