import config
import time
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

StartTime = time.time()
app = Client(
    "Anonymous",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="ROYEDITX"),
)


if __name__ == "__main__":
    print("⬤ sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ...♥︎")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("⬤ ʏᴏᴜʀ API_ID/API_HASH ɪs ɴᴏᴛ ᴠᴀʟɪᴅ...🌺")
    except AccessTokenInvalid:
        raise Exception("⬤ ʏᴏᴜʀ BOT_TOKEN ɪs ɴᴏᴛ ᴠᴀʟɪᴅ...🌸")
    uname = app.get_me().username
    print(f"⬤ @{uname} sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ...🏵️")
    idle()
    app.stop()
    print("⬤ ʙᴏᴛ sᴛᴏᴘᴇᴅ...🪴")
  
