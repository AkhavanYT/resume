import sqlite3

connection = sqlite3.connect('telegram_bot.db')
cursor = connection.cursor()


# score for each user based on telegram score filed
create_table_query = """
    CREATE TABLE IF NOT EXISTS user_scores(
        id integer primary key,
        user_id integer,
        score integer , 
        invited_count integer
        
    );
"""

cursor.execute(create_table_query)
connection.commit()
connection.close()
