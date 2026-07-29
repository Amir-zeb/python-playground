import random

CHOICES = ("rock", "paper", "scissors")
CHOICE_MAP = {"r": "rock", "p": "paper", "s": "scissors"}
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def get_user_choice()->str:
    while True:
        input_str = input("Type your choice: ").strip().lower()
        try:
            return CHOICE_MAP[input_str]
        except KeyError:
            print(f"'{input_str}' is invalid choice. Please try again")

def get_computer_choice()->str:
    num:int = random.randint(0, 2)
    return CHOICES[num]
    

def decide_winner(user, computer) -> str:
    print(f"You={user}, Computer={computer}")
    if user == computer:
        return "tie"
    return "win" if BEATS[user] == computer else "lose"
        

def play_round()->str:
    user=get_user_choice()
    computer=get_computer_choice()
    return decide_winner(user,computer)

def main():
    score = {"user": 0, "computer": 0}
    
    print("ROCK__PAPER__SCISSORS")
    print("__WELCOME__")
    print(f"r={CHOICES[0]}, p={CHOICES[1]}, s={CHOICES[2]}")
    
    while True:
        result =play_round()
        print(f"result={result}")
        if result=='win':
            score["user"]+=1
        elif result=='lose':
            score["computer"]+=1
        print('__Score__')
        print(f"You:{score['user']}, Computer:{score['computer']}")
        play_again:str=input("play again? (y/n): ").strip().lower()
        if play_again!='y':
            break

if __name__ == "__main__":
    main()