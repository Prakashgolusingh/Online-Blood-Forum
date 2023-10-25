import sqlite3

# Donor Validation Function

# if donor already exit
def is_donor_exist(email):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT email FROM donor WHERE email = ?", (email,))
    result = cursor.fetchone()
    connection.close()
    return result is not None

import sqlite3

def check_donor_password(email, password):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()

    # Use parameterized query to avoid SQL injection
    cursor.execute("SELECT * FROM donor WHERE email = ? AND password = ?", (email, password))
    result = cursor.fetchone()

    connection.close()
    return result is not None



# Hospital Validation Function
# if hospital already registered
def is_hospital_exist(email):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT email FROM hospital WHERE email = ?", (email,))
    result = cursor.fetchone()
    connection.close()
    return result is not None

def check_hospital_password(email, password):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()

    # Use parameterized query to avoid SQL injection
    cursor.execute("SELECT * FROM hospital WHERE email = ? AND password = ?", (email, password))
    result = cursor.fetchone()

    connection.close()
    return result is not None

# Admin Validation Function
def is_admin_exist(email):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT email FROM admin WHERE email = ?", (email,))
    result = cursor.fetchone()
    connection.close()
    return result is not None

def check_admin_password(email,password):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT email FROM admin WHERE email = ? AND password = ?", (email,password))
    result = cursor.fetchone()
    connection.close()
    return result is not None