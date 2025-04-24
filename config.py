from os import environ 

class Config:
    API_ID = environ.get("API_ID", "4775443785444")
    API_HASH = environ.get("API_HASH", "fufjjdn")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8023975610") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://:@cluster0.")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '00000000').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
