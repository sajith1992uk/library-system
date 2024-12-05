from BookList import BookList
from UserList import UserList
from Loan import Loan
from Book import Book
from User import User

class Menu:
    def __init__(self):
        self.book_list = BookList()
        self.user_list = UserList()
        self.loan_system = Loan(self.book_list, self.user_list)
    def main_menu(self):
        while True:
            # Ask user to select the option
            print("Welcome to Sefton Library! What would you like to do today?")
            print("1. Books Section press (b)")
            print("2. Users Section press (u)")
            print("3. Loans Section press (l)")
            print("4. Quit (q)")
            choice = input("Please enter your choice: ").lower()
            # Call relevant method according to the users choice
            if choice == 'b':
                self.book_section()
            elif choice == 'u':
                self.user_section()
            elif choice == 'l':
                self.loan_section()
            elif choice == 'q':
                print("Thank you for using our library facility. Goodbye!")
                break
            else:
                print("Please enter valid input. Please try again.")

    def book_section(self):
        #  Inside the book section users is asked 6 questions, and they have chance to return the previous menu
        while True:
            print("Book Section:")
            print("1. Add a New Book (a)")
            print("2. Search for a Book (b)")
            print("3. Remove a Book (c)")
            print("4. Show Total Number of Books (d)")
            print("5. Update Book Details (e)")
            print("6. Return to previous Menu (m)")
            book_input = input("What would you like to do? Enter your choice: ").lower()
            #  Manually add the books and create book object
            if book_input == 'a':
                new_book = Book.book_section_validation()
                self.book_list.add_book(new_book)
                print(f"The book '{new_book.get_title()}' has been added successfully!")
            #  search books regarding the fields that user choose
            elif book_input == 'b':
                search_field = input("Enter the one  field  to search by (title, author, publisher, publication_date): ").lower()
                search_value = input(f"Enter the {search_field} to search: ")
                found_book = self.book_list.search_book(search_field, search_value)
                if found_book:
                    print(f"Book found: '{found_book.get_title().title()}' by {found_book.get_author().title()}")
                else:
                    print("Sorry, we couldn't find the book you're looking for.")
            elif book_input == 'c':
                title = input("Enter the title of the book you want to remove: ")
                if self.book_list.remove_book(title):
                    print(f"The book '{title}' has been removed successfully.")
                else:
                    print("Sorry, we couldn't find the book to remove.")

            elif book_input == 'd':
                print(f"Currently, there are {self.book_list.total_books()} books in the library.")

            elif book_input == 'e':
                try:
                    title = input("Enter the book title to update: ").strip().lower()
                    #  check whether user enter book is in the book dictionary, if it not there print book not found
                    book = self.book_list.find_book_by_title(title)
                    if not book:
                        print("Book not found.")
                        continue

                    title, author, year, publisher, copies = None, None, None, None, None
                    #  ask user what they are going to update
                    print("Which details do you want to update?")
                    print("1. Title (t)")
                    print("2. Author (a)")
                    print("3. Year (y)")
                    print("4. Publisher (p)")
                    print("5. Copies (c)")
                    update_choice = input("Enter your choice: ").lower()

                    if update_choice == 't':
                        title = input("Enter the new title: ")
                    elif update_choice == 'a':
                        author = input("Enter the new author: ")
                    elif update_choice == 'y':
                        year = int(input("Enter the new year: "))
                    elif update_choice == 'p':
                        publisher = input("Enter the new publisher: ")
                    elif update_choice == 'c':
                        copies = int(input("Enter the new number of copies: "))
                    else:
                        print("Invalid choice for update. Please try again.")
                        continue

                    # pass user enter data book_list clas
                    self.book_list.update_book(book.get_book_id(), title=title, author=author, year=year, publisher=publisher, copies=copies)
                    print("Book details updated successfully.")

                except ValueError as e:
                    print(f"Error: {e}")
                except KeyError as e:
                    print(f"Error: {e}")

            elif book_input == 'm':
                break

    def user_section(self):
        while True:
            print("User Section:")
            print("1. Add user press (f)")
            print("2. Remove user press (g)")
            print("3. Search user press (h)")
            print("4. Show total users press (i)")
            print("5. Update user details press (j)")
            print("6. Return to Main Menu press (m)")
            user_input = input("Enter your choice: ").lower()

            if user_input == 'f':
                new_user = User.user_section_validation()
                self.user_list.add_user(new_user)
                print("User added successfully.")

            elif user_input == 'g':
                first_name = input("Enter the first name of the user to remove: ")
                if self.user_list.remove_user(first_name):
                    print("User removed successfully.")
                else:
                    print("User not found or multiple users with same first name.")

            elif user_input == 'h':
                username = input("Enter the username to search: ")
                found_user = self.user_list.get_user(username)
                if found_user:
                    print(f"User found: {found_user.get_firstname()} {found_user.get_surname()}")
                else:
                    print("User not found.")

            elif user_input == 'i':
                print(f"Total number of users: {self.user_list.count_users()}")

            elif user_input == 'j':
                try:
                    username = input("Enter the username of the user to update: ")
                    print("Which detail do you want to update?")
                    print("1. First Name (f)")
                    print("2. Surname (s)")
                    print("3. House Number (h)")
                    print("4. Street Name (st)")
                    print("5. Postcode (p)")
                    var = input("Enter your choice: ").lower()
                    update_data = None

                    if var == 'f':
                        update_data = input("Enter new first name: ")
                        self.user_list.update_user(username, firstname=update_data)
                    elif var == 's':
                        update_data = input("Enter new surname: ")
                        self.user_list.update_user(username, surname=update_data)
                    elif var == 'h':
                        update_data = input("Enter new house number: ")
                        self.user_list.update_user(username, house_number=update_data)
                    elif var == 'st':
                        update_data = input("Enter new street name: ")
                        self.user_list.update_user(username, street_name=update_data)
                    elif var == 'p':
                        update_data = input("Enter new postcode: ")
                        self.user_list.update_user(username, postcode=update_data)
                    else:
                        print("Invalid choice for update.")
                        continue
                    print("User details updated successfully.")
                except ValueError as e:
                    print(f"Error: {e}")
                except KeyError as e:
                    print(f"Error: {e}")

            elif user_input == 'm':
                break

    def loan_section(self):
        while True:
            print("Loan section:")
            print("1. Borrow book (b)")
            print("2. Return book (r)")
            print("3. Count user books (c)")
            print("4. Print overdue books (o)")
            print("5. Return to Main Menu (m)")
            loan_choice = input("Enter your choice: ").lower()

            if loan_choice == 'b':
                username = input("Enter username: ")
                book_title = input("Enter book title to borrow: ")
                user = self.user_list.get_user(username)
                book = self.book_list.search_book("title", book_title)
                if user and book:
                    self.loan_system.borrow_book(username, book)
                else:
                    print("User or book not found.")
            elif loan_choice == 'r':
                username = input("Enter username: ")
                book_title = input("Enter book title to return: ")
                user = self.user_list.get_user(username)
                book = self.book_list.search_book("title", book_title)
                if user and book:
                    self.loan_system.return_book(username, book)
                else:
                    print("User or book not found.")
            elif loan_choice == 'c':
                username = input("Enter username: ")
                user = self.user_list.get_user(username)
                if user:
                    print(f"Total books borrowed by user: {self.loan_system.count_user_books(username)}")
                else:
                    print("User not found.")

            elif loan_choice == 'o':
                self.loan_system.overdue_books()

            elif loan_choice == 'm':
                break



if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()





