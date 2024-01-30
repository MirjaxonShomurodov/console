from flask import Flask,request
import telegram 

app = Flask(__name__)

TOKEN = "6333225235:AAFbjxLb1QS7zZIW4maMZ4-CtRNybDdH6ys"
URL = "http://mirjaxon.pythonanywhere.com/"

bot = telegram.Bot(TOKEN)

chat_id = "5466480235"
@app.route('/',methods = ['POST'])
def main():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    bot.send_message(chat_id=chat_id,text=data['message']['text'])
    
    return 'Hello deploymint!'

if __name__=="__main__":
    app.run(debug=True, port=4000)