import webbrowser, pyperclip, sys


def open_page():
    if len(sys.argv) > 1:
        webbrowser.open(sys.argv[1])

    else:
        webbrowser.open(pyperclip.paste())


if __name__ == '__main__':
    open_page()
