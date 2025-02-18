import random
import uuid
import time
import random
import hashlib
from databaser import database


developer_id = 0
admins_id = []
table_name = "users"
db = database("data")
db.create_table('users', ['user_id', 'balance', 'nickname', 'bissnes', 'ident'])

def add_user():
    user_id = random.randint(10000000, 99999999)
    balance = 10000
    bissnes = None
    ident = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5,-1,-1)])
    nickname = 'User-' + str(random.randint(1000, 9999))
    db.insert(table_name, [
        {'user_id': user_id, 'balance': balance, 'nickname': nickname, 'bissnes': None, 'ident': ident}
    ])


def check_reg():
    ident = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5,-1,-1)])
    iterate_database
        if ident in db.select("users"):
            print('Your account was found in the system. You are already registered')

add_user()
check_reg()