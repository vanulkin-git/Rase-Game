import random
import uuid
import time
import random
import hashlib
from databaser import database
import os
from rich import print
from rich.console import Console
from rich.progress import Progress


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
    os.system('cls')
    result_reg = check_reg()
    if result_reg:
        result_reg, nickname = check_reg()
        print(f'{nickname}, welcome!\nI am a Rase game bot\n📚 I am very rich in various teams that you can use to pass your time by yourself or with your friends.\n❓ You can find out all the commands through the \033[33m"help"\033[0m command')
        wait_commads('start')
    else:
        add_user()
        print(f'{nickname}, welcome!\nI am a Rase game bot\n📚 I am very rich in various teams that you can use to pass your time by yourself or with your friends.\n❓ You can find out all the commands through the \033[33m"help"\033[0m command')
        wait_commads('start')


def help(nickname):
    print(f'❓ {nickname}, select the appropriate help section:\n\tDeveloper - 1\tHow to play - 2\n\tRules - 3\tCommands - 4')
    choose = int(input('--> '))
    try:
        if choose == 1:
            print("Developer's contacts:\n Telegram - @vanulkin\n GitHub - vanulkin-git\n\nReturn to help - r\tClear - c\tHelp - h")
            wait_commads('help')
        elif choose == 2:
            print('[link={"https://teletype.in/@che33333/xy7xknM5UDn"}]Game Guide[/link] or Basics for Beginners - https://teletype.in/@che33333/xy7xknM5UDn\n\nReturn to help - r\tClear - c\tHelp - h')
            wait_commads('help')
        elif choose == 3:
            print('You can read all the rules of the project here - https://teletype.in/@vanulkin/rules_rase\n\nReturn to help - r\tClear - c\tHelp - h')
            wait_commads('help')
        elif choose == 4:
            print(f'{nickname}, commands:\n\tMAIN - 1\tEARNING - 2\n\tGAMES - 3\tOTHER - 4')
            cat_command = int(input('--> '))
            cat_commands(cat_command)
    except:
        wait_commads(choose)


def cat_commands(cat_command):
    if cat_command == 1:
        print('👤 Профиль (проф) - просмотр профиля\n🔖 Сменить ник [новый ник]\n💵 Баланс (б)\n🤝 Передать - перевод денег\n🤝 Дать - перевод денег без айди\n🎟 Пасс\n🏦 Банк\n💸 Депозит\n⛏️ Кирка\n🔖 Сертификаты\n👍 Поинты (временная акция)\n📜 Квесты\n👑 Рейтинг\n🌌 Плазма\n🤴🏻 Король\n🪄 Палочки\n✈️ Перелёт\n⚔️ Клан\n🦊 Мой питомец\n🏆 Опыт\n🎁 Бонус\n⭐️ Топ — лучшие игроки!\n🧛 Вампир\n🛍 Магазин')
    elif command == 2:
        print('🏦 Банк\n📷 Ютуб - создай свой канал!\n📱 Тикток - заработай на видео!\n💼 Бизнесы\n💱 Курс биткоина\n👨‍💻 Работы\n🎣 Рыбалка\n📻 Фермы\n🏙 Город - создай свой город!\n🛥 Круиз\n🐠 Дайвинг\n🏹 Охота\n🪖 Шахта\n🛋 Крафт\n🌾 Грядка\n💃 Показ моды\n🚧 Раскопки\n🚕 Таксовать\n🏡 Аренда - заработок на имуществе')
    elif command == 3:
        print('🎰 Казино [сумма]\n🍓 Спин [ставка]\n📦 Кейсы\n🗳 Бочка\n🎟 Лотерея\n🚪 Дверь\n🔑 Сейф [число]\n🎲 Кубик [число 1-6]\n🏹 Босс\n🎯 Дартс [ставка]\n🏀 Баскетбол [ставка]\n❌ Крестики\n✂️ КНБ\n📈 Инвестиции\n📊 Трейд\n🎳 Боулинг [ставка]\n🏁 Гонка [ставка]\n🔫 Рулетка [ставка]\n🪙 Монетка [орел/решка]\n🔐 Хакнуть\n🧪 Эликсиры\n🔴 РР\n💣 Поле\n🏖 Клад\n🍹 Зелья')
    elif command == 4:
        print('🪙 Донат\n🐲 Босс\n🛢 Заправка\n📨 СМСКИ\n🏪 Рынок\n🧛 Вампир\n🌐 Курс биткоина\n🧞‍♂️ Гендер\n🔮 Алтарь\n🎁 Промо создать\n💞 Брак\n🎁 Подарок\n🏡 Садовод')

    wait_commads('help')


def wait_commads(previous_action, command=None):
    print('----------------------------------------------')
    print('----------------------------------------------')
    ident = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5,-1,-1)])
    results = db.select(table_name, condition=lambda record: record.get("ident") == ident)
    nickname = results[0].get("nickname")
    if command is None:
        command = input('--> ')

    if command in ('c', 'clear'):
        os.system('cls')
    if command in ('help', 'h'):
        help(nickname)
    if command in('return', 'r'):
        if previous_action in globals():
            func = globals()[previous_action]
            func(nickname)
    if command in ('b', 'balance'):
        print(f'{nickname}, your balance:\n\t')

start()