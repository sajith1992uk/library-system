import datetime

class User:
    def __init__(self, username, firstname, surname, house_number, street_name, postcode, email, date_birth):
        self.__username = username
        self.__firstname = firstname
        self.__surname = surname
        self.__house_number = int(house_number)
        self.__street_name = street_name
        self.__postcode = postcode
        self.__email = email
        self.__date_birth = date_birth

    # Method to create a user instance from user input until user enter correct input
    @classmethod
    def user_section_validation(cls):
        while True:
            username = input("Enter username: ").strip()
            if username:
                break
            print("Username cannot be empty.")

        while True:
            firstname = input("Enter first name: ").strip()
            if firstname:
                break
            print("First name cannot be empty.")

        while True:
            surname = input("Enter surname: ").strip()
            if surname:
                break
            print("Surname cannot be empty.")

        while True:
            try:
                house_number = int(input("Enter house number: ").strip())
                break
            except ValueError:
                print("Please enter a valid numeric value for the house number.")

        while True:
            street_name = input("Enter street name: ").strip()
            if street_name:
                break
            print("Street name cannot be empty.")

        while True:
            postcode = input("Enter postcode: ").strip()
            if postcode:
                break
            print("Postcode cannot be empty.")

        while True:
            email = input("Enter email: ").strip()
            if email:
                break
            print("Email cannot be empty.")

        while True:
            date_birth = input("Enter date of birth (YYYY-MM-DD): ").strip()
            try:
                user_date = datetime.datetime.strptime(date_birth, "%Y-%m-%d")
                if 1900 <= user_date.year <= 2024:
                    break
                else:
                    print("user date year must be between 1900 and 2024.")
            except ValueError:
                print("Please enter a valid date in the format YYYY-MM-DD.")

        return cls(username, firstname, surname, house_number, street_name, postcode, email, date_birth)

    # Encapsulation using getters and setters
    def get_username(self):
        return self.__username

    def get_firstname(self):
        return self.__firstname

    def get_surname(self):
        return self.__surname

    def get_house_number(self):
        return self.__house_number

    def get_street_name(self):
        return self.__street_name

    def get_postcode(self):
        return self.__postcode

    def get_email(self):
        return self.__email

    def set_firstname(self, firstname):
        self.__firstname = firstname

    def set_surname(self, surname):
        self.__surname = surname

    def set_house_number(self, house_number):
        try:
            self.__house_number = int(house_number)
        except ValueError:
            raise ValueError("Error setting house number: Please enter a valid numeric value.")

    def set_street_name(self, street_name):
        self.__street_name = street_name

    def set_postcode(self, postcode):
        self.__postcode = postcode
