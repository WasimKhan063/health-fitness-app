# In Python terminal:
from models.database import add_user, verify_user

# Test add_user
result = add_user("wasim", "wasim@gmail.com", "password123")
print(result)  # Should print: {'email': 'wasim@gmail.com', 'password': 'password123', 'id': 1}

# Test verify_user
is_valid = verify_user("wasim", "password123")
print(is_valid)  # Should print: True

is_valid = verify_user("wasim", "wrongpassword")
print(is_valid)  # Should print: False
