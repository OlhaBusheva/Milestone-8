class Book:
    def __init__(self, category, author, title):
        self.category = category
        self.author = author
        self.title = title

    def get_title(self):
        return self.title

    def __str__(self):
        return f"Category: {self.category}. Title: {self.title}. Author: {self.author}"


class Shelf:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def sort_books(self):
        self.books.sort(key=lambda book: book.get_title())

    def __str__(self):
        shelf_content = "\n".join(str(book) for book in self.books)
        return f"Shelf Content:\n{shelf_content}"


def books_on_shelves(books):
    shelves = {}
    for book in books:
        category = book.category
        if category not in shelves:
            shelves[category] = Shelf()
        shelves[category].add_book(book)
    return shelves


def sort_book(shelves):
    for shelf in shelves.values():
        shelf.sort_books()


Book1 = Book("Fantasy", "J. R. R. Tolkien", "The Hobbit")
Book2 = Book("Fantasy", "J. R. R. Tolkien", "The Lord of the Rings")
Book3 = Book("Horror", "S. King", "The Mist")
Book4 = Book("Novel", "A. Dumas", "The Three Musketeers")
Book5 = Book("Novel", "A. Dumas", "The Count of Monte Cristo")
Book6 = Book("Dystopian novel", "1984", "G. Orwell")
Book7 = Book("Dystopian novel", "Brave New World", "A. Huxley")
books = [Book1, Book2, Book3, Book4, Book5, Book6, Book7]

shelves = books_on_shelves(books)
sort_book(shelves)

for category, shelf in shelves.items():
    print(f"Shelf Category: {category}")
    print(shelf)
    print()
