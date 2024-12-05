from Book import Book

# BookList Class
class BookList:
    # Add dictionary to store books and also the current books
    def __init__(self):
        self.books = {}
        self.current_books()
    def current_books(self):
        # This five books add to the dictionary using for loop
        current_resources = [
            ("Harry Porter", "J. K. Rowling", 2005, "Bloomsbury", 5, "2005-12-12"),
            ("The Village by the Sea", "Anita Desai", 1982, "Heinemann", 10, "1982-10-10"),
        ]
        for book in current_resources:
            cur_book = Book(*book)
            self.add_book(cur_book)


    # This method use to add books to the dictionary from using validated book object
    def add_book(self, book):
        try:
            self.books[book.get_book_id()] = book
        except AttributeError as e:
            raise AttributeError("Invalid book") from e
    # store book id as key and book object as value in the books dictionary


    def search_book(self, search_field, search_value):
        search_value = search_value.strip().lower()
        #  get books comparing its selected filed and value
        try:
            for book in self.books.values():
                if search_field == 'title' and book.get_title() == search_value:
                    return book
                elif search_field == 'author' and book.get_author() == search_value:
                    return book
                elif search_field == 'publisher' and book.get_publisher() == search_value:
                    return book
                elif search_field == 'publication_date' and book.get_publication_date() == search_value:
                    return book
        except AttributeError as e:
            raise AttributeError("Invalid attribute provided.") from e
        return None
    def remove_book(self, title):
        # remove book from the dictionary by del method
        title = title.strip().lower()
        for book_id, book in list(self.books.items()):
            if book.get_title() == title:
                del self.books[book_id]
                return True
    def total_books(self):
        # return the length of the dictionary
        return len(self.books)

    def find_book_by_title(self, title):
        for book in self.books.values():
            if book.get_title().lower() == title.lower():
                return book
        return None

    def update_book(self, book_id, title=None, author=None, year=None, publisher=None, copies=None):
        try:
            # Retrieve the book using the provided book_id
            book = self.books.get(book_id)
            if not book:
                raise KeyError("Book not found.")

            if title is not None:
                book.set_title(title)
            if author is not None:
                book.set_author(author)
            if year is not None:
                book.set_year(year)
            if publisher is not None:
                book.set_publisher(publisher)
            if copies is not None:
                book.set_copies(copies)
            return True
        # Handle the case where the book is not found in the collection
        except KeyError as e:
            raise KeyError( "Book not found in the collection.") from e
        except AttributeError as e:
            raise AttributeError("Invalid attribute provided.") from e




