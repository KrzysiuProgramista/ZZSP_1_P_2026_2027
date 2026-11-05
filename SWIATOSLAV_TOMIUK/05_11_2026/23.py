def add_book(books, title, author, year):
    book = {
        "title": title,
        "author": author,
        "year": year
    }
    books.append(book)
    return books


def find_by_author(books, author):
    result = []

    for book in books:
        if book["author"] == author:
            result.append(book)

    return result
