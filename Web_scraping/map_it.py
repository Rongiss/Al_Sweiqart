import webbrowser, pyperclip, sys, requests


def open_page() -> None:
    """

    :return:
    """
    if len(sys.argv) > 1:
        webbrowser.open(sys.argv[1])

    else:
        webbrowser.open(pyperclip.paste())


def request_page() -> None:
    """

    :return:
    """
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    res.raise_for_status()
    play_file = open('RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100000):
        play_file.write(chunk)
    play_file.close()


if __name__ == '__main__':
    request_page()
    print('done')
