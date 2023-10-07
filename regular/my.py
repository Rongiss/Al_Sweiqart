import re, pyperclip

def inside_text():
    text = str(pyperclip.paste())
    print(text)

def find_word_in_text(text):
    a = r'Бэтмен|Тина Фей'
    heroRegex = re.compile(a)
    mo = heroRegex.findall(text)
    print(mo)


if __name__ == '__main__':
    find_word_in_text('Бэтмен и Тина Фей.')
    # inside_text()