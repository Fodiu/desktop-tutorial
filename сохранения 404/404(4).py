import sounddevice as sd
from pykokoro import KokoroPipeline, PipelineConfig
import random
from dictionary import WORDS  # предполагается, что файл dictionary.py лежит рядом

pipe = KokoroPipeline(PipelineConfig(voice="af_bella"))

def speak_word(word):
    try:
        result = pipe.run(word)
        sd.play(result.audio, result.sample_rate)
        sd.wait()
    except Exception as e:
        print(f"⚠️ Ошибка озвучки: {e}")
        
def show_all_words():
    """Выводит все слова из словаря с нумерацией."""
    if not WORDS:
        print("Словарь пуст!")
        return
    for i, (eng, rus) in enumerate(WORDS.items(), 1):
        print(f"{i}. {eng} – {rus}")

def check_duplicate(word):
    """Проверяет, есть ли слово в словаре."""
    return word in WORDS

def guess_game():
    """Режим угадывания: ввод перевода с клавиатуры."""
    if not WORDS:
        print("Словарь пуст! Добавьте слова.")
        return

    correct_count = 0
    wrong_count = 0
    all_words = list(WORDS.keys())  # один раз создаём список

    print("\n=== Угадай перевод ===")
    print("Вам показывают английское слово, вы вводите перевод.")
    print("Для выхода введите 'выход'.\n")

    while True:
        eng = random.choice(all_words)
        speak_word(eng)
        print(f"Английское слово: {eng}")
        user_input = input("Ваш перевод: ").strip().lower()
        if user_input in ("выход", "exit"):
            print("\n--- Статистика ---")
            print(f"✅ Правильно: {correct_count}")
            print(f"❌ Неправильно: {wrong_count}")
            print("------------------")
            break

        # Получаем правильный перевод (может быть несколько через запятую)
        correct_translations = [t.strip().lower() for t in WORDS[eng].split(',')]
        if user_input in correct_translations:
            correct_count += 1
            print("✅ Верно!\n")
        else:
            wrong_count += 1
            print(f"❌ Неверно! Правильный перевод: {WORDS[eng]}\n")

def pick_a_word():
    """Режим выбора правильного английского слова из нескольких вариантов."""
    if not WORDS:
        print("Словарь пуст! Добавьте слова.")
        return
    if len(WORDS) < 3:
        print("В словаре меньше трёх слов — режим недоступен.")
        return

    print("\n=== Выбери правильный перевод ===")
    print("Вам показывают русское слово, выберите английский вариант из трёх.")
    print("Для выхода введите 'выход'.\n")

    all_words = list(WORDS.keys())
    correct_count = 0
    wrong_count = 0

    while True:
        correct_eng = random.choice(all_words)
        correct_rus = WORDS[correct_eng]

        # Формируем варианты (всегда 3)
        options = [correct_eng]
        # Берём два случайных других слова
        other_words = [w for w in all_words if w != correct_eng]
        options.extend(random.sample(other_words, 2))
        random.shuffle(options)

        print(f"Перевод: '{correct_rus}'")
        print("Выберите правильный английский вариант:")
        for i, eng in enumerate(options, start=1):
            print(f"  {i}. {eng}")

        user_input = input("Ваш выбор (номер 1-3) или 'выход': ").strip().lower()
        if user_input in ("выход", "exit"):
            print("\n--- Статистика ---")
            print(f"✅ Правильно: {correct_count}")
            print(f"❌ Неправильно: {wrong_count}")
            print("------------------")
            break

        if not user_input.isdigit() or int(user_input) not in range(1, 4):
            print("⚠️  Пожалуйста, введите число 1, 2 или 3.\n")
            continue

        chosen_index = int(user_input) - 1
        chosen_eng = options[chosen_index]

        if chosen_eng == correct_eng:
            correct_count += 1
            print("✅ Правильно! Молодец!\n")
        else:
            wrong_count += 1
            print(f"❌ Неверно! Правильный ответ: {correct_eng}\n")

def main():
    """Главное меню программы."""
    while True:
        print("\n" + "=" * 40)
        print("ГЛАВНОЕ МЕНЮ")
        print("=" * 40)
        print("1. Проверить слово на повторение")
        print("2. Угадать перевод (ввод с клавиатуры)")
        print("3. Угадать перевод (выбор из трёх вариантов)")
        print("4. Показать все слова")
        print("5. Выход")
        print("=" * 40)

        choice = input("Ваш выбор: ").strip()
        if choice == "1":
            word = input("Введите английское слово: ").strip().lower()
            if check_duplicate(word):
                print("✅ Такое слово уже есть в словаре.")
            else:
                print("❌ Слова нет в словаре.")
        elif choice == "2":
            guess_game()
        elif choice == "3":
            pick_a_word()
        elif choice == "4":
            show_all_words()
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("⚠️  Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
