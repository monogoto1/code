!pip install pyTelegramBotAPI
import telebot
from telebot import types
import datetime
bot = telebot.TeleBot("5569274669:AAEf7WkX2wvodw3aFDZbB_asd9c6kcEKH7w")
user_var = {}
user_var_status = {}
def all_false():
  for key in user_var_status.keys():
    user_var_status[key] = False
def one_true(argument):
  user_var_status[argument] = True
def one_false(argument):
    user_var_status[argument] = False

day_today = None
test = None
keyboard = None

@bot.message_handler(commands=["start"])
def start(message):
  global test
  global day_today
  global user_var
  global keyboard
  test = message.from_user.id
  day_today = datetime.date.today()
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
  keyboard.row('Відтискання', 'Кегель', 'Підтягування', 'Біцепс')
  keyboard.row('Присідання', 'Жим', 'Армійський')
  keyboard.row('Статистика', 'Новий день')
  bot.send_message(message.chat.id, "Привіт, я створений для того, щоб ти міг записувати свої досягнення", reply_markup=keyboard)
  if test not in user_var:
    user_var[test] = {}
  global user_var_status
  user_var_status = {
    'vidtisk_set': False,
    'kegel_set': False,
    'pidtag_set': False,
    'biceps_set': False,
    'prysid_set': False,
    'bnchpress_set': False,
    'overhead_set': False,
    'peredlast': False
  }
  user_var[test][str(day_today)] = {
    'vidtisk': 0,
    'kegel': 0,
    'pidtag': 0,
    'biceps': 0,
    'prysid': 0,
    'bnchpress': 0,
    'overhead': 0
}


