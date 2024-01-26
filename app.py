from flask import Flask

app = Flask(__name__)

@app.route('/')
def name():
    return 'Nateja chiqmayapti nima uchun!'
if __name__=="__main__":
    app.run(debug=True, port=4000)