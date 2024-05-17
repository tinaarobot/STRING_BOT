from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""๏ нᴇʏ {msg.from_user.mention}, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !

๏ ɪ ᴀᴍ ‌ ‌{me2} ᴀɴᴅ ɪ ʜᴀᴠᴇ ᴛᴇʟᴇᴛʜᴏɴ ᴀɴᴅ ᴘʏʀᴏɢʀᴀᴍ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛɪɴɢ ғᴇᴀᴛᴜʀᴇs.

๏ ᴛʜɪs ɪs ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ ᴀɴᴅ ᴛʀᴜsᴛᴇᴅ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.

๏ 💌 ᴍᴀᴅᴇ ʙʏ ➠ [ʀᴏʏ ᴇᴅɪᴛx](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="💌 ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ 💌", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/THE_FRIENDZ"),
                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/ROY_EDITX")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
  
