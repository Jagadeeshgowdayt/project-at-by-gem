#new_relesed_python_code
import re
import os
from os import environ, getenv
from Script import script

# Utility functions
id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# ============================
# Bot Information Configuration
# ============================
SESSION = environ.get('SESSION', 'TechVJBot')   # Session name for the bot
API_ID = int(environ.get('API_ID', '16564172')) # API ID from my.telegram.org
API_HASH = environ.get('API_HASH', 'f0184f4c1bad2efdc2f59b8591c7a839')  # API Hash from my.telegram.org
BOT_TOKEN = environ.get('BOT_TOKEN', "")    # Bot token from @BotFather

# ============================
# Bot Settings Configuration
# ============================
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))    # Cache time in seconds (default: 5 minutes)
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))  # Use caption filter for search results (default: True)
INDEX_CAPTION = bool(environ.get('SAVE_CAPTION', True)) # Save caption db when idexing make it False if you dont use USE_CAPTION_FILTER for search results (default: True)
#Making it false will not save caption in db SO you can save some storage space


PICS = (environ.get('PICS', 'https://graph.org/-07-16-3027 https://graph.org/file/5303692652d91d52180c2.jpg https://graph.org/file/425b6f46efc7c6d64105f.jpg https://graph.org/file/876867e761c6c7a29855b.jpg')).split()  # Sample pic
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/b69af2db776e4e85d21ec.jpg")
MELCOW_PHOTO = environ.get("MELCOW_PHOTO", "https://t.me/How_To_Open_Linkl") # Mapped from MELCOW_VID in customized code
SPELL_IMG = environ.get("SPELL_IMG", "https://te.legra.ph/file/15c1ad448dfe472a5cbb8.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/242b7f1b52743938d81f1.jpg')) # Kept default from new code
FSUB_PICS = (environ.get('FSUB_PICS', 'https://graph.org/file/7478ff3eac37f4329c3d8.jpg https://graph.org/file/56b5deb73f3b132e2bb73.jpg')).split()  # Kept default from new code

# ============================
# Admin, Channels & Users Configuration
# ============================
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1308498708').split()] # Replaced with customized code value
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002428424894').split()]  # Replaced with customized code value

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002388027077'))  # Replaced with customized code value
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-100'))  # Kept default from new code
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-100'))  # Kept default from new code
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()] #(Replaced with customized code value)
support_chat_id = environ.get('SUPPORT_CHAT_ID', '')  # Replaced with customized code value (empty string)
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002428424894')  # Replaced with customized code value
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/J7NET_BOT')  # Replaced with customized code value

# FORCE_SUB
auth_req_channel = environ.get('AUTH_REQ_CHANNEL', '')  # Replaced with customized code value (empty string)
AUTH_CHANNELS = [int(channels_id) for channels_id in environ.get('AUTH_CHANNELS', '').split() if re.match(r'^-?\d+$', channels_id)]  # Replaced with customized code value (empty list)


# ============================
# Payment Configuration
# ============================
QR_CODE = environ.get('QR_CODE', 'https://envs.sh/qbt.jpg')    # Replaced with customized code value
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'order187pay@postbank')    # Replaced with extracted UPI ID from customized code
STAR_PREMIUM_PLANS = {
    10: "7day",
    20: "15day",
    40: "1month",
    55: "45day",
    75: "60day",
}  # Kept default from new code

# ============================
# MongoDB Configuration
# ============================
DATABASE_URI = environ.get('DATABASE_URI', "")  # Replaced with customized code value
DATABASE_NAME = environ.get('DATABASE_NAME', "jagadeeshs") # Replaced with customized code value
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'jagadeeshs') # Replaced with customized code value

