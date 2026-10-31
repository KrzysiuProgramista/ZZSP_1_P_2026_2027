MAX_ATTEMPTS = 3

CODE_FORMAT = ("Code format: digit sum, vowel count, consonant count, "
               "then 1 for a palindrome or 0 for not a palindrome.")

def sum_digits(number):
    total = 0
    for digit in str(abs(number)):
        total += int(digit)
    return total

def count_vowels(text):
    vowels = "aeiou"
    total = 0
    for letter in text.lower():
        if letter in vowels:
            total += 1
    return total

def count_consonants(text):
    consonants = "bcdfghjklmnpqrstvwxyz"
    total = 0
    for letter in text.lower():
        if letter in consonants:
            total += 1
    return total

def is_palindrome(text):
    cleaned = ""
    for letter in text.lower():
        if letter.isalnum():
            cleaned += letter
    return cleaned == cleaned[::-1]

def build_code(digit_sum, vowel_count, consonant_count, palindrome_result):
    first = str(digit_sum % 10)
    second = str(vowel_count % 10)
    third = str(consonant_count % 10)
    fourth = "1" if palindrome_result else "0"
    return first + second + third + fourth

def check_code(guess, secret_code):
    return guess.strip() == secret_code

def show_clues(clues, attempt):
    if attempt == 1:
        print(clues[0])
    elif attempt == 2:
        print(clues[1])
    else:
        print("Final attempt - here are all the clues:")
        for clue in clues:
            print(clue)
        print(CODE_FORMAT)
    print()

def main():
    print("Welcome to Escape the Temple!")
    print("You have", MAX_ATTEMPTS, "attempts to find the secret code.")
    print()

    number = 123
    vowel_text = "ANCIENT TEMPLE"
    consonant_text = "ANCIENT TEMPLE"
    palindrome_text = "Never odd or even!"

    digits = sum_digits(number)
    vowels = count_vowels(vowel_text)
    consonants = count_consonants(consonant_text)
    palindrome = is_palindrome(palindrome_text)

    secret_code = build_code(digits, vowels, consonants, palindrome)

    clues = [
        "Clue 1: The digits of " + str(number) + " add up to " + str(digits),
        "Clue 2: " + vowel_text + " has " + str(vowels) + " vowels",
        "Clue 3: " + consonant_text + " has " + str(consonants) + " consonants",
        "Clue 4: Is " + repr(palindrome_text) + " a palindrome? " +
        str(palindrome),
    ]

    attempt = 1
    while attempt <= MAX_ATTEMPTS:

        show_clues(clues, attempt)

        guess = input("Attempt " + str(attempt) + " of " +
                      str(MAX_ATTEMPTS) + " - enter the code: ").strip()

        # Reject invalid input without using up an attempt.
        if len(guess) != len(secret_code) or not guess.isdigit():
            print("Please enter exactly", len(secret_code), "digits.")
            print()
            continue

        if check_code(guess, secret_code):
            print("The temple doors open. You escaped!")
            return

        if attempt < MAX_ATTEMPTS:
            print("That code is wrong. Try again.")
            print()

        attempt += 1

    print("The temple stays sealed. The correct code was", secret_code)

if __name__ == "__main__":
    main()