import random

word_bank = ['stellar', 'quick', 'bumblebee', 'github', 'indonesia']

word = random.choice(word_bank)

guessWord = ['_'] * len(word)
attemps = 10

while attemps > 0 :
    print('\nCurrent word: ' + ' '.join(guessWord))
    guess = input('Guess a letter : ').lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessWord[i] = guess
        print('Great guess!')
    elif len(guess) == 2:
        print('Guess with only one letter!! \nEx : \'n\' or \'m\'')
    else:
        attemps -= 1
        print('Wrong guess! Attempts left: ' + str(attemps))
    if '_' not in guessWord :
        print('\nCongratulations!! You guess the word: ' +  word)  
        break
    if attemps == 0 and '_' in guessWord:
        print('\nYou\'ve run out of attempts!! The word was: ' + word)