@bot.message_handler(func=lambda message: message.text == 'Назад')
def back(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
  keyboard.row('Відтискання', 'Кегель', 'Підтягування', 'Біцепс')
  keyboard.row('Присідання', 'Жим', 'Армійський')
  keyboard.row('Статистика', 'Новий день')
  bot.send_message(message.chat.id, 'Головна сторінка', reply_markup=keyboard)
  all_false()

@bot.message_handler(func=lambda message: message.text == 'Статистика')
def statfn(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
  keyboard.row('Сьогодні', 'Інші дні')
  keyboard.row('Назад')
  bot.send_message(message.chat.id, 'Оберіть ту статистику, яку хочете дізнатися', reply_markup=keyboard)
@bot.message_handler(func=lambda message: message.text == 'Сьогодні')
def lastt(message):
  a = user_var[message.from_user.id][str(day_today)]['vidtisk']
  b = user_var[message.from_user.id][str(day_today)]['kegel']
  c = user_var[message.from_user.id][str(day_today)]['pidtag']
  d = user_var[message.from_user.id][str(day_today)]['biceps']
  e = user_var[message.from_user.id][str(day_today)]['prysid']
  f = user_var[message.from_user.id][str(day_today)]['bnchpress']
  g = user_var[message.from_user.id][str(day_today)]['overhead']
  bot.send_message(message.chat.id, f"Ви виконали {a} віджимань")
  bot.send_message(message.chat.id, f"Ви виконали {b} вправ кегеля")
  bot.send_message(message.chat.id, f"Ви виконали {c} підтягувань")
  bot.send_message(message.chat.id, f"Ви підняли {d} кг біцепсом")
  bot.send_message(message.chat.id, f"Ви підняли додатково {e} кг присіданнями")
  bot.send_message(message.chat.id, f"Ви підняли {f} кг армійським")
  bot.send_message(message.chat.id, f"Ви виконали {g} ", reply_markup=keyboard)
@bot.message_handler(func=lambda message: message.text == 'Інші дні')
def peredlastt(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
  keyboard.row('Назад')
  bot.send_message(message.chat.id, 'Ось всі ваші дні')
  for a in user_var[test]:
    bot.send_message(message.chat.id, f"{a}")
  bot.send_message(message.chat.id, 'Оберіть той день, який вас цікавить', reply_markup=keyboard)
  one_true('peredlast')
@bot.message_handler(func=lambda message: user_var_status['peredlast'])
def day_x(message):
  answer = message.text
  keyboard.row('Назад')
  try:
    a = user_var[message.from_user.id][str(answer)]['vidtisk']
    b = user_var[message.from_user.id][str(answer)]['kegel']
    c = user_var[message.from_user.id][str(answer)]['pidtag']
    d = user_var[message.from_user.id][str(answer)]['biceps']
    e = user_var[message.from_user.id][str(answer)]['prysid']
    f = user_var[message.from_user.id][str(answer)]['bnchpress']
    g = user_var[message.from_user.id][str(answer)]['overhead']
    bot.send_message(message.chat.id, f"Ви виконали {a} віджимань")
    bot.send_message(message.chat.id, f"Ви виконали {b} вправ кегеля")
    bot.send_message(message.chat.id, f"Ви виконали {c} підтягувань")
    bot.send_message(message.chat.id, f"Ви підняли {d} кг біцепсом")
    bot.send_message(message.chat.id, f"Ви підняли додатково {e} кг присіданнями")
    bot.send_message(message.chat.id, f"Ви підняли {f} кг жимом")
    bot.send_message(message.chat.id, f"Ви підняли {g} кг армійським", reply_markup=keyboard)
  except:
    bot.send_message(message.chat.id, 'Даної дати не знайдено', reply_markup=keyboard)
  one_false('peredlast')
@bot.message_handler(func=lambda message: message.text == 'Новий день')
def new_day(message):
  global day_today
  day_today = datetime.date.today()
  bot.send_message(message.chat.id, 'Встановлено нагальну дату', reply_markup=keyboard)
@bot.message_handler(func=lambda message: message.text == 'Відтискання')
def vidtiskfn(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
  keyboard.row('Назад')
  bot.send_message(message.chat.id, 'Введіть кількість відтискань', reply_markup=keyboard)
  one_true('vidtisk_set')


@bot.message_handler(func=lambda message: user_var_status['vidtisk_set'])
def handle_vidtisk(message):
  try:
    num = int(message.text)
    user_var[message.from_user.id][str(day_today)]['vidtisk'] = user_var[message.from_user.id][str(day_today)]['vidtisk']+num
    bot.send_message(message.chat.id, 'Кількість відтискань була успішно збільшена на {}'.format(num), reply_markup=keyboard)
  except ValueError:
    bot.send_message(message.chat.id, 'Це не число')
  one_false('vidtisk_set')


@bot.message_handler(func=lambda message: message.text == 'Кегель')
def kegelfn(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
  keyboard.row('Назад')
  bot.send_message(message.chat.id,'Введіть кількість повторів', reply_markup=keyboard)
  one_true('kegel_set')


@bot.message_handler(func=lambda message: user_var_status['kegel_set'])
def handle_kegel(message):
  try:
    num = int(message.text)
    user_var[message.from_user.id][str(day_today)]['kegel'] = user_var[message.from_user.id][str(day_today)]['kegel'] + num
    bot.send_message(message.chat.id,'Кількість вправ кегеля була успішно збільшена на {}'.format(num), reply_markup=keyboard)
  except ValueError:
    bot.send_message(message.chat.id, 'Це не число')
  one_false('kegel_set')


@bot.message_handler(func=lambda message: message.text == 'Підтягування')
def pidtagfn(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
  keyboard.row('Назад')
  bot.send_message(message.chat.id,'Введіть кількість підтягувань', reply_markup=keyboard)
  one_true('pidtag_set')



@bot.message_handler(func=lambda message: user_var_status['pidtag_set'])
def handle_pidtag(message):
  try:
    num = int(message.text)
    user_var[message.from_user.id][str(day_today)]['pidtag'] = user_var[message.from_user.id][str(day_today)]['pidtag'] + num
    bot.send_message(message.chat.id, 'Кількість підтягувань була успішно збільшена на {}'.format(num), reply_markup=keyboard)
  except ValueError:
    bot.send_message(message.chat.id, 'Це не число')
  one_false('pidtag_set')

@bot.message_handler(func=lambda message: message.text == 'Біцепс')
def bicepsfn(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
  keyboard.row('Назад')
  bot.send_message(message.chat.id, 'Введіть загальну кількість піднятих кг', reply_markup=keyboard)
  one_true('biceps_set')

@bot.message_handler(func=lambda message: user_var_status['biceps_set'])
def handle_biceps(message):
  try:
    num = int(message.text)
    user_var[message.from_user.id][str(day_today)]['biceps'] = user_var[message.from_user.id][str(day_today)]['biceps'] + num
    bot.send_message(message.chat.id, 'Кількість піднятих кг біцепсом була успішно збільшена на {}'.format(num), reply_markup=keyboard)
  except ValueError:
    bot.send_message(message.chat.id, 'Це не число')
  one_false('biceps_set')

@bot.message_handler(func=lambda message: message.text == 'Присідання')
def prysidfn(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
  keyboard.row('Назад')
  bot.send_message(message.chat.id, 'Введіть кількість загальну кількість кг присядів', reply_markup=keyboard)
  one_true('prysid_set')

@bot.message_handler(func=lambda message: user_var_status['prysid_set'])
def handle_prysid(message):
  try:
    num = int(message.text)
    user_var[message.from_user.id][str(day_today)]['prysid'] = user_var[message.from_user.id][str(day_today)]['prysid'] + num
    bot.send_message(message.chat.id, 'Кількість додаткових піднятих кг присядами була успішно збільшена на {}'.format(num), reply_markup=keyboard)
  except ValueError:
    bot.send_message(message.chat.id, 'Це не число')
  one_false('prysid_set')


@bot.message_handler(func=lambda message: message.text == 'Жим')
def bnchpressfn(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
  keyboard.row('Назад')
  bot.send_message(message.chat.id, 'Введіть кількість кг жиму', reply_markup=keyboard)
  one_true('bnchpress_set')


@bot.message_handler(func=lambda message: user_var_status['bnchpress_set'])
def handle_bnchpress(message):
  try:
    num = int(message.text)
    user_var[message.from_user.id][str(day_today)]['bnchpress'] = user_var[message.from_user.id][str(day_today)]['bnchpress'] + num
    bot.send_message(message.chat.id, 'Кількість кг жиму була успішно збільшена на {}'.format(num), reply_markup=keyboard)
  except ValueError:
    bot.send_message(message.chat.id, 'Це не число')
  one_false('bnchpress_set')


@bot.message_handler(func=lambda message: message.text == 'Армійський')
def overheadfn(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
  keyboard.row('Назад')
  bot.send_message(message.chat.id, 'Введіть кількість піднятих кг армійським', reply_markup=keyboard)
  one_true('overhead_set')

@bot.message_handler(func=lambda message: user_var_status['overhead_set'])
def handle_overhead(message):
  try:
    num = int(message.text)
    user_var[message.from_user.id][str(day_today)]['overhead'] = user_var[message.from_user.id][str(day_today)]['overhead'] + num
    bot.send_message(message.chat.id, 'Кількість піднятих кг армійським була успішно збільшена на {}'.format(num), reply_markup=keyboard)
  except ValueError:
    bot.send_message(message.chat.id, 'Це не число')
  one_false('overhead_set')


bot.polling(none_stop=True)