from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AarohiX import app as bot
import requests
from config import BOT_USERNAME
from AarohiX.utils.errors import capture_err

start_txt = """**
➤ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴡᴏʀʟᴅ ᥫᩣ
 
 ⦿ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ɴ ᴠᴘs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ !
 
 ⦿ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ !
 
 ⦿ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ !
 
 ⦿ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴅᴍ ᴍᴇ !
**"""

@bot.on_message(filters.command(["repo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("⦿ ᴀᴅᴅ ᴍᴇ ⦿", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/https://t.me/+g0YcEKl54yU0ZTU9"),
          InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/LuckyRaja0"),
        ],
        [
          InlineKeyboardButton("𝙶𝙸𝚃𝙷𝚄𝙱 𝙸𝙳", url=f"https://github.com/THE-TOP-BOY"),
          InlineKeyboardButton("︎𝚃𝙾𝙿 𝙼𝚄𝚂𝙸𝙲", url=f"https://github.com/THE-TOP-BOY/TOP-MUSIC"),
        ],
        [
          InlineKeyboardButton("𝙸𝙽𝚂𝚃𝙰 𝙸𝙳", url=f"https://www.instagram.com/itz_lucky.raja?igsh=ajFtZDRmbTZoaHY5"),
          InlineKeyboardButton("𝟹𝙳 𝙰𝙸 𝙳𝙿", url=f"https://t.me/DP_AI_DP"),
        ],
        [
          InlineKeyboardButton("𝚀𝚄𝙸𝚉 𝙶𝚁𝙾𝚄𝙿", url=f"https://t.me/+wsMlyxTvQtYwN2Y1"),
          InlineKeyboardButton("𝚃𝙾𝚃𝙰𝙻 𝚀𝚄𝙸𝚉", url=f"https://t.me/T_Quiz"),
        ],
        [
          InlineKeyboardButton("𝙼𝙰𝚂𝚃𝙸 𝙶𝚁𝙾𝚄𝙿 ", url="https://t.me/+YFFVeXdYxkQ1ODhl"),
          InlineKeyboardButton("बदनाम मोहब्बत", url=f"https://t.me/Badnam_Mohabbat"),
        ],
        [
          InlineKeyboardButton("TOP TG BOTS", url=f"https://t.me/TOP_TG_BOTS"),
          InlineKeyboardButton("TOP TG FRIENDS", url=f"TOP_TG_FRIENDS"),
        ],
        [
          InlineKeyboardButton("𝙵𝙸𝚁𝚂𝚃 𝙸𝙳", url=f"https://t.me/THE_OP_BOY"),
          InlineKeyboardButton("𝚂𝙴𝙲𝙾𝙽𝙳 𝙸𝙳", url=f"https://t.me/THE_TOP_BOY_OP"),
        ],
        [
          InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/ZiddiXBot"),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/511cdf3ea09cb8c35a06b.jpg",
        caption=start_txt,
        reply_markup=reply_markup,
    )



#-------------------------------------------------------#


@bot.on_message(filters.command("repo", prefixes="@"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/THE-TOP-BOY/TOP-MUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[ʀᴇᴘᴏ](https://github.com/THE-TOP-BOY/TOP-MUSIC) | [SUPPORT 𝖦𝖱𝖮𝖴𝖯](https://t.me/+g0YcEKl54yU0ZTU9)
| ᴄᴏɴᴛʀɪʙᴜᴛᴏʀs |
----------------
{list_of_users}"""
        await bot.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await bot.send_message(message.chat.id, text="Failed to fetch contributors.")

