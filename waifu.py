import telebot
from dotenv import load_dotenv
import os
import requests

load_dotenv()
token = os.getenv('TOKEN')

bot = telebot.TeleBot(token)

def get_url():
    contents = requests.get('https://api.waifu.pics/sfw/waifu').json()
    image_url = contents['url']
    return image_url

def get_nekourl():
    contents = requests.get('https://api.waifu.pics/sfw/neko').json()
    image_url = contents['url']
    return image_url

def get_shinobuurl():
    contents = requests.get('https://api.waifu.pics/sfw/shinobu').json()
    image_url = contents['url']
    return image_url

def get_meguminurl():
    contents = requests.get('https://api.waifu.pics/sfw/megumin').json()
    image_url = contents['url']
    return image_url

def get_kissurl():
    contents = requests.get('https://api.waifu.pics/sfw/kiss').json()
    image_url = contents['url']
    return image_url

def get_lickurl():
    contents = requests.get('https://api.waifu.pics/sfw/lick').json()
    image_url = contents['url']
    return image_url

def get_nwaifuurl():
    contents = requests.get('https://api.waifu.pics/nsfw/waifu').json()
    image_url = contents['url']
    return image_url

def get_lewdurl():
    contents = requests.get('https://nekos.life/api/v2/img/lewd').json()
    image_url = contents['url']
    return image_url

def get_titsurl():
    contents = requests.get('https://nekos.life/api/v2/img/tits').json()
    image_url = contents['url']
    return image_url

def get_boobsurl():
    contents = requests.get('https://nekos.life/api/v2/img/boobs').json()
    image_url = contents['url']
    return image_url


def get_solourl():
    contents = requests.get('https://nekos.life/api/v2/img/solo').json()
    image_url = contents['url']
    return image_url

def get_erourl():
    contents = requests.get('https://nekos.life/api/v2/img/ero').json()
    image_url = contents['url']
    return image_url

def get_hentaiurl():
    contents = requests.get('https://nekos.life/api/v2/img/hentai').json()
    image_url = contents['url']
    return image_url

@bot.message_handler(commands = ['greet','start'])
def greet(message):
    msg = ''' Hey there, I'm Tsuzumi 💖
     I can fetch hottest anime photos and GIFs and send them to you
     Send /help to check the commands out. '''
    bot.send_message(message.chat.id, msg) 

@bot.message_handler(commands = ['help'])
def help(message):
    msg = ''' Here are the commands :
    /waifu | /neko | /shinobu | /megumin
    /kiss  | /lick | /lewd    | /tits 
    /boobs | /solo | /ero     | /hentai
    '''
    bot.send_message(message.chat.id, msg)
    
@bot.message_handler(commands = ['waifu'])
@bot.message_handler(regexp=r'waifu')
def waifu(message):
    url = get_url()
    bot.send_photo(message.chat.id, url)
    
@bot.message_handler(commands = ['neko'])
@bot.message_handler(regexp=r'neko')
def neko(message):
    url = get_nekourl()
    bot.send_photo(message.chat.id, url)    

@bot.message_handler(commands = ['shinobu'])
@bot.message_handler(regexp=r'shinobu')
def shinobu(message):
    url = get_shinobuurl()
    bot.send_photo(message.chat.id, url)   
    
@bot.message_handler(commands = ['megumin'])
@bot.message_handler(regexp=r'megumin')
def megumin(message):
    url = get_meguminurl()
    bot.send_photo(message.chat.id, url)       

@bot.message_handler(commands = ['kiss'])
@bot.message_handler(regexp=r'kiss')
def kiss(message):
    url = get_kissurl()
    bot.send_photo(message.chat.id, url)  
    
@bot.message_handler(commands = ['lick'])
@bot.message_handler(regexp=r'lick')
def lick(message):
    url = get_lickurl()
    bot.send_photo(message.chat.id, url)    
    
@bot.message_handler(commands = ['lewd'])
@bot.message_handler(regexp=r'lewd')
def lewd(message):
    url = get_lewdurl()
    bot.send_photo(message.chat.id, url)
    
@bot.message_handler(commands = ['tits'])
@bot.message_handler(regexp=r'tits')
def lewdb(message):
    url = get_titsurl()
    bot.send_photo(message.chat.id, url)
    
@bot.message_handler(commands = ['solo'])
@bot.message_handler(regexp=r'solo')
def lewdc(message):
    url = get_solourl()
    bot.send_photo(message.chat.id, url)
    
@bot.message_handler(commands = ['boobs'])
@bot.message_handler(regexp=r'boobs')
def lewdd(message):
    url = get_boobsurl()
    bot.send_photo(message.chat.id, url)
    
@bot.message_handler(commands = ['ero'])
@bot.message_handler(regexp=r'ero')
def ero(message):
    url = get_erourl()
    bot.send_photo(message.chat.id, url)
    
@bot.message_handler(commands = ['hentai'])
@bot.message_handler(regexp=r'hentai')
def hentai(message):
    url = get_hentaiurl()
    bot.send_photo(message.chat.id, url)     
    

@bot.message_handler(func=lambda m: True)
def repeat(message):
    bot.send_message(message.chat.id, message.text)

def main():
    bot.polling()

if __name__ == '__main__':
    main()
