
book = []

def add_book(books, title, author, year):
    """Add one book and return the updated list."""
    book = {"title": title, "author": author, "year": year}
    books.append(book)
    return books



def find_by_author(books, author):
    """Find books by author (case-insensitive)."""
    return [book for book in books
            if book["author"].lower() == author.lower()]

def oldest_book(books):
    if not books:
        return None
    return min(books, key=lambda book: book["year"])

def print_books(books):
    if not books:
        return None
    print(books)
    return books
