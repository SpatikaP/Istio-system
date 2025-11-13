from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>App Version 2</h1><p>This is version v2 of the application — updated layout and color!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

