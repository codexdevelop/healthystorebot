
import re
import os
from os import getenv, environ
from Script import script 
from dotenv import load_dotenv

load_dotenv()

# Credit @Codexownerr.
# Please Don't remove credit.
# Codexownerr Forever !
# Thanks You For Help Us In This Amazing Creativity 
# Thanks You For Giving Me Credit @Codexownerr
# For Any ERROR Please Contact Me -> Telegram ->@codexbotmaker & Insta @Codexownerr
# Please Love & Support 💗💗🙏


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Credit @Codexownerr.
# Please Don't remove credit.
# Codexownerr Forever !
# Thanks You For Help Us In This Amazing Creativity 
# Thanks You For Giving Me Credit @Codexownerr
# For Any ERROR Please Contact Me -> Telegram ->@codexbotmaker & Insta @Codexownerr
# Please Love & Support 💗💗🙏
      
# Owner Information
API_ID = int(environ.get("API_ID", "21994822"))
API_HASH = environ.get("API_HASH", "3d2430972bb360876864a636f0f06015")
ADMINS = int(environ.get("ADMINS", "7014391442"))

# Database Information
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://ap8181568:four@cluster4.ojmga.mongodb.net/?retryWrites=true&w=majority&appName=Cluster4")
CDB_NAME = environ.get("CDB_NAME", "Cluster4")
DB_URI = environ.get("DB_URI", "mongodb+srv://godlikeadi02:three@cluster3.5q9qt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster3")
DB_NAME = environ.get("DB_NAME", "Cluster3")

# Credit @Codexownerr.
# Please Don't remove credit.
# Codexownerr Forever !
# Thanks You For Help Us In This Amazing Creativity 
# Thanks You For Giving Me Credit @Codexownerr
# For Any ERROR Please Contact Me -> Telegram ->@codexbotmaker & Insta @Codexownerr
# Please Love & Support 💗💗🙏

# Bot Information
BOT_TOKEN = environ.get("BOT_TOKEN", "6751281414:AAHD82JheC-ujDJFarjqy0yd633c7uOPPfQ")
BOT_USERNAME = environ.get("BOT_USERNAME", "filestro_bot") # your bot username without @
PICS = (environ.get('PICS', 'https://media-hosting.imagekit.io//cf953b679ef1474d/giphy%20(1).gif?Expires=1835193163&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=d4Wd-3B6c4Fq-HCxEom76S4DQ6VGpSG9ZxRF3hbTWDqawjRF1Fr8HkvYpyMrZmvDPkwn6Vz1dLASkqDyrc2koxynEo9lLAjjsfhgjy-OwMw6JZVoNGIYaV6vnH85LbJnacbO1V-tpfEIfZHMs65Yr4y~So-GoDFLmEnbGD0ZG7ySWM42kmilbYz9pV8SP9lfr3neqEtsglOA~OmWDwRJn95-FQJip715lTWz0os4iPpTE0pj3cAm3dbgedI5Gbf~DDlntNRTVFnyWB-6CMm8sA~BBV05YykjgSiwr6OZtz6qQqpU7Kh3zBGqJRWNXCH~1eeS3t6VFPlYE347ITlDvw__')).split() # Bot Start Picture

# Auto Delete Information
AUTO_DELETE = int(environ.get("AUTO_DELETE", "5")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "300")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002318738273"))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002311834360')).split()]

# Credit @Codexownerr.
# Please Don't remove credit.
# Codexownerr Forever !
# Thanks You For Help Us In This Amazing Creativity 
# Thanks You For Giving Me Credit @Codexownerr
# For Any ERROR Please Contact Me -> Telegram ->@codexbotmaker & Insta @Codexownerr
# Please Love & Support 💗💗🙏

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Credit @Codexownerr.
# Please Don't remove credit.
# Codexownerr Forever !
# Thanks You For Help Us In This Amazing Creativity 
# Thanks You For Giving Me Credit @Codexownerr
# For Any ERROR Please Contact Me -> Telegram ->@codexbotmaker & Insta @Codexownerr
# Please Love & Support 💗💗🙏

# File Stream Config
class Var(object):
    MULTI_CLIENT = False
    name = str(getenv('name', 'theblackfilestore'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002197998836'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://usual-torey-theblackxyz24.koyeb.app/"
    else:
        URL = "https://usual-torey-theblackxyz24.koyeb.app/"



# Credit @Codexownerr.
# Please Don't remove credit.
# Codexownerr Forever !
# Thanks You For Help Us In This Amazing Creativity 
# Thanks You For Giving Me Credit @Codexownerr
# For Any ERROR Please Contact Me -> Telegram ->@codexbotmaker & Insta @Codexownerr
# Please Love & Support 💗💗🙏
    
