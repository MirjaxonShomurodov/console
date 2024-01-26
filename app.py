from flask import Flask

app = Flask(__name__)

@app.route('/')
def name():
    return 'hi deploymint'

@app.route("/rout")
def main():
    return "Depolymint app"

if __name__=="__main__":
    app.run(debug=True, port=4000)