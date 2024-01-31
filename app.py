from telegram.ext import CallbackContext,MessageHandler,Filters,CommandHandler,Updater
from telegram import Update ,ReplyKeyboardMarkup,KeyboardButton
from flask import Flask,request
import telegram 


app = Flask(__name__)

TOKEN = "6333225235:AAFbjxLb1QS7zZIW4maMZ4-CtRNybDdH6ys"
URL = "http://mirjaxon.pythonanywhere.com/"

bot = telegram.Bot(TOKEN)


@app.route('/',methods = ['POST'])
def main():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    bot.send_message(chat_id=chat_id,text=data['message']['text'])

    
LIKES,DISLIKES = 0,0

def start(update:Update,context:CallbackContext):
    user = update.message.from_user
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👍"),KeyboardButton(text="👎")],
            [KeyboardButton(text='🆑')]
            ],
        resize_keyboard=True
    )
    update.message.reply_html(
        text=f"Hello welcome to our bot {user.first_name}",
        reply_markup=keyboard
    )

def like(update:Update,context:CallbackContext):
    global LIKES
    LIKES+=1

    update.message.reply_html(text=f"likes:{LIKES}\ndislike:{DISLIKES}")

def dislikes(update:Update,context:CallbackContext):
    global DISLIKES
    DISLIKES+=1

    update.message.reply_text(text=f"likes:{LIKES}\ndislike: {DISLIKES}")


    update = Updater(TOKEN)

    dispatcher = update.dispatcher

    dispatcher.add_handler(handler=CommandHandler(command='start',callback=start))

    dispatcher.add_handler(handler=MessageHandler(filters = Filters.text('👍'),callback=like))
    dispatcher.add_handler(handler=MessageHandler(filters = Filters.text('👎'),callback=dislikes))

    update.start_polling()
    update.idle()
    
    return 'Hello deploymint!'

if __name__=="__main__":
    app.run(debug=True, port=4000)