from models.user import User

user = User("wasim", "wasim@gmail.com", "pass123")
print(user.is_valid())  # Expect True
print(user)             # Expect User(wasim)

bad_user = User("john", "invalidemail", "123")
print(bad_user.is_valid())  # Expect False