# If MULTIPLE_DB Is True Then Fill DATABASE_URI2 Value Else You Will Get Error.
MULTIPLE_DB = is_enabled(os.environ.get('MULTIPLE_DB', "False"), False) # Kept default from new code, ensures compatibility
DATABASE_URI2 = environ.get('DATABASE_URI2', "")  # Kept default from new code, as no second URI in customized code
# ============================
# Movie Notification & Update Settings
# ============================
MOVIE_UPDATE_NOTIFICATION = bool(environ.get('MOVIE_UPDATE_NOTIFICATION', False))  # Kept default from new code
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-100'))  # Kept default from new code
DREAMXBOTZ_IMAGE_FETCH = bool(environ.get('DREAMXBOTZ_IMAGE_FETCH', True))  # Kept default from new code
LINK_PREVIEW = bool(environ.get('LINK_PREVIEW', False)) # Kept default from new code
ABOVE_PREVIEW = bool(environ.get('ABOVE_PREVIEW', True)) # Kept default from new code


# ============================
# Verification Settings
# ============================
IS_VERIFY = is_enabled('IS_VERIFY', False)  # Replaced with customized code value
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-100')) # Kept default from new code
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-100')) # Kept default from new code
VERIFY_IMG = environ.get("VERIFY_IMG", "https://telegra.ph/file/9ecc5d6e4df5b83424896.jpg") # Kept default from new code

TUTORIAL = environ.get("TUTORIAL", "https://telegram.me/J7NET_BOT")   # Replaced with customized code value
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://telegram.me/J7NET_BOT")   # Replaced with customized code value
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://telegram.me/J7NET_BOT")   # Replaced with customized code value

# Verification (Must Fill All Veriables. Else You Got Error
SHORTENER_API = environ.get("SHORTENER_API", "f5760039a7c4bf3fddd00c4297dfad9ff82ce46a") # Replaced with customized code value
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "tnshort.net") # Replaced with customized code value

SHORTENER_API2 = environ.get("SHORTENER_API2", "")  # Replaced with customized code value (empty string)
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "") # Replaced with customized code value (empty string)

SHORTENER_API3 = environ.get("SHORTENER_API3", "a7ac9b3012c67d7491414cf272d82593c75f6cbb")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "omegalinks.in") # Kept default from new code

TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "1200")) # Kept default from new code
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "54000"))

# ============================
# Channel & Group Links Configuration
# ============================
GRP_LNK = environ.get('GRP_LNK', 'https://telegram.me/J7NET_BOT') # Replaced with customized code value
OWNER_LNK = environ.get('OWNER_LNK', 'https://telegram.me/J7NET_BOT') # Replaced with customized code GRP_LNK as a general link
UPDATE_CHNL_LNK = environ.get('UPDATE_CHNL_LNK', 'https://t.me/J7NET_BOT') # Replaced with customized code CHNL_LNK

# ============================
# User Configuration
# ============================
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1308498708').split()] # Replaced with customized code value
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()] # Kept default from new code

# ============================
# Miscellaneous Configuration
# ============================
MAX_B_TN = environ.get("MAX_B_TN", "5") # Replaced with customized code value
PORT = environ.get("PORT", "8080")  # Replaced with customized code value
MSG_ALRT = environ.get('MSG_ALRT', 'im J7NET_BOT who are you..?') # Replaced with customized code value
DELETE_TIME = int(environ.get("DELETE_TIME", "300"))  # Kept default from new code
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")   # Kept as is
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION) # Kept as is
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")     # Kept as is
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None) # Replaced with customized code value
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', -1002388027077))  # Replaced with customized code value
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))  # Replaced with customized code value
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)    # Replaced with customized code value
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)    # Replaced with customized code value
IMDB = is_enabled((environ.get('IMDB', "True")), True)    # Replaced with customized code value
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True) # Replaced with customized code value
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True) # Replaced with customized code value
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False) # Replaced with customized code value
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True) # Replaced with customized code value
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True) # Replaced with customized code value
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False) # Replaced with customized code value
PM_SEARCH = bool(environ.get('PM_SEARCH', True))  # Replaced with customized code value
EMOJI_MODE = bool(environ.get('EMOJI_MODE', False))  # Kept default from new code
BUTTON_MODE = is_enabled((environ.get('BUTTON_MODE', "True")), True) # Mapped from SINGLE_BUTTON in customized code
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Replaced with customized code value

