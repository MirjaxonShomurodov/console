from flask import Flask
import telegram 

app = Flask(__name__)

TOKEN = "6333225235:AAFbjxLb1QS7zZIW4maMZ4-CtRNybDdH6ys"

bot = telegram.Bot(TOKEN)

chat_id = "5466480235"
@app.route('/')
def main():
  
    bot.send_message(
        chat_id=chat_id,
        text=f"Hello, how are you, thank you for visiting our site "
        )
    return 'Hello deploymint!'



if __name__=="__main__":
    app.run(debug=True, port=4000)