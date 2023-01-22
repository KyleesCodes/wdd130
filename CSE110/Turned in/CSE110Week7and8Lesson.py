from typing import Counter

print('')
print("Welcome to Kylee's word guessing game!\n")

secret_word = "love"
total_letters = len(secret_word)

hint = '_ ' * total_letters
print(f'Your hint is {hint}.')

counter = 0

secret_guess = None
while secret_guess != secret_word.lower():
    secret_guess = input("\nWhat is your guess? ")
    guess_len = len(secret_guess)
    counter+=1 
    if guess_len == total_letters:
        print("Your hint is: ")
        for i in range(total_letters):
            letter=secret_guess[i]
            secret_letter=secret_word[i]
            if letter==secret_letter:
                print(letter.upper(), end=' ')
            elif letter in secret_word:
                print(letter.lower(),end=' ')
            else:
                print("_",end=' ')
    else:
        print('')
        print('The guess length does not match the hint length.')
print('')
print('Congratulations!')

if counter <= 1:
   print(f'It took you {counter} guess!')
else:
   print(f'It took you {counter} guesses!')