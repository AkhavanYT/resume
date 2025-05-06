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

