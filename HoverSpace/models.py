from pymongo import MongoClient

DB_NAME = 'hoverspace'
DATABASE = MongoClient()[DB_NAME]

USERS_COLLECTION = DATABASE.users
QUESTIONS_COLLECTION = DATABASE.questions
ANSWERS_COLLECTION = DATABASE.answers