import requests
from telebot import TeleBot

TOKEN = ''
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['wallpapers'])
def wall(message):
    url = 'https://nekos.life/api/v2/img/wallpaper'
    r = requests.get(url, allow_redirects=True)
    r.headers
    json = r.json()
    pussyurl = json['url']
    rs = requests.get(pussyurl, allow_redirects=True)
    open('wallpaper.png', 'wb').write(rs.content)
    bot.send_photo(message.chat.id, open("wallpaper.png", "rb"))
    bot.send_document(message.chat.id, open("wallpaper.png", "rb"))
bot.polling()