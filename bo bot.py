import telebot
from telebot import types

bot = telebot.TeleBot("6487950145:AAElH7_0tNkdiZXqR6UpWR4HaIrO6iznkQ0")

user_data = {}

asset_type = {}

brand = {}
brand_type = {}
asset_code = {}

brand_m = {}
brand_type_m = {}
asset_code_m = {}

brand_s = {}
asset_code_s = {}
ip = {}

brand_type_mapping = {
    'EDMI': ['MK6N', 'MK6E', 'MK10E', 'MK7B', 'MK7C', 'MK10', 'MK6', 'MK7MI', 'MK11'],
    'ACTARIS': ['SL7000'],
    'ITRON': ['CENTIAN', 'SL6000', 'SL7000A', 'NIAS DC', 'NIAS CT', 'ACE6000'],
    'WASION': ['iMeter 318', 'iMeter 310', 'aMeter 100'],
    'HEXING': ['HXE313-KP', 'HXE320', 'HXT300'],
    'SMI': ['SMI-3000'],
    'LANDIS+GYR': ['E550(ZMG)', 'E850(ZMD)'],
    'SCHENEIDER': ['ION7400', 'ION860'],
    'CEWE': ['PROMETER 100']
}

brand_type_mapping_m = {
    'EDMI': ['EWM100', 'IMDES', 'EWM100POD', 'TWM1000', 'EDMI02', 'TM87-SMART'],
    'WASION': ['WS-100', 'WS-18E', 'WS-18', 'WS-18F'],
    'MLIS': ['MLB-65-DC', 'MLB-G3001', 'MLB-S-65-RJ', 'MLB-G3002'],
    'SIERRA': ['GL6100'],
    'HEXING': ['HXM100', 'HXM200', 'HXM300'],
    'INTERCEL': ['SAM2W'],
    'MAESTRO': ['M1003GXT02'],
    'SIMCOM': ['T5320', 'T900'],
    'ROBUSTEL': ['MX1000XP'],
    'SANXING': ['CSI21', 'CSI21S', 'CSI21P'],
    'DeSkylink': ['DLS-T3', 'DLS-E'],
    'WAVECOM': ['MULTIBAND'],
    'ELIPS SYSTEM': ['NG-1']
}

brand_list_sim = ['TELKOMSEL', 'INDOSAT', 'XL', 'TRI', 'SMARTFREN']

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    markup.add(types.KeyboardButton('ASSET'), types.KeyboardButton('COMMISSIONING'))
    bot.send_message(message.chat.id, f"Halo {user.first_name}!\n"
                                      "Pilih salah satu opsi:", reply_markup=markup)

    bot.register_next_step_handler(message, choice)

def choice(message):
    user_data['choice'] = message.text
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, f"Anda telah memilih: {user_data['choice']}", reply_markup=markup)

    if user_data['choice'] == 'ASSET':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        markup.add(types.KeyboardButton('METER'), types.KeyboardButton('MODEM'), types.KeyboardButton('SIM'))
        bot.send_message(message.chat.id, "Pilih jenis asset:", reply_markup=markup)
        bot.register_next_step_handler(message, asset)
    elif user_data['choice'] == 'COMMISSIONING':
        commisioning(message)

def asset(message):
    user_data['asset'] = message.text
    asset_type[message.chat.id] = user_data['asset']

    if user_data['asset'] == 'METER':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        markup.add(*brand_type_mapping.keys())
        bot.send_message(message.chat.id, "Pilih jenis meter:", reply_markup=markup)
        bot.register_next_step_handler(message, meter)
    elif user_data['asset'] == 'MODEM':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        markup.add(*brand_type_mapping_m.keys())
        bot.send_message(message.chat.id, "Pilih jenis modem:", reply_markup=markup)
        bot.register_next_step_handler(message, modem)
    elif user_data['asset'] == 'SIM':
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        markup.add(*brand_list_sim)
        bot.send_message(message.chat.id, "Pilih jenis SIM:", reply_markup=markup)
        bot.register_next_step_handler(message, sim)
    else:
        print(f"Pilihan Asset: {user_data['asset']}")
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, f"Anda telah memilih: {user_data['asset']}", reply_markup=markup)
        bot.send_message(message.chat.id, "Percakapan selesai.")

def meter(message):
    user_data['meter'] = message.text
    brand[message.chat.id] = user_data['meter']

    if user_data['meter'] in brand_type_mapping:
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        brand_type_options = brand_type_mapping[user_data['meter']]
        markup.add(*brand_type_options)
        bot.send_message(message.chat.id, "Pilih jenis brand:", reply_markup=markup)
        bot.register_next_step_handler(message, set_brand_type)
    else:
        print(f"Pilihan Meter: {user_data['meter']}")
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, f"Anda telah memilih: {user_data['meter']}", reply_markup=markup)
        bot.send_message(message.chat.id, "Percakapan selesai.")

def set_brand_type(message):
    user_data['brand_type'] = message.text
    brand_type[message.chat.id] = user_data['brand_type']
    get_asset_code(message)

