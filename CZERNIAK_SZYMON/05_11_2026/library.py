books = []

def add_book(books, title, author, year):
    books.append({
        "title": title,
        "author": author,
        "year": year
    })
    return books


add_book(books, title="Leo Sound - A little traublemaker", author="Adam Shooter", year=2026)
add_book(books, title="Glory", author="Bartosz Gierek", year=1980)
add_book(books, title="Qou Vadis", author="Jan Kochanowski", year=1800)


def find_by_author(books, author):
    found_books = []

    for book in books:
        if author == book["author"]:
            found_books.append(book)

    return found_books


def find_oldest_book(books):
    if not books:
        return None

    oldest_book = min(books, key=lambda book: book["year"])
    return oldest_book


def print_all_books(books):
    if not books:
        print("No books found.")
        return

    print("ALL BOOKS")

    for number, book in enumerate(books, start=1):
        print(f"{number}. {book['title']}")
        print(f"   Author: {book['author']}")
        print(f"   Year: {book['year']}")
        print()


print_all_books(books)


oldest = find_oldest_book(books)

if oldest:
    print(" OLDEST BOOK")
    print(f"Title: {oldest['title']}")
    print(f"Author: {oldest['author']}")
    print(f"Year: {oldest['year']}")


author = input("Enter the author of the book:")
result = find_by_author(books, author)

if result:
    print("SEARCH RESULTS")
    for book in result:
        print(f"{book['title']} ({book['year']}) - {book['author']}")
else:
    print("No books found for this author.")
