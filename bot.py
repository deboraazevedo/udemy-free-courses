import telegram

from decouple import config
from pyudemy import Udemy

 
def send_message(message):
    bot = telegram.Bot(token=config('TOKEN'))
    status = bot.send_message(chat_id="@freecoursesudemy", text=message, parse_mode=telegram.ParseMode.HTML)
 
    print(status)


if __name__ == '__main__':
    send_message()