def get_asset_code(message):
    bot.send_message(message.chat.id, "Berapa Asset Codenya?")
    bot.register_next_step_handler(message, set_asset_code)

def set_asset_code(message):
    user_data['asset_code'] = message.text
    asset_code[message.chat.id] = user_data['asset_code']

    asset_type_info = asset_type[message.chat.id]
    brand_info = brand[message.chat.id]
    brand_type_info = brand_type[message.chat.id]
    asset_code_info = asset_code[message.chat.id]

    info_message = f"Menu : ASSET\nAsset Type : {asset_type_info}\nBrand : {brand_info}\nBrand Type : {brand_type_info}\nAsset Code : {asset_code_info}"
    bot.send_message(message.chat.id, info_message)
    bot.send_message(message.chat.id, "Percakapan selesai.")

def commisioning(message):
    user_data['commissioning'] = message.text
    print(f"Pilihan Commissioning: {user_data['commissioning']}")
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, f"Anda telah memilih: {user_data['commissioning']}", reply_markup=markup)
    bot.send_message(message.chat.id, "Percakapan selesai.")

def modem(message):
    user_data['modem'] = message.text
    brand_m[message.chat.id] = user_data['modem']

    if user_data['modem'] in brand_type_mapping_m:
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        brand_type_options = brand_type_mapping_m[user_data['modem']]
        markup.add(*brand_type_options)
        bot.send_message(message.chat.id, "Pilih jenis brand:", reply_markup=markup)
        bot.register_next_step_handler(message, set_brand_type_modem)
    else:
        print(f"Pilihan Modem: {user_data['modem']}")
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, f"Anda telah memilih: {user_data['modem']}", reply_markup=markup)
        bot.send_message(message.chat.id, "Percakapan selesai.")

def set_brand_type_modem(message):
    user_data['brand_type_modem'] = message.text
    brand_type_m[message.chat.id] = user_data['brand_type_modem']
    get_asset_code_modem(message)

def get_asset_code_modem(message):
    bot.send_message(message.chat.id, "Berapa Asset Codenya?")
    bot.register_next_step_handler(message, set_asset_code_modem)

def set_asset_code_modem(message):
    user_data['asset_code_modem'] = message.text
    asset_code_m[message.chat.id] = user_data['asset_code_modem']

    asset_type_info = asset_type[message.chat.id]
    brand_modem_info = brand_m[message.chat.id]
    brand_type_modem_info = brand_type_m[message.chat.id]
    asset_code_modem_info = asset_code_m[message.chat.id]

    info_message = f"Menu : ASSET\nAsset Type : {asset_type_info}\nBrand Modem : {brand_modem_info}\nBrand Type Modem : {brand_type_modem_info}\nAsset Code Modem : {asset_code_modem_info}"
    bot.send_message(message.chat.id, info_message)
    bot.send_message(message.chat.id, "Percakapan selesai.")

def get_ipul_ip(message):
    user_data['ipul_ip'] = message.text
    ip[message.chat.id] = user_data['ipul_ip']

    asset_type_info = asset_type[message.chat.id]
    brand_modem_info = brand_m[message.chat.id]
    brand_type_modem_info = brand_type_m[message.chat.id]
    asset_code_modem_info = asset_code_m[message.chat.id]
    ipul_ip_info = ip[message.chat.id]

    info_message = f"Menu : ASSET\nAsset Type : MODEM\nBrand Modem : {brand_modem_info}\nBrand Type Modem : {brand_type_modem_info}\nAsset Code Modem : {asset_code_modem_info}\nipul_ip : {ipul_ip_info}"
    bot.send_message(message.chat.id, info_message)
    bot.send_message(message.chat.id, "Percakapan selesai.")

def sim(message):
    user_data['sim'] = message.text
    brand_s[message.chat.id] = user_data['sim']

    if user_data['sim'] in brand_list_sim:
        bot.send_message(message.chat.id, "Berapa Asset Codenya?")
        bot.register_next_step_handler(message, get_asset_code_sim)
    else:
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, "Pilihan SIM tidak valid. Percakapan selesai.", reply_markup=markup)

def get_asset_code_sim(message):
    user_data['asset_code_sim'] = message.text
    asset_code_s[message.chat.id] = user_data['asset_code_sim']

    bot.send_message(message.chat.id, "Masukkan IP:")
    bot.register_next_step_handler(message, get_ip_sim)

def get_ip_sim(message):
    user_data['ip_sim'] = message.text
    ip[message.chat.id] = user_data['ip_sim']

    asset_type_sim_info = asset_type[message.chat.id]
    brand_sim_info = brand_s[message.chat.id]
    asset_code_sim_info = asset_code_s[message.chat.id]
    ip_sim_info = ip[message.chat.id]

    info_message = f"Menu : ASSET\nAsset Type : {asset_type_sim_info}\nBrand SIM : {brand_sim_info}\nAsset Code SIM : {asset_code_sim_info}\nIP SIM : {ip_sim_info}"
    bot.send_message(message.chat.id, info_message)
    bot.send_message(message.chat.id, "Percakapan selesai.")

bot.polling()
