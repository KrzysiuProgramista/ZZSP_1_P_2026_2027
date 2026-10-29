def sum_digits(number):
    total = 0

    for digit in str(abs(number)):
        total += int(digit)

    return total


def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u"}
    count = 0

    for letter in text.lower():
        if letter in vowels:
            count += 1

    return count


def is_palindrome(text):
    word = "".join(text.lower().split())
    return word == word[::-1]


def build_code(digit_sum, vowel_count, palindrome_result):
    result = "1" if palindrome_result else "0"
    code = str(digit_sum % 10)
    code += str(vowel_count % 10)
    code += result

    return code


def check_code(guess, secret_code):
    if guess == secret_code:
        return True
    return False


def main():
    print("=" * 32)
    print("       ESCAPE THE TEMPLE")
    print("=" * 32)
    print("Complete the puzzles to escape!\n")

    number = int(input("Puzzle 1: Enter a number: "))
    digit_sum = sum_digits(number)
    print("Sum of digits:", digit_sum)

    sentence = input("\nPuzzle 2: Enter some text: ")
    vowel_count = count_vowels(sentence)
    print("Vowels found:", vowel_count)

    word = input("\nPuzzle 3: Enter a palindrome: ")
    palindrome_result = is_palindrome(word)
    print("Palindrome:", palindrome_result)

    secret_code = build_code(
        digit_sum, vowel_count, palindrome_result
    )

    guess = input("\nEnter the secret code: ")

    if check_code(guess, secret_code):
        print("\nThe temple door opens!")
        print("You escaped successfully!")
    else:
        print("\nIncorrect code!")
        print("The temple remains locked.")


if __name__ == "__main__":
    main()
