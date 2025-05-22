import random

# Constants
COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']  # Red, Green, Blue, Yellow, White, Orange
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    """Generates a random code consisting of CODE_LENGTH colors."""
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code

def guess_code():
    """Takes and validates the user's guess."""
    while True:
        guess = input(f"Enter your guess ({CODE_LENGTH} colors, space-separated like R G B Y): ").upper().split()

        if len(guess) != CODE_LENGTH:
            print(f"Please enter exactly {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color '{color}'. Please use only {COLORS}.")
                break
        else:
            return guess  # Only return if all colors are valid

def check_code(guess, real_code):
    """Checks the guess against the real code and returns counts of correct and misplaced colors."""
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0
    incorrect_colors = 0

    # First, count correct colors in the correct position
    for i in range(CODE_LENGTH):
        if guess[i] == real_code[i]:
            correct_pos += 1
        else:
            # Count all other colors that are in the real_code but not at the correct position
            if real_code[i] in color_counts:
                color_counts[real_code[i]] += 1
            else:
                color_counts[real_code[i]] = 1

    # Now, count the colors that are correct but in the wrong position
    for i in range(CODE_LENGTH):
        if guess[i] != real_code[i]:
            if guess[i] in color_counts and color_counts[guess[i]] > 0:
                incorrect_pos += 1
                color_counts[guess[i]] -= 1
            else:
                incorrect_colors += 1

    return correct_pos, incorrect_pos, incorrect_colors

def game():
    """Runs the Mastermind game."""
    print("Welcome to Mastermind!")
    print(f"Try to guess the secret code made of {CODE_LENGTH} colors from {COLORS}.")
    print(f"You have {TRIES} tries to guess correctly.")

    code = generate_code()
    # print(f"DEBUG: Secret code is {''.join(code)}")  # Uncomment for testing

    for attempt in range(1, TRIES + 1):
        print(f"\nAttempt {attempt}:")
        guess = guess_code()
        correct_pos, incorrect_pos, incorrect_colors = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"\nCongratulations! You guessed the code {''.join(code)} correctly in {attempt} attempts!")
            break

        print(f"Correct Positions: {correct_pos} | Correct Colors in Wrong Positions: {incorrect_pos} | Incorrect Colors: {incorrect_colors}")

    else:
        print(f"\nSorry! You've used all {TRIES} tries. The correct code was {''.join(code)}.")

if __name__ == "__main__":
    game()
