from flask import Flask,request
import telegram
app = Flask(__name__)

TOKEN = "6333225235:AAFbjxLb1QS7zZIW4maMZ4-CtRNybDdH6ys"

bot = telegram.Bot(TOKEN)

@app.route('/',methods = ['POST'])
def main():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    print(data)
    if data['message'].get('text')!=None:   
        bot.send_message(chat_id=chat_id,text=data['message']['text'])

    elif data['message'].get('photo')!=None:
        bot.send_photo(chat_id=chat_id,photo=data['message']['photo'][0]['file_id'])

    elif data['message'].get('audio')!=None:
        bot.send_audio(chat_id,data['message']['audio']['file_id'],caption="Audio fayil.")

    elif ['message'].get('contact')!=None:
        bot.send_contact(chat_id,data['message']['contact']['phone_number'],data['message']['contact']['first_name'])

    elif data['message'].get('animation')!=None:
        bot.send_animation(chat_id=chat_id,animation=data['message']['animation'],duration=12)

    elif data['message'].get('dice')!=None:
        bot.send_dice(chat_id=chat_id,emoji=data['message']['dice']['emoji'],disable_notification=True)

    elif data['message'].get('location')!=None:
        bot.send_location(chat_id=chat_id,latitude = data['message']['location']['latitude'],longitude=data['message']['location']['longitude'],heading=2,protect_content=True)

    elif data['message'].get('sticker')!=None:
        bot.send_sticker(chat_id=chat_id,text=data['message']['sticker'],file_id = str(['file_id']),file_uniqua_id=data['file_uniqua_id'],width=['width'],height=['height'])

    elif data['message'].get('voice')!=None:
        bot.send_voice(chat_id=chat_id, data = data['message']['voice']['file_id'])

    elif data['message'].get('poll')!=None:
        bot.send_poll(chat_id=chat_id,question = data['message']['poll']['question'],options = data['message']['poll']['options'])

    elif data['message'].get('document')!=None:
        bot.send_document(chat_id=chat_id,document =data['message']['document']['file_id'],caption="Documitatsiya",protect_copntent=True)

    elif data['message'].get('video')!=None:
        bot.send_video(chat_id=chat_id,video = data['message']['video'][0]['file_id'])
    return 'Hello deploymint!'

if __name__=="__main__":
    app.run(debug=True, port=8000)