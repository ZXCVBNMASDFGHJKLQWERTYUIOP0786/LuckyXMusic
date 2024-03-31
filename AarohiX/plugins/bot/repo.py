from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AarohiX import app
from config import BOT_USERNAME

start_txt = """**
✪ ωεℓ¢σмє ✪

 𝐌𝐄𝐋𝐄 𝐁𝐀𝐁𝐔 𝐊𝐎 𝐑𝐄𝐏𝐎 𝐂𝐇𝐀𝐇𝐈𝐘𝐄

➲ 🎧 ᴘʟᴀʏ 𝟸𝟺×𝟽 ᴀᴄᴛɪᴠᴇ 𝐋𝚞𝚌𝚔𝚢🅧𝐌𝚞𝚜𝚒𝚌 🎧

➥ sᴜᴘᴘᴏʀᴛᴇᴅ ғᴜɴᴄᴛɪᴏɴ ➻ ᴡᴇʟᴄᴏᴍᴇ - ʟᴇғᴛ ɴᴏᴛɪᴄᴇ, ᴛᴀɢᴀʟʟ, ᴠᴄᴛᴀɢ, ʙᴀɴ - ᴍᴜᴛᴇ, sʜᴀʏʀɪ, ɢᴀᴍᴇ, ɪɴғᴏ, ᴀᴘʀᴏᴠᴇᴅ, ғɪʟᴛᴇʀ, sᴏɴɢ - ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ᴇᴛᴄ... 

🔐ᴜꜱᴇ » /help ᴛᴏ ᴄʜᴇᴄᴋ
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
     
            [ 
          InlineKeyboardButton("𝐀𝙳𝙳 𝐌𝙴 𝐆𝚁𝙾𝚄𝙿", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝐎𝚆𝙽𝙴𝚁", url="https://t.me/itz_Lucky_Raja"),
          InlineKeyboardButton("𝐉𝙰𝙰𝙽", url="https://t.me/LuckyRaja0"),
          ],
               [
                InlineKeyboardButton("😍𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬😍", url="https://t.me/+g0YcEKl54yU0ZTU9"),

],
[
              InlineKeyboardButton("𝐒𝚃𝚄𝙳𝚈", url=f"https://t.me/+UQUsfzMdlIJjNjll"),
              InlineKeyboardButton("︎𝐓 𝚀𝚄𝙸𝚉 ", url=f"https://t.me/T_QUIZ"),
              ],
              [
              InlineKeyboardButton("𝐃𝐞𝐯🥀", url=f"https://t.me/LuckyRaja0"),
InlineKeyboardButton("𝐒𝐡𝐚𝐲𝐫𝐢🥀", url=f"https://t.me/Badnam_Mohabbat"),
InlineKeyboardButton("𝐆𝐫𝐨𝐮𝐩", url=f"https://t.me/+WDNH4yTCWe5jOTI1"),
],
[
InlineKeyboardButton("𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 𝐀𝐝𝐝 𝐌𝐞 𝐆𝐫𝐨𝐮𝐩 ", url=f"https://t.me/Miss_Mahi_Bot?startgroup=true")
],
[
              InlineKeyboardButton("𝐁𝐨𝐭", url=f"https://t.me/ZiddiXBot"),
              InlineKeyboardButton("𝟑𝐃 𝐀𝐢 𝐃𝐩", url=f"https://t.me/DP_AI_DP"),
              ],
              [
              InlineKeyboardButton("𝐏𝐫𝐨𝐟𝐢𝐥𝐞", url=f"https://t.me/THE_OP_BOY"),
InlineKeyboardButton("𝐎𝐟𝐟𝐢𝐜𝐞", url=f"https://t.me/THE_TOP_BOY_OP"),
],
[
InlineKeyboardButton("𝐓𝐠 𝐁𝐨𝐭", url=f"https://t.me/TOP_TG_BOTS"),
InlineKeyboardButton("𝐓𝐠 𝐟𝐫𝐢𝐞𝐧𝐝𝐬 ", url=f"https://t.me/TOP_TG_FRIENDS"),
],
[
InlineKeyboardButton("𝐀𝐧𝐢𝐦𝐞 𝐌𝐨𝐯𝐢𝐞 ", url=f"https://t.me/AnimeMovieLucky"),
             ],
     
              ]
 
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_video(
        video="https://te.legra.ph/file/dcbac030f70758cd12a91.mp4",
        caption=start_txt,
        reply_markup=reply_markup
    )
