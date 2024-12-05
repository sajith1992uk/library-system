import random
import datetime

class Book:
    # initialize the constructors with given attributes
    def __init__(self, title, author, year, publisher, copies, pub_date):
        self.__book_id = random.randint(100, 8000)  # Randomly generated book ID
        self.__title = title.strip().lower()
        self.__author = author.strip().lower()
        self.__year = self.validate_year(year)
        self.__publisher = publisher.strip().lower()
        self.__copies = self.validate_copies(copies)
        self.__available_copies = self.__copies
        self.__pub_date = self.validate_pub_date(pub_date)

    # Method to create a book instance from user input until user enter correct input
    @classmethod
    def book_section_validation(cls):
        while True:
            title = input("Enter the book title: ").strip()
            if title:
                break
            print("Please Enter Tittle.")

        while True:
            author = input("Enter the author's name: ").strip()
            if author:
                break
            print("Author cannot be empty.")

        while True:
            try:
                year = int(input("Enter the year of publication: "))
                # check year whether it valid or not
                if 1900 <= year <= 2024:
                    break
                else:
                    print("Year must be between 1900 and 2024.")
            except ValueError:
                print("Please enter a numeric value.")

        while True:
            publisher = input("Enter the publisher: ").strip()
            if publisher:
                break
            print("Publisher cannot be empty.")

        while True:
            try:
                copies = int(input("Enter the number of copies available: "))
                break
            except ValueError:
                print("Please enter a numeric value.")

        while True:
            publication_date = input("Enter the publication date (YYYY-MM-DD): ").strip()
            try:
                publication_date_val = datetime.datetime.strptime(publication_date, "%Y-%m-%d")
                if 1900 <= publication_date_val.year <= 2024:
                    break
                else:
                    print("Publication date year must be between 1900 and 2024.")
            except ValueError:
                print("Please enter a valid date in the format YYYY-MM-DD.")

        return cls(title, author, year, publisher, copies, publication_date)

# Static method to validate the year of publication, number of copies, and date
    @staticmethod
    def validate_year(year):
        if not (1900 <= year <= 2024):
            raise ValueError("Year must be between 1900 and 2024.")
        return year


    @staticmethod
    def validate_copies(copies):
        if copies < 0:
            raise ValueError("Number of copies cannot be negative.")
        return copies


    @staticmethod
    def validate_pub_date(pub_date):
        try:
            publication_date_obj = datetime.datetime.strptime(pub_date, "%Y-%m-%d")
            if not (1900 <= publication_date_obj.year <= 2024):
                raise ValueError("Publication date year must be between 1900 and 2024.")
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        return pub_date


    # Encapsulation using getters
    def get_title(self):
        return self.__title


    def get_author(self):
        return self.__author


    def get_year(self):
        return self.__year


    def get_publisher(self):
        return self.__publisher


    def get_copies(self):
        return self.__copies


    def get_available_copies(self):
        return self.__available_copies


    def get_publication_date(self):
        return self.__publication_date


    def get_book_id(self):
        return self.__book_id


    # Encapsulation using setters
    def set_title(self, title):
        if title.strip():
            self.__title = title.strip().lower()
        else:
            raise ValueError("Title cannot be empty.")


    def set_author(self, author):
        if author.strip():
            self.__author = author.strip().lower()
        else:
            raise ValueError("Author cannot be empty.")


    def set_year(self, year):
        self.__year = self.validate_year(year)


    def set_publisher(self, publisher):
        if publisher.strip():
            self.__publisher = publisher.strip().lower()
        else:
            raise ValueError("Publisher cannot be empty.")


    def set_copies(self, copies):
        self.__copies = self.validate_copies(copies)


    # Methods for managing available copies
    def decrease_copies(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
        else:
            raise ValueError("No copies available to borrow.")


    def increase_copies(self):
        if self.__available_copies < self.__copies:
            self.__available_copies += 1
        else:
            raise ValueError("Cannot return more copies than initially available.")


