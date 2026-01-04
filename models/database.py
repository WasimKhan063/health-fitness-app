# In-memory database for users
users_db = {}

def add_user(username, email, password):
    """Add a new user to database"""
    if username in users_db:
        return None  # User already exists
    
    users_db[username] = {
        'email': email,
        'password': password,
        'id': len(users_db) + 1
    }
    return users_db[username]

def get_user(username):
    """Get user from database"""
    return users_db.get(username)

def verify_user(username, password):
    """Verify username and password"""
    user = users_db.get(username)
    if not user:
        return False
    return user['password'] == password
