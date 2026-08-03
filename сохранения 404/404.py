import random

her = ['dusk-сумерки','dawn-рассвет','morning-утро','noon-полночь','afternoon-время после полудня до вечера',
'evening-вечер','night-ночь','middle-середина','midnight-полночь','half-половина','quarter-четверть'
,'past-прошедшее','a.m-дневное время','p.m-ночное время','(имя:сущ,2пере-да)fall-падать,осень','last-последний',
'next-следующий','this-этот','ago-спустя','buy-купить','new-новый','call-вызывать','day-день',
'week-неделя','weekend-выходные','monday-понидельник','tuesday-вторник','wednsday-среда','thursday-четверг'
,'friday-пятница','saturday-суббота','sunday-воскресенье','year-год','month-месяц','winter-зима'
,'december-декабрь','junuary-январь','february-февраль','spring-весна','march-март','april-апрель',
'may-май','summer-лето','june-июнь','july-июль','autumn-осень','september-сентябрь',
'october-октябрь','november-ноябрь','on-на','ubder-под','behind-позади',
'in front of-перед','of-чего','near-рядом','next to-следующий','over-над','above-выше'
,'along-вдоль','among-среди','between-середина','magical-волшебный','head-голова'
,'hat-шляпа','magic-волшебство','street-улица','bird-птица','bolow-ниже','next-следующий'
,'opposite-противополжный','roof-крыша','flor-пол','way-путь','lose-терять'
,'unusual-необычный','always-всегда','yesterday-вчера','tomorrow-завтра'
,'today-сегодня','never-никогда','feel-чувствовать',"let's-давай",'let-позволять'
,'think-думать','come-подходить','come back-возврощатся','question-вопрос'
,'what-что','where-где','when-когда','why-почему','who-кто','how-как','whoese-чей'
,'do-делать','like-нравится','drink-пить','matter-иметь значение','live-жить'
,'leave-покидать','knowe-знать', 'in-в ','at-рядом ','even-даже', 'with you-с тобой'
, 'because-потому что', 'crowd-толпа', 'crowded-толпа', 'from-от', 'to-к', 'there-там'
, 'these-эти', 'those-те', 'that-что', 'attractive-привлекательный', 'difficult-трудный'
, 'incredible-невероятный', 'fascinating-очаровательный', 'honest-честный',
'sure-конечно', 'belive-верить', 'need-нуждатся', 'attract-привлекать', 'amaze-удивлять',
'mind-разум', 'than-чем', 'more-более', 'most-большинство', 'as-как', 'tired-усталый',
'fame-слава', 'enough-достаточно', 'probably-вероятно','can-может','for-для',
'answer-отвечать', 'awesome-потрясающий', 'again-снова', 'look for-искать',
'all-все', 'till-до', 'make-делать', 'breakfast-завтрак', 'dinner-обед,ужин',
'lunch-полдник,обед', 'supper-ужин', 'funny-весёлый', 'fun-веселье', 'image-картинка',
'imagine-вооброжать', 'forest-лес', 'fascinating-плентиельный', 'wonder-удивляться',
'bring-приносить', 'soup-суп','bathroom-ванная'] # словарь английских слов

choise = input('Выберите одно из двух "проверка на повторение" или "отгадывать слова": ').lower()
if choise == 'проверка на повторение':
    eng = input('Введите слово для проверки на повтор: ')
    if eng in her:
        print('Повторение слова')
    else:
        print('Такого слова нету!')
DI = input('Хотите ли вы  увидеть все слова в словаре? Yes/No :').title()
N = 0
if 'Yes'in DI:
    print('')
    for i in her:
        N += 1
        print(N, i,'\n--------')

else:
    while True:
        rand_dom = random.choice(her)
        rand = rand_dom.split('-')[0]
        print(rand)
        Gess_the_word = input('напиши перевод на руссском пример"-яблоко"').lower()
        word = (rand + Gess_the_word)
        if word in her:
            print('Верно!')
            print('')
        else:
            print('')
            print('Не верно! Правильный перевод: ',rand_dom)
#-----------------------------------------------------------------------------------------------------------
import random
import json

# Словарь вместо списка
WORDS = {
    "dusk": "сумерки",
    "dawn": "рассвет",
    # ... остальные пары
}

def show_all_words():
    for i, (eng, rus) in enumerate(WORDS.items(), 1):
        print(f"{i}. {eng} – {rus}")

def check_duplicate(word):
    return word in WORDS

def guess_game():
    print("Игра: угадайте перевод английского слова")
    while True:
        eng = random.choice(list(WORDS.keys()))
        print(f"Слово: {eng}")
        user_input = input("Ваш перевод (или 'выход' для завершения): ").strip().lower()
        if user_input in ("выход", "exit"):
            break
        correct = WORDS[eng].lower()
        if user_input == correct:
            print("Верно!\n")
        else:
            print(f"Неверно! Правильный перевод: {WORDS[eng]}\n")

def main():
    while True:
        choice = input("Выберите действие:\n1 - Проверка на повторение\n2 - Отгадывать слова\n3 - Показать все слова\n4 - Выйти\n> ").strip()
        if choice == "1":
            word = input("Введите английское слово: ").strip().lower()
            if check_duplicate(word):
                print("Такое слово уже есть в словаре.")
            else:
                print("Слова нет в словаре.")
        elif choice == "2":
            guess_game()
        elif choice == "3":
            show_all_words()
        elif choice == "4":
            break
        else:
            print("Некорректный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()