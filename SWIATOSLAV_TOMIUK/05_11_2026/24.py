def oldest_book(books):
    if len(books) == 0:
        return None

    oldest = books[0]

    for book in books:
        if book["year"] < oldest["year"]:
            oldest = book

    return oldest


def print_books(books):
    for number in range(len(books)):
        book = books[number]
        print(f"{number + 1}. {book['title']} by {book['author']} ({book['year']})")