# ============================
# Bot Configuration
# ============================
AUTH_REQ_CHANNEL = int(auth_req_channel) if auth_req_channel and id_pattern.search(auth_req_channel) else None # Adjusted based on customized code
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None # Adjusted based on customized code
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None # Adjusted based on customized code
LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"] # Replaced with customized code value
QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"] # Replaced with customized code value

SEASON_COUNT = 12 # Kept default from new code
SEASONS = ["season 1", "season 2", "season 3", "season 4", "season 5", "season 6", "season 7", "season 8", "season 9", "season 10"] # Replaced with customized code value

BAD_WORDS = {
    "PrivateMovieZ",
    "toonworld4all",
    "themoviesboss",
    "1tamilmv",
    "tamilblasters",
    "1tamilblasters",
    "skymovieshd",
    "extraflix",
    "hdm2",
    "moviesmod",
    "hdhub4u",
    "mkvcinemas",
    "primefix",
} # Kept default from new code


# ============================
# Server & Web Configuration
# ============================

NO_PORT = bool(environ.get('NO_PORT', False)) # Kept default from new code
APP_NAME = None # Kept default from new code
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0')) # Kept default from new code
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com' # Kept default from new code
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else "https://{}/".format(FQDN, PORT) # Kept dynamic URL generation from new code
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60')) # Replaced with customized code value
WORKERS = int(environ.get('WORKERS', '4')) # Kept default from new code
SESSION_NAME = str(environ.get('SESSION_NAME', 'dreamXBotz')) # Kept default from new code
MULTI_CLIENT = False # Replaced with customized code value
name = str(environ.get('name', 'DREAMXBOTZ')) # Kept default from new code
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # Replaced with customized code value
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))
else:
    ON_HEROKU = False
HAS_SSL = bool(getenv('HAS_SSL', True)) # Kept default from new code
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

# ============================
# Reactions Configuration
# ============================
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"] # Kept default from new code

# ============================
# Command Bot
# ============================
Bot_cmds = {
    "start": "Sᴛᴀʀᴛ Mᴇ Bᴀʙʏ",
    "stats": "Gᴇᴛ Bᴏᴛ Sᴛᴀᴛs",
    "alive": " Cʜᴇᴄᴋ Bᴏᴛ Aʟɪᴠᴇ ᴏʀ Nᴏᴛ ",
    "settings": "ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs",
    "id": "ɢᴇᴛ ɪᴅ ᴛᴇʟᴇɢʀᴀᴍ ",
    "info": "Gᴇᴛ Usᴇʀ ɪɴғᴏ ",
    "del_msg": "ʀᴇᴍᴏᴠᴇ ғɪʟᴇ ɴᴀᴍᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ɴᴏтɪғɪᴄᴀᴛɪᴏɴ...",
    "movie_update": "ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "pm_search": "ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "trendlist": "Gᴇᴛ Tᴏᴘ Tʀᴀɴᴅɪɴɢ Sᴇᴀʀᴄʜ Lɪsᴛ",
    "broadcast": "ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ.",
    "grp_broadcast": "ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs",
    "send": "ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴜꜱᴇʀ.",
    "add_premium": "ᴀᴅᴅ ᴀɴʏ ᴜꜱᴇʀ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.",
    "remove_premium": "ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴘʀᴇᴍɪᴜᴍ.",
    "premium_users": "ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ.",
    "restart": "ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.",
    "group_cmd": "ɢʀᴏᴜᴘ ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ",
    "admin_cmd": "ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs ʟɪsᴛ."
} # Kept default from new code

# ============================
# Logs Configuration
# ============================
LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for your queries.\n" if IMDB else "IMDB Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found, Users will be redirected to send /start to Bot PM instead of sending file directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled, files will be sent in PM instead of starting the bot.\n")
LOG_STR += ("BUTTON_MODE is found, filename and file size will be shown in a single button instead of two separate buttons.\n" if BUTTON_MODE else "BUTTON_MODE is disabled, filename and file size will be shown as different buttons.\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be sent along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled, Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode is enabled, bot will be suggesting related movies if movie name is misspelled.\n" if SPELL_CHECK_REPLY else "Spell Check Mode is disabled.\n")
