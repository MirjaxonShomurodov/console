from flask import Flask

app = Flask(__name__)

@app.route('/')
def name():
    return 'Hello depoment'
if __name__=="__main__":
    app.run(debug=True, port=4000)