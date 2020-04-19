#TODO: vetor de letras já encontradas, pra mesma letra n contar como dois pontos
#TODO: checar se a letra encontrada é repetida

def play_hang_man():
    errors = 0
    right_letters = 0

    print("#### Hang Man ####")
    word_to_guess = input("Input single word: ")
    while not validate_input(word_to_guess):
        word_to_guess = input("Input valid word (no numbers or spaces): ")

    n_letters = len(word_to_guess)
    max_errors = n_letters
    guess_vector = [None]*n_letters
    guess_vector = ['_' for i in range(0,n_letters)]

    while (errors < max_errors and right_letters < n_letters):
        print_iteration(guess_vector, [errors, max_errors, right_letters, n_letters])
        letter_to_guess = input('Try a letter: ')
        check = check_letter(word_to_guess, letter_to_guess)
        [errors, right_letters, guess_vector] = iteration_result(check, letter_to_guess, [errors, right_letters, guess_vector])
    if errors >= max_errors:
        print('Too bad :T')
        return 'Too bad :T'
    else:
        [print(i, end='') for i in guess_vector]
        print('\n Got it!')
        return 'Got it!'

def validate_input(input_word):
    if input_word.find(' ') > 0:
        return False
    elif any(i.isdigit() for i in input_word):
        return False
    return True

def check_letter(word_to_guess, letter_to_guess):
    return word_to_guess.find(letter_to_guess)

def iteration_result(check, letter, list):
    [errors, right_letters, guess_vector] = list
    if check < 0:
        return [errors+1,right_letters,guess_vector]
    else:
        guess_vector[check] = letter
        return [errors,right_letters+1,guess_vector]

def print_iteration(guess_vector,list):
    [errors, max_errors, right_letters, n_letters] = list
    print('Erros: ',errors,'/',max_errors,'; letters: ',right_letters,'/',n_letters)
    for i in guess_vector:
        print(i, end=' ')
    print('\n')

if __name__ == '__main__':
    play_hang_man()
