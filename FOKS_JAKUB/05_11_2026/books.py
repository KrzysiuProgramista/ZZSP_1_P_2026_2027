
def add_book(books, title, author, year):
    new_book = {
        "title": title,
        "author": author,
        "year": year
    }
    books.append(new_book)
    return books


def find_by_author(books, author):
    found_books = []
    for item in books:
        if item["author"] == author:
            found_books.append(item)
    return found_books


def oldest_book(books):
    oldest = books[0]
    for item in books:
        if item["year"] < oldest["year"]:
            oldest = item
    return oldest


def print_books(books):
    i = 1
    for item in books:
        print(f"{i}. {item['title']} - {item['author']} ({item['year']})")
        i += 1


books = []

add_book(books, "Pan Tadeusz", "Adam Mickiewicz", 1834)
add_book(books, "Lalka", "Bolesław Prus", 1890)
add_book(books, "Quo Vadis", "Henryk Sienkiewicz", 1896)
add_book(books, "Dziady", "Adam Mickiewicz", 1823)

print("Wszystklie książki:")
print_books(books)

print("\nKsiążki Mickiewicza:")
mickiewicz = find_by_author(books, "Adam Mickiewicz")
print_books(mickiewicz)

print("\nNajstarsza książka:")
oldest = oldest_book(books)
print(f"{oldest['title']} - {oldest['author']} ({oldest['year']})")
