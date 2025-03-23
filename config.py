from os import environ 

class Config:
    API_ID = environ.get("API_ID", "29922662")
    API_HASH = environ.get("API_HASH", "fabd9f89368de7cc31357522a0089a56")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6966644189:AAFHOah_zz4-bRCrHJ_UGR1zvoqc9RV8u0Y") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Supermandb:Supermandb@cluster0.nqkqpub.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Supermandb")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6874351976').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
