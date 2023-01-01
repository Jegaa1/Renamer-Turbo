"""
© Mrvishal2k2
RenameBot
This file is a part of mrvishal2k2 rename repo
Dont kang !!!
© Mrvishal2k2
"""
import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "1923471"))
    API_HASH = os.environ.get("API_HASH","fcdc178451cd234e63faefd38895c991")
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1965973276:AAFngpmzKFyESfcvQscv7S7Dmus7N-nksWI")
    AUTH_USERS = [int(x) for x in os.environ.get("AUTH_USERS", "880087645").split()]
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./bot/DOWNLOADS")
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://video:video@rishi.fzpls33.mongodb.net/?retryWrites=true&w=majority")
    # owner is for log cmd only owner can use (this can be multiple users)
    OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID", "880087645").split(" ")]
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "JAsuran2p0")
    CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", False)
