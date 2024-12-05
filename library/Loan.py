
import datetime
from Book import Book
from User import User


class Loan:
    def __init__(self, book_list, user_list):
        # Dictionary to store borrowed books. The key is the username, and the value is a list of tuples.
        # Each tuple contains a book object and the borrow date.
        self.loans = {}
        self.book_list = book_list
        self.user_list = user_list

    def borrow_book(self, username, book):
        try:
            if not isinstance(book, Book):
                raise TypeError("Invalid book object provided.")

            user = self.user_list.get_user(username)
            # Check if the book has available copies
            if book.get_available_copies() == 0:
                raise ValueError(f"Sorry, all copies of '{book.get_title()}' are currently borrowed.")

            # Decrement the available copies and add to the user's borrowed books
            book.decrease_copies()
            # capture the current date and time at the point when the user borrows a book
            borrow_date = datetime.datetime.now()

            if username not in self.loans:
                self.loans[username] = []

            self.loans[username].append((book, borrow_date))
            print(f"Book '{book.get_title()}' successfully borrowed by user '{username}'.")

        except (KeyError, ValueError, TypeError) as e:
            print(f"Error: {e}")

    def return_book(self, username, book):
        try:

            # Check if the user has borrowed any books
            if username not in self.loans:
                raise ValueError(f"User '{username}' has no borrowed books.")

            # Check if the specific book was borrowed by the user
            book_borrowed = False
            for b in self.loans[username]:
                if b[0] == book:
                    book_borrowed = True
                    break
            # If the book was not borrowed, raise an error
            if not book_borrowed:
                raise ValueError(f"Book '{book.get_title()}' was not borrowed by user '{username}'.")

            # Increment the available copies since the book is being returned
            book.increase_copies()

            # Remove the returned book from the user's borrowed books list
            self.loans[username] = [b for b in self.loans[username] if b[0] != book]

            # Inform the user that the book was successfully returned
            print(f"Book '{book.get_title()}' successfully returned by user '{username}'.")

        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def count_user_books(self, username):
        try:
            user = self.user_list.get_user(username)
            if not user:
                raise KeyError(f"User with username '{username}' not found.")

            if username in self.loans:
                book_count = len(self.loans[username])
                print(f"Total books borrowed by user '{username}': {book_count}")
                return book_count
            else:
                print(f"Total books borrowed by user '{username}': 0")
                return 0

        except KeyError as e:
            print(f"Error: {e}")
            return 0

    def overdue_books(self):
        try:
            print("Overdue Books:")
            today = datetime.datetime.now()
            overdue_found = False

            for username, borrowed_books in self.loans.items():
                user = self.user_list.get_user(username)
                if not user:
                    continue

                for book, borrow_date in borrowed_books:
                    # Assume a loan period of 14 days for determining overdue books
                    due_date = borrow_date + datetime.timedelta(days=14)
                    if today > due_date:
                        overdue_found = True
                        print(
                            f"User: {user.get_username()}, | Book: '{book.get_title().title()}' | Due Date: {due_date.strftime('%Y-%m-%d')}")

            if not overdue_found:
                print("No overdue books found.")

        except Exception as e:
            print(f"Error: {e}")
