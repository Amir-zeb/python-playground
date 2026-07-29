import random
from typing import Literal

CHOICES: tuple[Literal["heads"], Literal["tails"]] = ("heads", "tails")
CHOICE_MAP: dict[str, Literal["heads", "tails"]] = {"h": "heads", "t": "tails"}

def get_user_choice()->Literal['heads','tails']:
    while True:
        input_str:str = input("Type your choice: ").strip().lower()
        try:
            return CHOICE_MAP[input_str]
        except KeyError:
            print(f"'{input_str}' is invalid choice. Please try again")

def coin_flip()->Literal['heads','tails']:
    print('COIN IN THE AIR')
    print('-')
    print('\\')
    print('|')
    print('/')
    print('-')
    return random.choice(CHOICES)


def play_round()->Literal['win','lose']:
    user:str=get_user_choice()
    coin:str=coin_flip()
    print(f'IT\'s {coin.upper()}')
    return "win" if user==coin else "lose"

def main()-> None:
    score:dict[str,int] = {"win": 0, "lose": 0}
    
    print("HEADS_OR_TAILS")
    print("__WELCOME__")
    print(f"h={CHOICES[0]}, t={CHOICES[1]}")
    
    while True:
        result:str =play_round()
        print(f"YOU {result.upper()}")
        if result=='win':
            score["win"]+=1
        elif result=='lose':
            score["lose"]+=1
        print('__SCORE__')
        print(f"WIN:{score['win']}, LOSE:{score['lose']}")
        play_again:str=input("play again? (y/n): ").strip().lower()
        if play_again!='y':
            break

if __name__ == "__main__":
    main()