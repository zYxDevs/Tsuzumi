import telebot
from dotenv import load_dotenv
import os
import requests

load_dotenv()
token = os.getenv('TOKEN')

bot = telebot.TeleBot(token)

# Let's define stuff
def get_url():
    contents = requests.get('https://api.waifu.pics/sfw/waifu').json()
    return contents['url']

def get_nekourl():
    contents = requests.get('https://api.waifu.pics/sfw/neko').json()
    return contents['url']

def get_avatarurl():
    contents = requests.get('https://nekos.life/api/v2/img/avatar').json()
    return contents['url']


def get_shinobuurl():
    contents = requests.get('https://api.waifu.pics/sfw/shinobu').json()
    return contents['url']

def get_meguminurl():
    contents = requests.get('https://api.waifu.pics/sfw/megumin').json()
    return contents['url']

def get_kissurl():
    contents = requests.get('https://api.waifu.pics/nsfw/trap').json()
    return contents['url']

def get_lickurl():
    contents = requests.get('https://api.waifu.pics/nsfw/blowjob').json()
    return contents['url']

def get_nwaifuurl():
    contents = requests.get('https://api.waifu.pics/nsfw/waifu').json()
    return contents['url']

def get_lewdurl():
    contents = requests.get('https://nekos.life/api/v2/img/lewd').json()
    return contents['url']

def get_holourl():
    contents = requests.get('https://nekos.life/api/v2/img/hololewd').json()
    return contents['url']

def get_titsurl():
    contents = requests.get('https://nekos.life/api/v2/img/tits').json()
    return contents['url']

def get_boobsurl():
    contents = requests.get('https://nekos.life/api/v2/img/boobs').json()
    return contents['url']

def get_solourl():
    contents = requests.get('https://nekos.life/api/v2/img/solo').json()
    return contents['url']

def get_erourl():
    contents = requests.get('https://nekos.life/api/v2/img/ero').json()
    return contents['url']

def get_hentaiurl():
    contents = requests.get('https://nekos.life/api/v2/img/hentai').json()
    return contents['url']

def get_eronurl():
    contents = requests.get('https://nekos.life/api/v2/img/eron').json()
    return contents['url']


def get_bjurl():
    contents = requests.get('https://nekos.life/api/v2/img/bj').json()
    return contents['url']

def get_erokiturl():
    contents = requests.get('https://nekos.life/api/v2/img/eroK').json()
    return contents['url']

def get_pussyurl():
    contents = requests.get('https://nekos.life/api/v2/img/pussy').json()
    return contents['url']

def get_kitesuneurl():
    contents = requests.get('https://nekos.life/api/v2/img/lewdk').json()
    return contents['url']

def get_holoerourl():
    contents = requests.get('https://nekos.life/api/v2/img/holoero').json()
    return contents['url']


@bot.message_handler(commands = ['greet','start'])
def greet(message):
    msg = ''' Hey there, I'm Tsuzumi 💖
     I can fetch hottest anime and hentai images & send them to you
     Send /help to check the commands out. '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['ping'])
def greet(message):
    msg = ''' I'm alive :3 '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['repo'])
def greet(message):
    msg = ''' Repository Link -> https://github.com/nisarga-developer/tsuzumi '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['source'])
def greet(message):
    msg = ''' Source Code -> https://github.com/nisarga-developer/tsuzumi
              Author -> Nisarga Adhikary
              License -> Apache 2.0 License    '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands = ['help'])
def help(message):
    msg = ''' Here are the commands :

    SFW Commands :
    /waifu
    /neko
    /shinobu
    /megumin
    /avatar

    NSFW Commands :
    /trap
    /blowjob
    /lewd
    /tits
    /boobs
    /solo
    /ero
    /hentai
    /bj
    /kitesune
    /eroKitesune
    /pussy
    /holo
    /holoEro
    /eroNeko

    Other Commands :
    /ping
    /repo
    /source
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

@bot.message_handler(commands = ['eroNeko'])
@bot.message_handler(regexp=r'eroNeko')
def eroneko(message):
    url = get_eronekourl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['avatar'])
@bot.message_handler(regexp=r'avatar')
def avatar(message):
    url = get_avatarurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['kitesune'])
@bot.message_handler(regexp=r'kitesune')
def kitesune(message):
    url = get_kitesuneurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['eroKitesune'])
@bot.message_handler(regexp=r'eroKitesune')
def eroKitesune(message):
    url = get_erokiturl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['holo'])
@bot.message_handler(regexp=r'holo')
def eroHolo(message):
    url = get_holourl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['holoEro'])
@bot.message_handler(regexp=r'holoEro')
def holoEro(message):
    url = get_holoerourl()
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

@bot.message_handler(commands = ['bj'])
@bot.message_handler(regexp=r'bj')
def bj(message):
    url = get_bjurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['pussy'])
@bot.message_handler(regexp=r'pussy')
def pussy(message):
    url = get_pussyurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['trap'])
@bot.message_handler(regexp=r'trap')
def kiss(message):
    url = get_kissurl()
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands = ['blowjob'])
@bot.message_handler(regexp=r'blowjob')
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


def main():
    bot.polling()

if __name__ == '__main__':
    main()
