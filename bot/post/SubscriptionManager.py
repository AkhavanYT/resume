import sys
import telebot
import requests
import re
from telebot import TeleBot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
import sqlite3
import psycopg2
from telebot import TeleBot, types
from telegram.ext import Updater, CommandHandler, MessageHandler
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup , KeyboardButton 
from telebot.types import ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import hashlib
import uuid
# Create a Telegram bot instance using your bot token (replace with your actual token)
bot = telebot.TeleBot("6771369229:AAGAcldhpExOWMtEM8eAz4bDkmbxM5Z9f8U")

# first we need to check that user is new or old 
# to not increase scores twice

# check user mobile when start the bot

# check user invite link
# if the link is existed in user table: 
db_name = 'telegram_bot.db'

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

        self.cursor = None
    
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
    
    def close(self):
        if self.connection is not None:
            self.cursor.close()
            self.connection.close()
            self.connection = None
            self.cursor = None
 
    def connect_to_db(self):
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user_links (
                                 user_id INTEGER PRIMARY KEY,
                                 user_link TEXT UNIQUE
                             )''')
        self.connection.commit()
        self.close()
        
    def get_user_link(self,user_id):
        self.connect_to_db()
        self.cursor.execute('SELECT user_link FROM user_links WHERE user_id = ?', (user_id,))
        user_link = self.cursor.fetchone()
        self.close()
        if self.user_link:
            return user_link[0]
        else:
            return None
    
    def create_user_link(self, user_id):
        user_hash = hashlib.sha256(str(user_id).encode('utf-8')).hexdigest()
        user_link = f"https://t.me/micro2024bot/?start={user_hash}"

        self.connect()
        self.cursor.execute('INSERT INTO user_links (user_id, user_link) VALUES (?, ?)', (user_id, user_link))
        self.connection.commit()
        self.close()

        return user_link     

def create_user_link(user_id):
    db_manager = DatabaseManager('telegram_bot.db')
    user_link = db_manager.create_user_link(user_id)
    return user_link

def get_user_link(user_id):
    db_manager = DatabaseManager('telegram_bot.db')
    user_link = db_manager.get_user_link(user_id)
    return user_link

def handle_start_command(message):
    user_id = message.chat.id
    db_manager = DatabaseManager('telegram_bot.db')
    user_link = db_manager.get_user_link(user_id)
    if not user_link:
        user_link = db_manager.create_user_link(user_id)

    print(f"لینک کاربری شما: {user_link}")  # Print the user link
    bot.send_message(user_id, f"لینک کاربری شما: {user_link}")


def send_message(user_id, text, reply_markup=None):
    bot.send_message(user_id, text, reply_markup=reply_markup)
  
@bot.message_handler(commands=['start'])
def start_message_handler(message):
    bot.send_message(message.chat.id,"hiii")
    handle_start_command(message)  # آرگومان db_name حذف شد

bot.polling()