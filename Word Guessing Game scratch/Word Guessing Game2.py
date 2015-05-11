import random


def get_random_word():
    words = ["apples", "cheese", "pizza"]
    word = words[random.randint(0, 2)]
    return word


def get_blanked_word(word):
    blanked_word = list("-"*len(word))
    return blanked_word


def show(blanked_word):
    spaced_blanked_word = " ".join(blanked_word)
    return spaced_blanked_word


def process_guess(letter, word, blanked_word):
    found = False
    for i in range(0, len(word)):
        if word[i] == letter:
            blanked_word[i] = letter
            found = True
    return found


def check_finished(blanked_word):
    for i in range(0, len(blanked_word)):
        if blanked_word[i] == "-":
            return False
    return True


def strike_x(strikes):
    return "X " * strikes


def play_word_game():
    strikes = 0
    max_strikes = 3
    playing = True

    word = get_random_word()
    blanked_word = get_blanked_word(word)
    print("Your word is \n" + show(blanked_word))

    while playing:
        print("Please guess a letter")
        letter = input()

        found = process_guess(letter, word, blanked_word)
        print(show(blanked_word))
        finished = check_finished(blanked_word)

        if not found:
            strikes += 1
            strike_as_x = strike_x(strikes)
            print(strike_as_x)

        if strikes >= max_strikes:
            playing = False

        if finished:
            playing = False

    if strikes >= max_strikes:
        print("Loser!")

    if strikes < max_strikes:
        print("You Won!")

print("Game Started")
play_word_game()
print("Game Over")

