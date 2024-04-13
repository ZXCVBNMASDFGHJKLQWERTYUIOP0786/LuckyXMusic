from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app
from config import BOT_USERNAME


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="۞ 𝐇𝙴𝙻𝙿 ۞", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="☢ 𝐒𝙴𝚃 ☢", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="✡ 𝐆𝚁𝙾𝚄𝙿 ✡", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="𝐎ᴡɴᴇʀ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="𝐃ᴇᴠʟᴏᴘᴇʀ", user_id=7048220980),
        ],
        [
           InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
InlineKeyboardButton(text=_["S_B_7"], url=f"https://t.me/Miss_Mahi_Bot?startgroup=true")
        
        ],
    ]

    return buttons