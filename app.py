from flask import Flask, render_template

from flask import Blueprint
from dotenv import load_dotenv
import os

load_dotenv()
APP_ROOT = os.environ.get("APP_ROOT", "")  # Set to '/dummy-app' in prod, '' in dev
app = Flask(__name__, static_url_path=f"{APP_ROOT}/static")
main_bp = Blueprint('main', __name__, url_prefix=APP_ROOT)

@main_bp.route('/')
def home():
    return render_template('index.html')

app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8864)
