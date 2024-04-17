from flask import Flask
from config import APP_NAME
from iriusrisk.views import summarize_text_path

app = Flask(APP_NAME)
app.register_blueprint(summarize_text_path)

if __name__ == '__main__':
    app.run()
