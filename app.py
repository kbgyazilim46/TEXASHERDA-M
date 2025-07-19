from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>TEXSAS</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-image: url('https://raw.githubusercontent.com/kbgyazilim46/TEXASHERDA-M/main/arkaplan.jpg');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                color: #fff;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                backdrop-filter: brightness(0.6);
            }
            h1 {
                font-size: 2em;
                margin-bottom: 20px;
                text-align: center;
                background: rgba(0, 0, 0, 0.6);
                padding: 10px 20px;
                border-radius: 10px;
            }
            a.button {
                display: inline-block;
                padding: 12px 24px;
                background-color: #e1306c;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
                transition: background-color 0.3s ease;
                background: rgba(0, 0, 0, 0.6);
            }
            a.button:hover {
                background-color: #c1235a;
            }
        </style>
    </head>
    <body>
        <h1>CEHENNEM BUZ TUTANA KADAR TEXSAS</h1>
        <a href="https://instagram.com/txs.xeons" target="_blank" class="button">
            INSTAGRAM: @txs.xeons
        </a>
    </body>
    </html>
    '''

# Gunicorn ile çalıştırmak için:
# gunicorn app:app
