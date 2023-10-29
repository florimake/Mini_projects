import random

NUM_DIGITS = 3 # (!) Try setting this to 1 or 10.
MAX_GUESSES = 10 # (!) Try setting this to 1 or 100.

def set_num_digits(digit=3):
    """int() - (!) Try setting this to 1 or 10."""
    global NUM_DIGITS
    NUM_DIGITS = int(digit)
    
def set_max_guesses(guesses=10):
    """int() - (!) Try setting this to 1 or 100."""
    global MAX_GUESSES
    MAX_GUESSES = int(guesses)
    
def messages():
    print("\nBagels, a deductive logic game.")
    print(f"I am thinking of a {NUM_DIGITS}-digit number. Try to guess what it is.")
    print(f"I have {MAX_GUESSES} guesses to try")
    print("Here are some clues:")
    print("When I say: That means:")
    print("Pico - One digit is correct but in the wrong position.")
    print("Fermi - One digit is correct and in the right position.")
    print("Bagels - No digit is correct.\n")
    
def compare(number, hint):
    print(f"hint-{hint}; numner-{number}")
    found = 0
    cont = 0
    clue = []
    for nr in hint:
        if nr in number:
            if nr == number[cont]:
                found += 1
                cont += 1
                clue.append("Pico")
            else:
                found += 1
                cont += 1
                clue.append("Fermi")
        elif nr not in number:
            cont += 1
    if nr not in number and found == 0:
            print('Bagels - No digit is correct.')
    else: 
        print(" - ".join(clue))

def play():
    num = ''.join([str(random.randint(0, 9)) for _ in range(NUM_DIGITS)])
    guesses = 1
    print(f"You have {MAX_GUESSES} guesses to get the {NUM_DIGITS} digits.")
    while True:
        if guesses > MAX_GUESSES:
            print(f"\nYou have {(MAX_GUESSES+1)-guesses} guesses, you miss {num}")
            break
        print(f"Guess #{guesses}:")
        while True:
            number = input(">  ")
            if number == 'exit':
                print("Thanks for playing!\n")
                exit()
            elif number == 'back':
                break
            elif len(number) == NUM_DIGITS:
                try: 
                    int(number)
                    break
                except:
                    print(f"Incorect, insert {NUM_DIGITS} digits ...")
            else:
                print(f"Incorect, insert {NUM_DIGITS} digits ...")
        if number == 'exit':
            print("Thanks for playing!\n")
            exit()
        elif number == 'back':
            break
        elif number == num:
            print(f"You got it! {num} is the correct number and you get in {guesses} guesses")
            break
        compare(num, number)
        guesses += 1

if __name__ == "__main__":
    messages()
    while True:
        print(f"1. Play")
        print(f"2. Change digits and quesses")
        print(f"3. Exit")
        player = input("> ")
        print()
        if player == "1":
            while True:
                play()
                if input("Do you want to play again? (yes or no)") == "no":
                    print("")
                    break
        elif player == "2":
            set_num_digits(input("setup digits: "))
            set_max_guesses(input("setup guesses: "))
        elif player == "3":
            print("Thanks for playing!")
            break
        