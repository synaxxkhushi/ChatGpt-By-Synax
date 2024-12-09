import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "24267726"))
API_HASH = environ.get("API_HASH", "7500ba8248548cc3864bd033668f9a9a")
BOT_TOKEN = environ.get("BOT_TOKEN", "5603694906:AAHP8J5nO4DcEHtx11di3yleYAJ_rQSXoiA")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002132398644"))
ADMINS = int(environ.get("ADMINS", "6231550362"))
DB_URI = environ.get("DB_URI", "mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "EXONTESTMONGO")
OPENAI_API = environ.get("OPENAI_API", "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")
AI = is_enabled((environ.get("AI","True")), False)
