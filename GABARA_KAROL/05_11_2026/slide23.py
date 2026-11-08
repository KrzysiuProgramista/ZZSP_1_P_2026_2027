def add_book(books_list, t, a, y):
    books_list.append({"title": t, "author": a, "year": y})
    return books_list


def find_by_author(books_list, author_name):
    found = []
    i = 0
    while i < len(books_list):
        item = books_list[i]
        if item["author"] == author_name:
            found.append(item)
        i += 1
    return found
