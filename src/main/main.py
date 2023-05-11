from src.utils.utils import load_words_subwords, random_word_in_list
from class_Player.Player import Player
from class_BasicWord.BasicWord import BasicWord

WORDS_SUBWORDS = "https://www.jsonkeeper.com/b/2Y4S"


def main():
    load_words = load_words_subwords(WORDS_SUBWORDS)

    if load_words is None:
        print("ERROR 404")
        return

    random_word = random_word_in_list(load_words)
    basic_word = BasicWord(random_word.get('word'), random_word.get('subwords'))
    user_name = input('User name: ')
    player = Player(user_name)

    print(f'Hello {player.name_user}')
    print(f"Составьте {len(basic_word.subwords)} слова из слова '{basic_word.word}'")
    print("Слова должны быть не короче 3 букв")
    print("Чтобы закончить игру напишите stop")
    print("Поехали, ваше первое слово?")

    while len(basic_word.subwords) != len(player.use_word):
        user_word = input()
        if user_word in ['stop', 'cтоп']:
            print(f"Игра завершена, вы угадали {len(player.use_word)} слов из {len(basic_word.subwords)}")
            not_guess_subword = set(basic_word.subwords).difference(set(player.use_word))
            print(f"Вы не угадали следующие слова: {', '.join(not_guess_subword)}")
            return

        elif len(user_word) < 3:
            print('Слишком короткое')
            continue

        elif user_word in player.use_word:
            print("Слово уже использовано")
            continue

        elif not basic_word.check_subwords(user_word):
            print('Такого слова нет')

        else:
            player.use_user_word(user_word)
            print("Верно")


if __name__ == '__main__':
    main()
