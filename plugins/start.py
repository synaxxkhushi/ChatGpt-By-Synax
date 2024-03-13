from pyrogram import Client, filters
from config import LOG_CHANNEL
from plugins.database import db
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)


LOG_TEXT = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""

@Client.on_message(filters.command('start'))
async def start_message(c,m):
    await db.is_user_exist(m.from_user.id)
    await db.add_user(m.from_user.id, m.from_user.first_name)
    await c.send_message(LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
    await m.reply_photo(f"https://graph.org/file/bed3114b73b2969f92018.jpg",
        caption="**ʜɪ ɢᴜʏs 🇮🇳❤️** \n\n**ɪ ᴀᴍ ᴀ ᴄʜᴀᴛɢᴘᴛ ʙᴏᴛ ☢️**\n\n⭕ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :-** **[𝐒ᴀɴᴀᴛᴀɴɪ 𝐒ʏɴᴀx](https://t.me/coder_s4nax)**",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🇮🇳 ᴊᴏɪɴ ғᴏʀ ᴜᴘᴅᴀᴛᴇ 🇮🇳', url='https://t.me/synaxbots')
                    ],  
                    [
                        InlineKeyboardButton("🍁 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🍁", url='https://t.me/coder_s4nax'),
                        InlineKeyboardButton("🍁 ᴜᴘᴅᴀᴛᴇ 🍁", url='https://t.me/synaxnetwork')
                    ]
                ]
            )
        )
  
