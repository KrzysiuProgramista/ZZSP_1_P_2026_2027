from library import add_book, find_by_author, oldest_book, print_books

books = []
add_book(books, "Solaris", "Stanisław Lem", 1961)
add_book(books, "Dune", "Frank Herbert", 1965)
add_book(books, "The Hobbit", "J. R. R. Tolkien", 1937)
add_book(books, "1984", "George Orwell", 1949)

print_books(books)
print(find_by_author(books, "Stanisław Lem"))
print(oldest_book(books))
