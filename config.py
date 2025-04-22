from os import environ 

class Config:
    API_ID = environ.get("API_ID", "28036362")
    API_HASH = environ.get("API_HASH", "84e4bd8457dab2f065801bde8874842a")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8023975610:AAFqa_mIZBoffvFWdoSy4UnzY3y1nPVVvHc") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://wikeke7922:VMoBcxdkgJwjeCaK@cluster0.sexvt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7576455886').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
