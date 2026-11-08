def oldest_book(books):
    if not books:
        return None
    
    old_one = books[0]
    for b in books:
        if b["year"] < old_one["year"]:
            old_one = b
    return old_one


def print_books(books):
    idx = 1
    for b in books:
        print(f"{idx}. {b['title']} by {b['author']} ({b['year']})")
        idx += 1
