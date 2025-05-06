import sqlite3


class channel:
    def __init__(self, db_file):
        self.db = db_file("telegram_bot")
        self.name = None
        self.Id = None
        connection = sqlite3.connect('telegram_bot.db')
        cursor = connection.cursor()


# telegram channels that usr joined
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_join_list(
        id integer primary key,
        user_id Integer, 
        channel_id inetegr,
        joined_at date
        );
        """

        cursor.execute(create_table_query)
        connection.commit()
        connection.close()

    def set_name(self, name):
        try:

            self.name = name
            self.db.insert("Channel", f"'{name}', NULL")
        except Exception as e:
            print("name error")

    def set_Id(self, Id):
        self.Id = Id
        self.db.update("Channel", f"Id={Id}", f"name='{self.name}'")

    def get_name(self):

        try:

            if self.name is None:
                self.name = self.db.select("Channel", "name")[0][0]
            return self.name
        except:
            print("...")

    def get_Id(self):
        if self.Id is None:
            self.Id = self.db.select("Channel", "Id")[0][0]
        return self.Id

    def save_to_db(self):
        self.db.insert("Channel", f"'{self.name}', {self.Id}")

    def load_from_db(self):
        rows = self.db.select("Channel", "name, Id")
        if rows:
            self.name, self.Id = rows[0]
            return self.name, self.Id

    def __str__(self):
        return f"channel {self.name} is {self.Id} years old"


# main-link
