from random import randint
from art import logo

easy_level_turns = 10
hard_level_turns = 5
Turns = 0
def check_answer(answer,guess,turns):
    if guess>answer:
        print("too high!")
        return turns-1
    elif guess<answer:
        print("too low!")
        return turns-1
    else:
        print("you guessed it right!")

def set_difficulty():
    diff=input("choose your difficulty. type 'easy' or 'hard'")
    if diff == "easy":
        return easy_level_turns
    if diff == "hard":
        return hard_level_turns


def play_games():
    print(logo)
    print("welcome to the number guessing game!")
    print("i am thinking of number between 1 to 100!")
    answer = randint(1,100)
    guess = 0
    turns = set_difficulty()
    while guess!=answer:
        print(f"you have {turns} remaining!")
        guess = int(input("make a guess\n"))
        turns = check_answer(answer,guess,turns)
        if turns==0:
            print("sorry! you ran out of turns. GAME OVER!")
        if guess!=answer:
            print("guess again")
play_games()


