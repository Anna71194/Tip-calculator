import random

def random_generator():
    computer=random.randint(1,1000)
    get_guess(computer)

def get_guess(computer):
    guess= int(0)
    counter=int(0)
    while guess != computer:
        try:
            guess=input('Guess a number between 1 and 1000: ')
            guess=int(guess)
            counter = counter+1
        except ValueError:
            print("Im sorry, the value you entered was not a number i recognize, try again")
            continue
        if guess > 1000:
            print('Your guess is over 1000, the range is 1 - 1000, try again')
        elif guess > computer:
            print('Sorry, your guess is too high')
            counter = counter+1
        elif guess < computer:
            print('Sorry your guess is too low')
            counter = counter+1
    win_game(computer, guess, counter)
def win_game(computer, guess, counter):
        print('Thank you for playing you won! The number was {} and it took you {} guesses to win!' .format(computer,counter))


random_generator()
        
