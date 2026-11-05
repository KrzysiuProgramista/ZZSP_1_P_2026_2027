"""
ESCAPE THE TEMPLE
Complete each function. Use return to send values back.
Includes Bonus Challenges: 3 attempts, hints on wrong guess, 
punctuation ignored in palindromes, and a 4th puzzle function.
"""

def sum_digits(number):
    """Return the sum of the digits."""
    total = 0
    for digit in str(abs(number)):
        if digit.isdigit():
            total += int(digit)
    return total


def count_vowels(text):
    """Count and return the vowels a, e, i, o, u."""
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


def is_palindrome(text):
    """Ignore letter case, spaces, and punctuation. Return True or False."""
    cleaned = ""
    for char in text.lower():
        if char.isalnum():  # This automatically ignores punctuation and spaces
            cleaned += char
            
    if not cleaned:
        return False
        
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


def count_consonants(text):
    """Bonus Challenge D: Fourth puzzle function to count consonants."""
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for char in text.lower():
        if char in consonants:
            count += 1
    return count


def build_code(digit_sum, vowel_count, palindrome_result, consonant_count):
    """Return a four-character string combining all puzzle results."""
    p_char = "1" if palindrome_result else "0"
    d_char = str(digit_sum % 10)
    v_char = str(vowel_count % 10)
    c_char = str(consonant_count % 10)
    
    return d_char + v_char + p_char + c_char


def check_code(guess, secret_code):
    """Return True if the codes match."""
    return guess.strip() == secret_code


def main():
    """Own the menu loop and handle player attempts and hints."""
    print("WELCOME TO THE TEMPLE PUZZLE CHALLENGE")
    print("Solve the riddles to generate the four-character activation code.\n")
    
    # Target puzzle data
    puzzle_number = 459               # Digits sum = 18 -> '8'
    puzzle_text = "Never odd or even!" # Vowels = 6 -> '6', Palindrome = True -> '1', Consonants = 8 -> '8'
    
    # Calculate results using functions
    digit_sum = sum_digits(puzzle_number)
    vowel_count = count_vowels(puzzle_text)
    palindrome_result = is_palindrome(puzzle_text)
    consonant_count = count_consonants(puzzle_text)
    
    # Generate the secret code
    secret_code = build_code(digit_sum, vowel_count, palindrome_result, consonant_count)
    
    print(f"Hint 1: The magical number is {puzzle_number}.")
    print(f"Hint 2: The sacred inscription is '{puzzle_text}'.")
    
    # Bonus Challenge A: Limit to 3 attempts
    attempts = 3
    
    while attempts > 0:
        guess = input(f"\nEnter the 4-character security code ({attempts} attempts left): ").strip()
        
        if check_code(guess, secret_code):
            print("\nSUCCESS! The code matches. The temple inner sanctum has been unlocked.")
            return
        else:
            attempts -= 1
            print("Incorrect code!")
            
            # Bonus Challenge B: Give a specific hint after a wrong guess
            if attempts > 0:
                if attempts == 2:
                    print(f"Hint: The first two characters of the code are {secret_code[:2]}.")
                elif attempts == 1:
                    print(f"Hint: The code ends with the character {secret_code[-1]}.")
                    
    print(f"\nFAILURE! You have run out of attempts. The temple remains permanently sealed.")


if __name__ == "__main__":
    main()
