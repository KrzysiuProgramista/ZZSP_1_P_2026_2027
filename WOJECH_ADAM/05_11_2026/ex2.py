def add_book(books, title, author, year):
    book = {
        'title': title,
        'author': author,
        'year': int(year)
    }
    books.append(book)
    return books

def oldest_book(books):
    if not books:
        return None
    
    oldest = books[0]
    for book in books:
        if book['year'] < oldest['year']:
            oldest = book
    return oldest

def find_by_author(books, author):
    matching_books = []
    for book in books:
        if book['author'].lower() == author.lower():
            matching_books.append(book)
    return matching_books

def print_books(books):
    if not books:
        print("No books found.")
        return
        
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

books_list = []

while True:
    inp = input("Write a command. Commands are under 'help': ").strip().lower()
    
    if inp == "quit" or inp == "exit":
        break
        
    elif inp == "add_books":
        ti = input("Whats the title of this book: ")
        au = input("Whos the author of the book: ")
        ye = input("When was the book published: ")
        add_book(books_list, ti, au, ye)
        print("Book added successfully")
        
    elif inp == "oldest_book":
        oldest = oldest_book(books_list)
        if oldest:
            print(f"Oldest book: {oldest['title']} ({oldest['year']})")
        else:
            print("No books in the library.")
            
    elif inp == "find_by_author":
        au = input("Enter author name: ")
        results = find_by_author(books_list, au)
        print_books(results)
        
    elif inp == "print_books":
        print_books(books_list)
        
    elif inp == "help":
        print("Available commands:")
        print("  add_books      - Add a new book to the library")
        print("  oldest_book    - Show the oldest book")
        print("  find_by_author - Search books by author")
        print("  print_books    - Display all books")
        print("  quit / exit    - Close the program")
        
    else:
        print("Not a command. Use 'help' to see them.")
