import sqlite3

connection = sqlite3.connect('telegram_bot.db')
cursor = connection.cursor()



# telegram channels that usr joined
create_table_query = """
    CREATE TABLE IF NOT EXISTS user_join_list(
        id integer primary key,
        user_id integer, 
        channel_id inetegr,
        joined_at date
    );
"""

cursor.execute(create_table_query)
connection.commit()
connection.close()
