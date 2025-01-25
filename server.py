from flask import Flask, render_template
from api import api

app = Flask(__name__, static_folder='dist/assets', template_folder='dist')

app.register_blueprint(api, url_prefix="/api")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

app.run(host="0.0.0.0", port=80)