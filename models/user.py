class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def validate_email(self):
        return "@" in self.email

    def validate_password(self):
        return len(self.password) >= 6

    def is_valid(self):
        return self.validate_email() and self.validate_password()

    def __repr__(self):
        return f"User({self.username})"
