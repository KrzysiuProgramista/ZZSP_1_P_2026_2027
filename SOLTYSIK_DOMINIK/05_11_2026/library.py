
class ShelfManager:
    def __init__(self):
        self.collection = [
            {
                "title": "JoJo's Bizarre Adventure Part 7: Steel Ball Run",
                "author": "Hirohiko Araki",
                "year": 2004
            },
            {
                "title": "JoJo's Bizarre Adventure Part 8: JoJolion",
                "author": "Hirohiko Araki",
                "year": 2011
            },
            {
                "title": "JoJo's Bizarre Adventure Part 9: The JOJOLands",
                "author": "Hirohiko Araki",
                "year": 2023
            }
        ]

    def store_book(self, book_title, book_author, publish_year):
        new_entry = {
            "title": book_title,
            "author": book_author,
            "year": publish_year
        }
        self.collection.append(new_entry)

    def show_collection(self):
        if not self.collection:
            print("The library is empty.")
            return

        print("\nMY MANGA COLLECTION")
        print("-------------------")

        for position, entry in enumerate(self.collection, start=1):
            print(f"{position}. {entry['title']}")
            print(f"   Author: {entry['author']}")
            print(f"   Year: {entry['year']}\n")

    def get_earliest_book(self):
        if not self.collection:
            return None

        earliest = self.collection[0]

        for entry in self.collection[1:]:
            if entry["year"] < earliest["year"]:
                earliest = entry

        return earliest

    def look_up_writer(self, writer_name):
        matches = []

        for entry in self.collection:
            if entry["author"].casefold() == writer_name.strip().casefold():
                matches.append(entry)

        return matches

    def show_earliest_book(self):
        oldest_entry = self.get_earliest_book()

        if oldest_entry is None:
            print("There are no manga in the collection.")
            return

        print("\nOLDEST MANGA")
        print("------------")
        print(f"Title: {oldest_entry['title']}")
        print(f"Author: {oldest_entry['author']}")
        print(f"Year: {oldest_entry['year']}")


# Create the manga collection
my_shelf = ShelfManager()

# Display all manga
my_shelf.show_collection()

# Find and display the oldest manga
my_shelf.show_earliest_book()

# Search for manga by author
search_name = input("\nEnter an author's name: ")
matching_entries = my_shelf.look_up_writer(search_name)

if matching_entries:
    print("\nSEARCH RESULTS")
    print("--------------")

    for entry in matching_entries:
        print(f"{entry['title']} ({entry['year']}) - {entry['author']}")
else:
    print("No manga found for this author.")
