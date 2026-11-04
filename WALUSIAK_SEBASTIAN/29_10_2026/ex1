# ESCAPE THE TEMPLE

def sum_digits(number):
    total = 0
    for digit in str(abs(number)):
        total += int(digit)
    return total


def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for letter in text.lower():
        if letter in vowels:
            count += 1

    return count


def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def build_code(digit_sum, vowel_count, palindrome_result):
    palindrome_digit = "1" if palindrome_result else "0"
    return str(digit_sum) + str(vowel_count) + palindrome_digit


def check_code(guess, secret_code):
    return guess == secret_code


def main():
    print("=== ESCAPE THE TEMPLE ===", flush=True)

    number = int(input("Enter a number: "))
    text = input("Enter a word or phrase: ")

    digit_sum = sum_digits(number)
    vowel_count = count_vowels(text)
    palindrome_result = is_palindrome(text)

    print("\n=== YOUR RESULTS ===")
    print("Sum of digits:", digit_sum)
    print("Number of vowels:", vowel_count)
    print("Is palindrome:", palindrome_result)

    secret_code = build_code(
        digit_sum,
        vowel_count,
        palindrome_result
    )


    guess = input("\nEnter the secret code: ")

    if check_code(guess, secret_code):
        print("The temple was unlocked!")
    else:
        print("Wrong code! The temple remains locked.")
        print("Correct code was:", secret_code)


if __name__ == "__main__":
    main()
