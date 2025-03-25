
import sqlite3
import bcrypt

class UserDatabase:
    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self.setup_database()

    def setup_database(self):
        """Create the database and users table if it doesn't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    hashed_password BLOB NOT NULL,
                    project TEXT NOT NULL
                )
            ''')
            conn.commit()

    def register_user(self, username, password, project):
        """Register a new user with a hashed password."""
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    INSERT INTO users (username, hashed_password, project)
                    VALUES (?, ?, ?)
                ''', (username, hashed_password, project))
                conn.commit()
                print(f"User '{username}' registered successfully!")
            except sqlite3.IntegrityError:
                print(f"Username '{username}' already exists.")

    def verify_user(self, username, password, project):
        """Verify user credentials during login."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT hashed_password, project FROM users WHERE username = ?
            ''', (username,))
            result = cursor.fetchone()

        if result:
            stored_hashed_password, stored_project = result
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password) and stored_project == project:
                return True
        return False

class UserLoginApp:
    def __init__(self):
        self.db = UserDatabase()

    def register_users(self):
        """Register some sample users."""
        self.db.register_user("user3", "pass123", "ProjectA")
        self.db.register_user("user4", "pass456", "ProjectB")

    def new_user_register(self):
        pass
        #TODO: Pending

    def check_users_registered(self):
        pass
        #"TODO": Pending

    def login(self):
        """Handle user login."""
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        project = input("Enter your project: ")

        if self.db.verify_user(username, password, project):
            print("Login successful! Access granted to the app.")
            return True
        else:
            print("Invalid username, password, or project. Access denied.")
            return False


#### Registered users #####
# uf.register_user("user1", "pass123", "ProjectA")
# uf.register_user("user2", "pass456", "ProjectB")
# uf.register_user('JulioAngulo', 'JA123', 'UDS_Champs')
# self.db.register_user("user3", "pass123", "ProjectA")
# self.db.register_user("user4", "pass456", "ProjectB")