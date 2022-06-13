from flask import Blueprint, render_template, request
import os
from unicodedata import normalize
from flask_user import current_user, login_required


from .youtube import youtube_download
from .transcriber import transcribe
from .upload import upload
# from .transcribe_2 import transcribe

public_blueprint = Blueprint('public', __name__, template_folder='templates')

# @public_blueprint.route('/')
# def home_page():
#     return render_template('pages/home_page.html')
# GLOBALS
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="google_cloud.json"
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3', 'mp4', 'wav'}
HOST = '0.0.0.0'
PORT = 5000
LOCALES = {"ru": "ru-RU", "kz": "kk-KZ", "en": "en-US"}

# CONFIG
# app = Flask(__name__)
# app.config['MAX_CONTENT_LENGTH'] = 200 * 1000 * 1000
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# FUNCTIONS
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@public_blueprint.route("/", methods=['GET', 'POST'])
def home_page():
    return render_template('pages/home_page.html')

#https://www.youtube.com/shorts/rz0rvzJL_6U
@public_blueprint.route("/transcribe", methods=['GET', 'POST'])
@login_required
def transcribe_page():
    if request.method == 'POST':
       locale = request.form.get("locale")
       print(f"LOCALE {locale}")
       file = request.files['file']
       if file and allowed_file(file.filename):
           filename = normalize('NFKC',file.filename)
           file_location = f"{UPLOAD_FOLDER}/{filename}"
           print(f"file_location: {file_location}")
           file.save(file_location)
           filename = upload(file_location)
           text, confidence = transcribe(filename, LOCALES[locale])
       elif request.form["youtube"]:
           filename = youtube_download(request.form["youtube"])
           print(filename)
           text, confidence = transcribe(filename, LOCALES[locale])
       else:
           text="Ошибка. Вставьте либо файл, либо ссылку с YouTube"
           confidence = ""
    else:
          text="Запустите приложение для получения транскрипции"
          confidence = ""
    return render_template('pages/transcribe_page.html', data=text)