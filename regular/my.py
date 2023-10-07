import re, pyperclip


def finding_word_intext() -> str:
    """
    функция принимает и возвращает слово для поиска в тексте
    :return:
    """
    return input('Ввкдите слово для поиска в тексте')


def inside_text() -> str:
    """
    функция получает текст из буфера обмена для дальнейшего поиска необходимого слова
    :return:
    """
    input("Скопируйте текст ипросто нажмите ввод")
    text = str(pyperclip.paste())
    return text


def find_word_in_text():
    """
    функция выводит на экра список найденных слов
    :return:
    """
    a = finding_word_intext()
    heroRegex = re.compile(a)
    text = inside_text()
    mo = heroRegex.findall(text)
    print(mo)


if __name__ == '__main__':
    # find_word_in_text('Бэтмен и Тина Фей.')
    # inside_text()
    find_word_in_text()
