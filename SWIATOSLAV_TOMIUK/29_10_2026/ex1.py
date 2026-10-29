# ESCAPE THE TEMPLE
# Complete each function. Use return to send values back.


def sum_digits(number):
    # TODO: Return the sum of the digits.
    total = 0
    for digit in str(abs(number)):
        total += int(digit)
    return total


def count_vowels(text):
    # TODO: Count and return the vowels a, e, i, o, u.
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count


def is_palindrome(text):
    # TODO: Ignore letter case and spaces.
    # Return True or False.
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def build_code(digit_sum, vowel_count, palindrome_result):
    # TODO: Return a three-character string.
    # Map True to "1" and False to "0".
    # % 10 keeps each part to a single digit/character
    return (
        str(digit_sum % 10)
        + str(vowel_count % 10)
        + ("1" if palindrome_result else "0")
    )


def check_code(guess, secret_code):
    # TODO: Return True if the codes match.
    return guess.strip() == secret_code


def main():
    # Welcome the player.
    print("=" * 40)
    print("         ESCAPE THE TEMPLE")
    print("=" * 40)
    print("Solve the three puzzles to find the")
    print("three-digit code that unlocks the door!\n")

    # Call the puzzle functions.
    number = 341
    text = "Ancient Temple Gate"
    phrase = "never odd or even"

    print(f"Puzzle 1: Add up the digits of {number}.")
    print(f'Puzzle 2: Count the vowels in "{text}".')
    print(f'Puzzle 3: Is "{phrase}" a palindrome? (yes = 1, no = 0)')

    # Build the secret code.
    digit_sum = sum_digits(number)
    vowel_count = count_vowels(text)
    palindrome_result = is_palindrome(phrase)
    secret_code = build_code(digit_sum, vowel_count, palindrome_result)

    # Ask the player to enter the code.
    guess = input("\nEnter the 3-digit code: ")

    # Display whether the temple was unlocked.
    if check_code(guess, secret_code):
        print("\nThe stone door rumbles open... YOU ESCAPED!")
    else:
        print(f"\nThe door stays sealed. The code was {secret_code}.")


if __name__ == "__main__":
    main()
