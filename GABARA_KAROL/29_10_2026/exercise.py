# ESCAPE THE TEMPLE
# Complete each function. Use return to send values back.


def sum_digits(number):
    # Return the sum of the digits.
    return sum(int(digit) for digit in str(abs(number)))


def count_vowels(text):
    # Count and return the vowels a, e, i, o, u.
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)


def is_palindrome(text):
    # Ignore letter case and spaces.
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def build_code(digit_sum, vowel_count, palindrome_result):
    # Return a three-character string.
    # Map True to "1" and False to "0".
    palindrome_digit = "1" if palindrome_result else "0"
    return f"{digit_sum % 10}{vowel_count % 10}{palindrome_digit}"


def check_code(guess, secret_code):
    # Return True if the codes match.
    return guess == secret_code


def main():
    # Welcome the player.
    print("================================")
    print("     ESCAPE THE TEMPLE")
    print("================================")
    print("Solve the puzzles to unlock the temple!\n")

    # Puzzle 1: Sum of digits
    number = int(input("Puzzle 1: Enter a number: "))
    digit_sum = sum_digits(number)
    print(f"The sum of the digits is: {digit_sum}\n")

    # Puzzle 2: Count vowels
    text = input("Puzzle 2: Enter a word or sentence: ")
    vowel_count = count_vowels(text)
    print(f"The number of vowels is: {vowel_count}\n")

    # Puzzle 3: Check palindrome
    word = input("Puzzle 3: Enter a palindrome: ")
    palindrome_result = is_palindrome(word)
    print(f"Is it a palindrome? {palindrome_result}\n")

    # Build the secret code
    secret_code = build_code(
        digit_sum, vowel_count, palindrome_result
    )

    # Ask the player to enter the code
    guess = input("Enter the three-character secret code: ")

    # Display the result
    if check_code(guess, secret_code):
        print("\nCongratulations! The temple is unlocked!")
        print("You escaped the temple!")
    else:
        print("\nWrong code! The temple remains locked.")
        print("Try again next time!")


if __name__ == "__main__":
    main()
