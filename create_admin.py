
from app import get_db, create_tables
from werkzeug.security import generate_password_hash
from getpass import getpass
import sqlite3


create_tables()

print("\n===== CREATE ADMIN ACCOUNT =====\n")

username = input("Enter admin username: ").strip()
password = getpass("Enter admin password: ")
confirm = getpass("Confirm password: ")

if len(username) < 3:
    print("Username must have at least 3 characters.")

elif len(password) < 8:
    print("Password must have at least 8 characters.")

elif password != confirm:
    print("Passwords do not match.")

else:

    conn = get_db()

    try:

        password_hash = generate_password_hash(password)

        conn.execute("""
            INSERT INTO users
            (username, password_hash, role)
            VALUES (?, ?, 'admin')
        """, (username, password_hash))

        conn.commit()

        print("\nAdmin account created successfully!")

    except sqlite3.IntegrityError:
        print("\nThis username already exists.")

    finally:
        conn.close()
