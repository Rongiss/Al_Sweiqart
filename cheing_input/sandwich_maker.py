import pyinputplus as pyip


def sandwich_maker():
    burger_ingridients = {
        'types_of_bread': {'mass': 'Tип хлеба\n', 'цельнозерновой': 1.4, 'белый': 1.2, 'ржаной': 1.0},
        'types_of_protein_product': {'mass': 'Tип белкового продукта:\n', 'курица': 5, 'индейка': 7, 'ветчина': 6.5,
                                     'тофу': 10},
        'types_of_cheese': {'mass': 'Tип сыра\n', 'чеддер': 5, 'швейцарский': 10, 'моцарелла': 7.5}}
    dopings = {'майонез': 0.35, 'горчицa': 1, 'салат': 2, 'помидор': 1.5}

    out_burger = dict()
    for ing in burger_ingridients.values():
        ww = pyip.inputMenu(list(ing.keys())[1:], default=list(ing.keys())[1], numbered=True,
                            prompt=ing['mass'])
        out_burger[ww] = ing[ww]
    for doping in dopings.keys():
        res = pyip.inputYesNo(prompt=f'Вы хотите добавть {doping}?\n', yesVal=r'да', noVal='нет', default='нет')
        if res == 'да' or res == 'д':
            out_burger[doping] = dopings[doping]
        else:
            continue
    how_many = pyip.inputInt(prompt='Сколько бургеров приготовить?\n', min=1, )
    print(f'Итовая сумма - {sum(out_burger.values()) * how_many}')


if __name__ == '__main__':
    sandwich_maker()
