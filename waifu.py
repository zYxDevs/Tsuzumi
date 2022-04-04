import telebot
from dotenv import load_dotenv
import os
import requests

load_dotenv()
token = os.getenv('TOKEN')

bot = telebot.TeleBot(token)

def get_url():
    contents = requests.get('https://api.waifu.pics/sfw/waifu/').json()
    image_url = contents['url']
    return image_url

@bot.message_handler(commands = ['greet','start', 'help'])
def greet(message):
    msg = ''' Hi, I'm the Waifu bot
    
    
Send /waifu to get an random waifu image. '''
    bot.send_message(message.chat.id, msg) 

@bot.message_handler(commands = ['waifu'])
@bot.message_handler(regexp=r'waifu')
def meow(message):
    url = get_url()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(func=lambda m: True)
def repeat(message):
    bot.send_message(message.chat.id, message.text)

def main():
    bot.polling()

if __name__ == '__main__':
    main()
