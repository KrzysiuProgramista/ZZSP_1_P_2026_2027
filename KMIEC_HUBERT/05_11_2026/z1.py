def add_book(books, title, author, year):
    book = {"title": title, "author": author, "year": year}
    books.append(book)
    return books

def find_by_author(books, author):
    return [book for book in books if book["author"] == author]

def oldest_book(books):
    if not books:
        return None
    return min(books, key=lambda book: book["year"])

def print_books(books):
    for index, book in enumerate(books, start=1):
        print(f"{index}. '{book['title']}' by {book['author']} ({book['year']})")

library = []

add_book(library, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)
add_book(library, "The Little Prince", "Antoine de Saint-Exupery", 1943)
add_book(library, "Harry Potter and the Chamber of Secrets", "J.K. Rowling", 1998)
add_book(library, "The Great Gatsby", "F. Scott Fitzgerald", 1925)

print("--- Printing All Books ---")
print_books(library)

print("\n--- Finding Books by J.K. Rowling ---")
rowling_books = find_by_author(library, "J.K. Rowling")
print_books(rowling_books)

print("\n--- Finding the Oldest Book ---")
oldest = oldest_book(library)
if oldest:
    print(f"The oldest book is '{oldest['title']}' published in {oldest['year']}.")
