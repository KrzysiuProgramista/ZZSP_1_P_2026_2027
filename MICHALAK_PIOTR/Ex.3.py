books = []



def add_book(books, title, author, year):
    new_book = {
        'title': title,
        'author': author,
        'year': year
    }
    books.append(new_book)
    return books

def find_by_author(books, author):
    return [book for book in books if book['author'].lower() == author.lower()]

def oldest_book(books):
    if not books:
        return None
    return min(books, key=lambda book: book['year'])

def print_books(books):
    if not books:
        print("No books available in the collection.")
        return
        
    for index, book in enumerate(books, 1):
        print(f"{index}. \"{book['title']}\" by {book['author']} ({book['year']})")