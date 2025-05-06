import sqlite3

connection = sqlite3.connect('telegram_bot.db')
cursor = connection.cursor()

create_table_query = """
    CREATE TABLE IF NOT EXISTS users(
        id integer primary key,
        first_name text,
        last_name text,
        phone_number text,
        email text , 
        status integer,
        invite_link text,
        refrence_user_id integer,
        created_at date,
        updated_at date,
        deleted_at date
    );
"""

cursor.execute(create_table_query)
connection.commit()
connection.close()

