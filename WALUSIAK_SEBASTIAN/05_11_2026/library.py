def add_book(books, title, author, year):
    new_book = {
        "title": title,
        "author": author,
        "year": year
    }
    books.append(new_book)
    return books

def find_by_author(books, author):
    return [book for book in books if book["author"].lower() == author.lower()]

def print_books(books):
    for index, book in enumerate(books, 1):
        print(f"{index}. '{book['title']}' – {book['author']} ({book['year']})")

def oldest_book(books):
    if not books:
        return None
    return min(books, key=lambda book: book["year"])

my_library = []

add_book(my_library, "Solaris", "Stanisław Lem", 1961)
add_book(my_library, "The Hobbit", "J.R.R. Tolkien", 1937)
add_book(my_library, "Niezwyciężony", "Stanisław Lem", 1964)

print("--- All Books ---")
print_books(my_library)

print("\n--- Oldest Book ---")
oldest = oldest_book(my_library)
print(f"'{oldest['title']}' from {oldest['year']}")

print("\n--- Books by Stanisław Lem ---")
lem_books = find_by_author(my_library, "Stanisław Lem")
for b in lem_books:
    print(b['title'])
