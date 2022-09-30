import random
from HANG import words

# HANGMAN_PICS = ['''
#    +---+
#        |
#        |
#        |
#       ===''', '''
#    +---+
#    0   |
#        |
#        |
#       ===''', '''
#    +---+
#    0   |
#    |   |
#        |
#       ===''', '''
#    +---+
#    0   |
#   /|   |
#        |
#       ===''', '''
#    +---+
#    0   |
#   /|\  |
#        |
#       ===''', '''
#    +---+
#    0   |
#   /|\  |
#   /    |
#       ===''', '''
#    +---+
#    0   |
#   /|\  |
#   / \  |
#       ===''']
# words = '''аист акула бабуин баран барсук бобр бык варан верблюд волк вомбат воробей ворон выдра
# голубь гусь додо дятел енот ехидна еж жаба жираф журавль заяц зебра землеройка зяблик
# игуана кабан казуар кайман какаду кальмар камбала канарейка каракатица карп кенгуру
# киви кит лама ламантин ласка ласточка лебедь лев лемур ленивец леопард лиса лягушка
# мотылек муравьед муравей мангуст медведь морж муха мышь медуза нарвал носорог орел омар олень овцебык
# осьминог орел осел оса овца опоссум обезьяна паук пескарь пингвин пиранья попугай
# пчела рысь рыба росомаха страус сурок стрекоза сорока сова снегирь сокол собака слон
# слон скорпион скворец скат сельдь свинья сурикат скунс слизень светлячок тюлень тукан тигр
# трясогуска термит тетерев тунец тритон тарантул таракан тля утконос уж устрица улитка угорь фазан фламинго
# форель хорек хомяк хамелеон цапля цесарка цикада черепаха червь чайка шимпанзе шиншилла
# щука эму ящерица ястреб як ягуар'''.split() # split разбивает строку и делает список

# получаем случайное слово из списка

# print(words)
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLaters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLaters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:  # показывает секретное слово с пробелами
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    # возвращает букву введенную игроком и проверяет не введено ли ничего лишнего
    while True:
        print('Введите букву: ')
        guess = input()
        guess = guess.lower()
        ru = list(map(chr, range(1040, 1104)))  # изменил, обрати внимание
        ru_str = ''.join(str(x) for x in ru)

        if len(guess) != 1:
            print('Введите одну букву')
        elif guess in alreadyGuessed:
            print('Эту букву Вы уже называли. Введите другую')
        elif guess not in ru_str:
            print('Пожалуйста введите БУКВУ')
        else:
            return guess


def playAgain():
    # возвращает True при ответе
    print('Хотите сыграть еще раз? (да или нет)')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    # позволяет игроку ввести букву
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # проверка победы
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f'Да! секретное слово - {secretWord}! Победа!')
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess

        # проверка на превышение количества слов
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print(
                f'Вы исчерпали все попытки! Не угадано букв: {str(len(missedLetters))} и угадано букв:\n '  # ОБРАТИ ВНИМАНИЕ
                f'{str(len(correctLetters))}. Было загадано слово {secretWord}')
            gameIsDone = True

    # Запрашивает желание повторной игры
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)
            gameIsDone = False
        else:
            break
