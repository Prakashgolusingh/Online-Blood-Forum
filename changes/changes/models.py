import sqlite3
import os
def init_db():
    if not os.path.isfile('Database.sqlite'):
        connection = sqlite3.connect('Database.sqlite')
        cursor = connection.cursor()

        query = '''
            PRAGMA foreign_keys = ON;

            CREATE TABLE donor (
                email TEXT PRIMARY KEY UNIQUE,
                name TEXT,
                age TEXT,
                gender TEXT,
                state TEXT,
                district TEXT,
                blood_group TEXT,
                contact Text,
                password TEXT
            );

            CREATE TABLE hospital (
                email TEXT PRIMARY KEY UNIQUE,
                name TEXT,
                license_no TEXT UNIQUE,
                district TEXT,
                state TEXT,
                contacts TEXT,
                password TEXT
            );

            CREATE TABLE availableBlood (
                id TEXT PRIMARY KEY,
                O_positive INTEGER DEFAULT 0,
                O_negative INTEGER DEFAULT 0,
                AB_positive INTEGER DEFAULT 0,
                AB_negative INTEGER DEFAULT 0,
                B_negative INTEGER DEFAULT 0,
                B_positive INTEGER DEFAULT 0,
                A_negative INTEGER DEFAULT 0,
                A_positive INTEGER DEFAULT 0,
                FOREIGN KEY (id) REFERENCES hospital (email)
            );

            CREATE TABLE camp (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                hospital_id TEXT,
                name TEXT DEFAULT 'camp',
                location TEXT DEFAULT 'hospital',
                date DATE DEFAULT (date('now', '+7 days')),
                no_of_donrs INTEGER DEFAULT 0,
                FOREIGN KEY (hospital_id) REFERENCES hospital(email)
            );

            CREATE TABLE campRegistered (
                donor_id TEXT,
                hospital_id TEXT,
                camp_id INTEGER,
                status TEXT,
                FOREIGN KEY (donor_id) REFERENCES donor(email),
                FOREIGN KEY (hospital_id) REFERENCES hospital(email),
                FOREIGN KEY (camp_id) REFERENCES camp(id)
            );

            CREATE TABLE admin (
                email TEXT PRIMARY KEY,
                password TEXT,
                name TEXT
            );

        '''

        cursor.executescript(query)
        cursor.close()
        connection.close()


def insert_donor(email, name, age, gender, state, district, blood_group, contact, password):
    connection = sqlite3.connect('Database.sqlite')
    cursor = connection.cursor()

    query = """
    INSERT INTO donor (email, name, age, gender, state, district, blood_group, contact, password)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(query, (email, name, age, gender, state, district, blood_group, contact, password))
    
    connection.commit()
    cursor.close()
    connection.close()

def insert_hospital(email, name, license_no, district, state, contacts, password):
    connection = sqlite3.connect('Database.sqlite')
    cursor = connection.cursor()

    query = """
    INSERT INTO hospital (email, name, license_no, district, state, contacts, password)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(query, (email, name, license_no, district, state, contacts, password))
    
    connection.commit()
    cursor.close()
    connection.close()

def insert_camp(hospital_id, name, location, date, no_of_donors):
    connection = sqlite3.connect('Database.sqlite')
    cursor = connection.cursor()

    query = """
    INSERT INTO camp (hospital_id, name, location, date, no_of_donors)
    VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(query, (hospital_id, name, location, date, no_of_donors))

    connection.commit()
    cursor.close()
    connection.close()

def insert_available_blood(id, O_positive, O_negative, AB_positive, AB_negative, B_negative, B_positive, A_negative, A_positive):
    connection = sqlite3.connect('Database.sqlite')
    cursor = connection.cursor()

    query = """
    INSERT INTO availableBlood (id, O_positive, O_negative, AB_positive, AB_negative, B_negative, B_positive, A_negative, A_positive)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(query, (id, O_positive, O_negative, AB_positive, AB_negative, B_negative, B_positive, A_negative, A_positive))

    connection.commit()
    cursor.close()
    connection.close()


def insert_camp_registered(donor_id, hospital_id, camp_id, status):
    connection = sqlite3.connect('Database.sqlite')
    cursor = connection.cursor()

    query = """
    INSERT INTO campRegistered (donor_id, hospital_id, camp_id, status)
    VALUES (?, ?, ?, ?)
    """
    cursor.execute(query, (donor_id, hospital_id, camp_id, status))

    connection.commit()
    cursor.close()
    connection.close()

def insert_admin(email, password, name):
    connection = sqlite3.connect('Database.sqlite')
    cursor = connection.cursor()

    query = """
    INSERT INTO admin (email, password, name)
    VALUES (?, ?, ?)
    """
    cursor.execute(query, (email, password, name))

    connection.commit()
    cursor.close()
    connection.close()

# fetch donor from email id.
def get_donor_by_email(email):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM donor WHERE email = ?", (email,))
    donor = cursor.fetchone()
    connection.close()
    return donor

def get_hospital_by_email(email):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hospital WHERE email = ?", (email,))
    hospital = cursor.fetchone()
    connection.close()
    return hospital

def get_admin_by_email(email):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM admin WHERE email = ?", (email,))
    admin = cursor.fetchone()
    connection.close()
    return admin

