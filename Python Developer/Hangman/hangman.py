from random import randint


def output_word(correct_word, letters):
    result_word = ''

    for letter in correct_word:
        if letter in letters:
            result_word += letter
        else:
            result_word += '-'

    return result_word


def check_input(input_word):
    if len(input_word) > 1 or len(input_word) > 1 == 0:
        print('You should input a single letter\n')
        return False

    if not input_word.isalpha() or not input_word.islower():
        print('Please enter a lowercase English letter\n')
        return False

    return True


print("H A N G M A N", end='\n')

while True:
    command_input = input('Type "play" to play the game, "exit" to quit: ')
    if command_input == 'play':
        print('')

        list_words = ['python', 'java', 'kotlin', 'javascript']
        word = list_words[randint(0, 3)]
        user_letters = []
        lives = 8

        while True:
            output = output_word(word, user_letters)
            print(output)
            user_input = input("Input a letter: ")

            if not check_input(user_input):
                continue

            if user_input in user_letters:
                print("You've already guessed this letter", end='\n\n')
            elif user_input not in word:
                print("That letter doesn't appear in the word")
                lives -= 1
                if lives == 0:
                    print('You lost!')
                    break
                else:
                    print('')
            else:
                print()

            user_letters.append(user_input)

            if output_word(word, user_letters) == word:
                print(word)
                print('You guessed the word!')
                print('You survived!')
                break
    elif command_input == 'exit':
        break

