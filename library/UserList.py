from User import User

class UserList:
    def __init__(self):
        # Add dictionary to store users and also the current users
        self.users = {}
        self.current_users()

    def current_users(self):
        # This five users add to the dictionary using for loop
        existing_users = [
            ("SSh", "Suren", "Sajith", 12, "Hulme St", "12345", "SSh@gmail.com", "1992-11-05"),
            ("MN", "Mano", "Sathsarani", 57, "Hart St", "23456", "mano@gmail.com", "1994-11-07"),

        ]
        for i in existing_users:
            new_user = User(*i)
            self.add_user(new_user)
    # from this method add validated users to the dictionary
    def add_user(self, user):
        if not isinstance(user, User):
            raise TypeError("Error adding user: Invalid user object provided.")
        if user.get_username() in self.users:
            raise ValueError(f"Error adding user: Username '{user.get_username()}' already exists.")
        self.users[user.get_username()] = user

    # from this method remove users from the dictionary
    def remove_user(self, name):
        if name not in self.users:
            raise KeyError(f" Username '{name}' not found.")
        del self.users[name]
        return True

    # from this method search users from the dictionary
    def search_user(self, username):
        return self.users.get(username, None)

    def get_user(self, username):
        # Directly use dictionary lookup to get the user
        user = self.users.get(username)
        if not user:
            raise KeyError(f" User with username '{username}' not found.")
        return user

    def count_users(self):
        return len(self.users)

    def update_user(self, username, firstname=None, surname=None, house_number=None, street_name=None, postcode=None):
        user = self.users.get(username)
        if not user:
            raise KeyError(f" Username '{username}' not found.")

        # Update user attributes if provided
        if firstname is not None:
            user.set_firstname(firstname)
        if surname is not None:
            user.set_surname(surname)
        if house_number is not None:
            user.set_house_number(house_number)
        if street_name is not None:
            user.set_street_name(street_name)
        if postcode is not None:
            user.set_postcode(postcode)

        return True
