import uuid
import time
import random
import Flask
from .databaser import create_database, insert_record, get_record, delete_record, list_records


developer_id = 0
admins_id = []
db = database
db_file = 'users.txt'
db.create_database(db_file)


def add_user(user_id, nickname=None, balance=10000, bissnes=None):
    db.insert_record(users, )