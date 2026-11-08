def add_book(books,title,author,year):
    book = {"title": title,"author": author,"year": year}
    books.append(book)
    return books
def find_by_author(books, author):
    result = []
    for book in books:
        if book["author"] == author:
            result.append(book)
    return result
def oldest_book(books):
    oldest = books[0]
    for book in books:
        if book["year"] < oldest["year"]:
            oldest = book
    return oldest
def print_books(books):
    number = 1
    for book in books:
        print(f"{number}. {book['title']} - {book['author']} ({book['year']})")
        number += 1

books = []
books = add_book(books, "Pan Tateusz","Adam Mickiewicz",1834)
books = add_book(books, "Lalka","Bolesław Prus",1890)
books = add_book(books, "Quo Vadis","Henryk Sienkiewicz",1896)
books = add_book(books, "Dziady","Adam Mickiewicz",1823)

print("Wszystklie książki:")
print_books(books)
print("\nKsiążki Mickiewicza:")
mickiewicz = find_by_author(books, "Adam Mickiewicz")
print_books(mickiewicz)
print("\nNajstarsza książka:")
oldest = oldest_book(books)
print(f"{oldest['title']} - {oldest['author']} ({oldest['year']})")
