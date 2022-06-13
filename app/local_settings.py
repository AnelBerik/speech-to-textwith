from datetime import timedelta
import os

# *****************************
# Environment specific settings
# *****************************

# DO NOT use "DEBUG = True" in production environments
DEBUG = True

# DO NOT use Unsecure Secrets in production environments
# Generate a safe one with:
#    python -c "import os; print(repr(os.urandom(24)));"
SECRET_KEY = 'DO_NOT_use_Unsecure_Secrets_in_production_environments'
COOKIE_SECURE = 'Secure'
COOKIE_DURATION = timedelta(days=365)

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids a SQLAlchemy Warning

BABEL_TRANSLATION_DIRECTORIES = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'translations/')

BABEL_DEFAULT_LOCALE = 'ru'

# Flask-Mail settings
# For smtp.gmail.com to work, you MUST set "Allow less secure apps"
# to ON in Google Accounts.
# Change it in https://myaccount.google.com/security#connectedapps
# (near the bottom).


MAIL_SERVER = 'mail.dp.buadcioq.kz'
MAIL_PORT = 25
MAIL_USE_SSL = True
MAIL_USE_TLS = True 
MAIL_USERNAME = 'info@dp.buadcioq.kz'
MAIL_PASSWORD = 'z01dS1@m8'
MAIL_DEFAULT_SENDER = '"Your Name" <info@dp.buadcioq.kz>'

ADMINS = [
    '"Admin One" <info@dp.buadcioq.kz>',
]
