import random

capitals = {'Айдахо': 'Бойсе', 'Айова': 'Де-Мойн', 'Алабама': 'Монтгомери', 'Аляска': 'Джуно', 'Аризона': 'Финикс',
            'Арканзас': 'Литл-Рок', 'Вайоминг': 'Шайенн', 'Вашингтон': 'Олимпия', 'Вермонт': 'Монтпилиер',
            'Виргиния': 'Ричмонд', 'Висконсин': 'Мадисон', 'Гавайи': 'Гонолулу', 'Делавэр': 'Довер',
            'Джорджия': 'Атланта', 'Западная Виргиния': 'Чарлстон', 'Иллинойс': 'Спрингфилд',
            'Индиана': 'Индианаполис',
            'Калифорния': 'Сакраменто', 'Канзас': 'Топика', 'Кентукки': 'Франкфорт', 'Колорадо': 'Денвер',
            'Коннектикут': 'Хартфорд', 'Луизиана': 'Батон-Руж', 'Массачусетс': 'Бостон', 'Миннесота': 'Сент-Пол',
            'Миссисипи': 'Джэксон', 'Миссури': ' Джефферсон-Сити', 'Мичиган': 'Лансинг', 'Монтана': 'Хелена',
            'Мэн': 'Огаста', 'Мэриленд': 'Аннаполис', 'Небраска': 'Линкольн', 'Невада': 'Карсон-Сити',
            'Нью-Джерси': 'Трентон', 'Нью-Йорк': 'Олбани', 'Нью-Мексико': 'Санта-Фе', 'Нью-Гэмпшир': 'Конкорд',
            'Огайо': 'Колумбус', 'Оклахома': 'Оклахома-Сити', 'Орегон': 'Сейлем', 'Пенсильвания': 'Гаррисберг',
            'Род-Айленд': 'Провиденс', 'Северная Дакот': 'Бисмарк', 'Северная Каролина': 'Роли', 'Теннесси': 'Нашвилл',
            'Техас': 'Остин', 'Флорида': 'Таллахасси', 'Южная Дакота': 'Пирр', 'Южная Каролина': 'Колумбия',
            'Юта': 'Солт-Лейк-Сити'}

for quizNum in range(35):
    # СДЕЛАТЬ: создать файлы билетов и ключей ответов
    quizFile = open(f'capitalsquiz_{quizNum + 1}.txt', 'w')
    # СДЕЛАТЬ: записать заголовок билета
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')
    # СДЕЛАТЬ: перемешать порядок следования штатов
    quizFile.write('Имя:\n\nДата:\n\nГруппа:\n\n')
    quizFile.write((' ' * 20) + f'Столицы штатов(билет {quizNum + 1})')
    quizFile.write('\n\n')
    # СДЕЛАТЬ: организовать цикл по всем 50 штатам, создавая вопрос для каждого из них
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        quizFile.write(f'{questionNum + 1}. Выберите столицу штата {states[questionNum]}.\n')
        for i in range(4):
            quizFile.write(f"\t{'АБВГ'[i]}. {answerOptions[i]}\n")
            # quizFile.write('\n')
            # Запись ключа ответа в файл
            answerKeyFile.write(f'{questionNum + 1}.{"АБВГ"[answerOptions.index(correctAnswer)]}\n')

quizFile.close()
answerKeyFile.close()