def get_all_hospitals():
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hospital")
    hospitals = cursor.fetchall()
    connection.close()
    return hospitals

def get_hospitals_count():
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM hospital")
    count = cursor.fetchall()
    connection.close()
    return count

def get_all_donors():
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM donor")
    donors = cursor.fetchall()
    connection.close()
    return donors

def get_donors_count():
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) FROM donor")
    count = cursor.fetchall()
    connection.close()
    return count

# Function to delete a hospital by email
def delete_hospital_by_email(email):
    try:
        conn = sqlite3.connect('database.sqlite')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM hospital WHERE email = ?", (email,))
        conn.commit()
        conn.close()
        return True  # Return True on successful deletion
    except sqlite3.Error as e:
        print("Error deleting hospital:", e)
        return False  # Return False on error

# Function to delete a donor by email
def delete_donor_by_email(email):
    try:
        conn = sqlite3.connect('database.sqlite')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM donor WHERE email = ?", (email,))
        conn.commit()
        conn.close()
        return True  # Return True on successful deletion
    except sqlite3.Error as e:
        print("Error deleting donor:", e)
        return False  # Return False on error

from flask import flash

def update_hospital_profile(email, name, contact):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('database.sqlite')
        cursor = conn.cursor()

        # Update the hospital's profile in the database
        cursor.execute("UPDATE hospital SET name = ?, contact = ? WHERE email = ?", (name, contact, email))
        conn.commit()

        flash('Your profile has been updated successfully', 'success')

    except Exception as e:
        # Handle exceptions, log errors, or display error messages as needed
        flash('An error occurred while updating your profile. Please try again later.', 'danger')
    finally:
        # Close the database connection, regardless of success or failure
        if conn:
            conn.close()


# Sankhanil

def search_camps_backend(state, district, donor_id = None):
    conn = sqlite3.connect('Database.sqlite')
    cursor = conn.cursor()

    query = ''
    res = None
    if donor_id != None:
        query = '''
            SELECT c.id, h.name, c.name, c.date, c.no_of_donrs, h.contacts FROM camp c
            JOIN hospital h ON c.hospital_id = h.email
            WHERE hospital_id IN (
                SELECT email FROM hospital
                WHERE state = ? AND district = ?) AND
            c.id NOT IN (
                SELECT camp_id from campRegistered WHERE donor_id = ?
            );
        '''
        res = cursor.execute(query, (state, district, donor_id))
    else:
        query = '''
            SELECT c.id, h.name, c.name, c.date, c.no_of_donrs, h.contacts FROM camp c
            JOIN hospital h ON c.hospital_id = h.email
            WHERE hospital_id IN (
                SELECT email FROM hospital
                WHERE state = ? AND district = ?);
        '''
        res = cursor.execute(query, (state, district))

    data = res.fetchall()

    conn.close()

    return data


def register_into_camp(donor_id, hospital_id, camp_id):
    conn = sqlite3.connect('Database.sqlite')
    cursor = conn.cursor()

    res = cursor.execute('INSERT INTO campRegistered VALUES(?, ?, ?, ?)', (donor_id, hospital_id, camp_id, 'Awaited'))

    conn.commit()
    conn.close()


def get_donor_past_camps(donor_id):
    conn = sqlite3.connect('Database.sqlite')
    cursor = conn.cursor()

    query = '''
        SELECT c.name, c.date, h.name, h.state, h.district, r.status FROM campRegistered r
        JOIN camp c ON r.camp_id = c.id
        JOIN hospital h ON h.email = c.hospital_id
        WHERE r.donor_id = ?
        AND DATE(c.date) < DATE('now');
    '''
    res = cursor.execute(query, (donor_id, ))
    rows = res.fetchall()

    conn.close()

    return rows


def view_registered_upcoming_camps(donor_id):
    conn = sqlite3.connect('Database.sqlite')
    cursor = conn.cursor()

    res1 = cursor.execute('''
        SELECT c.name, c.date, h.name, h.contacts, h.state, h.district FROM campRegistered r 
        JOIN camp c ON r.camp_id = c.id
        JOIN hospital h ON h.email = c.hospital_id
        WHERE r.donor_id = ?
        AND DATE(c.date) >= DATE('now')
        AND status = 'Awaited';
    ''', (donor_id, ))
    awaited_rows = res1.fetchall()

    res2 = cursor.execute('''
        SELECT c.name, c.date, h.name, h.contacts, h.state, h.district FROM campRegistered r 
        JOIN camp c ON r.camp_id = c.id
        JOIN hospital h ON h.email = c.hospital_id
        WHERE r.donor_id = ?
        AND DATE(c.date) >= DATE('now')
        AND status = 'Accepted';
    ''', (donor_id, ))
    accepted_rows = res2.fetchall()

    res3 = cursor.execute('''
        SELECT c.name, c.date, h.name, h.contacts, h.state, h.district FROM campRegistered r 
        JOIN camp c ON r.camp_id = c.id
        JOIN hospital h ON h.email = c.hospital_id
        WHERE r.donor_id = ?
        AND DATE(c.date) >= DATE('now')
        AND status = 'Rejected';
    ''', (donor_id, ))
    rejected_rows = res3.fetchall()

    conn.close()

    return awaited_rows, accepted_rows, rejected_rows