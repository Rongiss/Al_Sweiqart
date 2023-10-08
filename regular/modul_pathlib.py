import pathlib, sys, os, shelve


def main():
    a = pathlib.Path('spam') / ('bacon') / ('eggs')
    print(a)
    print(pathlib.Path.cwd())
    print(pathlib.Path.home())
    try:
        os.mkdir('bbb')
    except FileExistsError:
        pass
    a = os.system('ls')
    print(type(a))


def work_shelve():
    file_shelve = shelve.open('myfile')
    lst = ['cat', 'cat2', 'cat3']
    file_shelve['cats'] = lst
    file_shelve.close()
def open_file_shelve():

    try:
        shelve_file = shelve.open('myfile')
        a = shelve_file['cats']
        print(a)
        shelve_file.close()
    except FileNotFoundError:
        pass

if __name__ == '__main__':
    # main()
    open_file_shelve()
    work_shelve()
