import sqlite3
import hashlib
from datetime import datetime


def con():
    conn = sqlite3.connect('dtb1.db')
    return conn


def create_table_user():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists user(
            `id` integer not null primary key autoincrement,
            `first_name` varchar(30),
            `last_name` varchar(30),
            `email` varchar(50),
            `username` varchar(50),
            `password` varchar(150),
            `is_active` boolean default false,
            `registar_datetime` datetime
        )
    """)
    conn.commit()
    conn.close()


def insert_user(data: dict):
    conn = con()
    cur = conn.cursor()
    sha256 = hashlib.sha256()
    sha256.update(data['password1'].encode('utf-8'))
    hashed_password = sha256.hexdigest()
    query = """
        insert into user(`first_name`, `last_name`, `email`, `username`, `password`, `registar_datetime`)
        values(?, ?, ?, ?, ?, ?)
    """
    values = (data['first_name'], data['last_name'], data['email'], data['username'], hashed_password, datetime.now())
    if data['password1'] == data['password2']:
        if is_exists('username', data['username']):
            print('This username is already exists!!!')
            return 405
        if is_exists('email', data['email']):
            print('This email is already exists!!!')
            return 405
        cur.execute(query, values)
        conn.commit()
        conn.close()
        return 201
    else:
        print("Password are not same!!!")
        return 405

def login(data: dict):
    username = data['username']
    password = data['password']

    conn = con()
    cur = conn.cursor()
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    hashed_password = sha256.hexdigest()

    query = """
        select id from user where username=? and password=?
    """
    values = (username, hashed_password)
    cur.execute(query, values)
    dt = cur.fetchone()
    conn.close()
    return bool(dt[0])



def is_exists(field, field_data):
    query = f"""
        select count(id) from user where {field} = ?
    """
    value = (field_data,)
    conn = con()
    cur = conn.cursor()
    cur.execute(query, value)
    return cur.fetchone()[0]


def activate_user(data: dict):
    username = data['username']

    conn = con()
    cur = conn.cursor()

    query = """
            update user 
            set active=true where username=?
        """
    values = (username,)
    cur.execute(query, values)
    conn.commit()
    conn.close()
    return 200

