def add_book(books, title, author, year):
    book = {
        "title": title,
        "author": author,
        "year": year
    }
    books.append(book)
    return books

def find_by_author(books, author):
    return [book for book in books if book["author"].lower() == author.lower()]

def oldest_book(books):
    if not books:
        return None
    return min(books, key=lambda book: book["year"])

def print_books(books):
    if not books:
        print("The library is empty.")
        return
    for index, book in enumerate(books, 1):
        print(f"{index}. '{book['title']}' by {book['author']} ({book['year']})")

library = []

library = add_book(library, "The Hobbit", "J.R.R. Tolkien", 1937)
library = add_book(library, "1984", "George Orwell", 1949)
library = add_book(library, "The Fellowship of the Ring", "J.R.R. Tolkien", 1954)
library = add_book(library, "To Kill a Mockingbird", "Harper Lee", 1960)

print("--- Testing add_book ---")
print(f"Successfully added {len(library)} books.\n")

print("--- Testing print_books ---")
print_books(library)
print()

print("--- Testing find_by_author (J.R.R. Tolkien) ---")
tolkien_books = find_by_author(library, "J.R.R. Tolkien")
print_books(tolkien_books)
print()

print("--- Testing oldest_book ---")
oldest = oldest_book(library)
if oldest:
    print(f"The oldest book is: '{oldest['title']}' published in {oldest['year']}")
