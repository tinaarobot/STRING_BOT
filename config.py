from os import getenv
from dotenv import load_dotenv

load_dotenv()

#❖________①_______❖_______#
API_ID = int(getenv("API_ID", None))

#❖________②_______❖_______#
API_HASH = getenv("API_HASH", None)

#❖________③_______❖_______#
BOT_TOKEN = getenv("BOT_TOKEN", None)

#❖________④_______❖_______#
OWNER_ID = int(getenv("OWNER_ID", None))

#❖________⑤_______❖_______#
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

#❖________⑥_______❖_______#
MUST_JOIN = getenv("MUST_JOIN", None)
