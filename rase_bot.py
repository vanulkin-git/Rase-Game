import random
import uuid
import time
import random
import hashlib
from databaser import database
import os


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
    return nickname


def check_reg():
    ident = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5,-1,-1)])
    results = db.select(table_name, condition=lambda record: record.get("ident") == ident)
    if results:
        nickname = results[0].get("nickname")
        return True, nickname
    else:
        return False


def start():
    result_reg, nickname = check_reg()
    if result_reg:
        print(f'{nickname}, welcome!\nI am a Rase game bot\n📚 I am very rich in various teams that you can use to pass your time by yourself or with your friends.\n❓ You can find out all the commands through the \033[33m"help"\033[0m command')
    else:
        add_user()
        print(f'{nickname}, welcome!\nI am a Rase game bot\n\n📚 I am very rich in various teams that you can use to pass your time by yourself or with your friends.\n❓ You can find out all the commands through the \033[33m"help"\033[0m command')


def help(nickname):
    print(f'❓ {nickname}, select the appropriate help section:\n\tDeveloper - 1\tHow to play - 2\n\tRules - 3\tCommands - 4')
    choose = int(input('--> '))
    if choose == 1:
        print("Developer's contacts:\n Telegram - @vanulkin\n GitHub - vanulkin-git\n\nReturn to help - r\tClear - c\tHelp - h")


help('123')