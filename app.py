from flask import Flask,request
import telegram 
app = Flask(__name__)

TOKEN = "6333225235:AAFbjxLb1QS7zZIW4maMZ4-CtRNybDdH6ys"

URL = "https://mirjaxon.pythonanywhere.com/"
bot = telegram.Bot(TOKEN)

@app.route('/',methods = ['POST'])
def main():
    data = request.get_json()
    print(data)
    chat_id = data['message']['chat']['id']
    if data['message'].get['message']!=None:   
        bot.send_message(chat_id=chat_id,text=data['message']['text'])
    elif data['message'].get['photo']!=None:
        bot.send_photo(chat_id=chat_id,file_id=['message']['photo'][-1]['file_id'])
    elif data['message'].get['audio']!=None:
        bot.send_audio(chat_id=chat_id,audio = ['message']['audio']['file_id'])
    elif ['message'].get['contact']!=None:
        bot.send_contact(chat_id=chat_id,contact=['message']['contact'],full_name=['message']['from_user'])
    elif data['message'].get['animation']!=None:
        bot.send_animation(chat_id=chat_id,misc=['message']['animation'])
    elif data['message'].get['dice']!=None:
        bot.send_dice(chat_id=chat_id,text=['message']['dice'])
    elif data['message'].get['location']!=None:
        bot.send_location(chat_id=chat_id,text = ['message']['location'])
    elif data['message'].get['sticker']!=None:
        bot.send_sticker(chat_id=chat_id,text=['message']['sticker'])
    elif data['message'].get['poll']!=None:
        bot.send_poll(chat_id=chat_id,is_anonymous=True)
    elif data['message'].get['document']!=None:
        bot.send_document(chat_id=chat_id,text = ['message']['document']['file_id'])
    elif data['message'].get['video']!=None:
        bot.send_video(chat_id=chat_id,video = ['message']['video']['file_id'])
    return 'Hello deploymint!'

if __name__=="__main__":
    app.run(debug=True, port=4000)