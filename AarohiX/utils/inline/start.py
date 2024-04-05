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
            InlineKeyboardButton(text="❤️‍🔥𝐎𝚆𝙽𝙴𝚁❤️‍🔥", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="💝𝐉𝙰𝙰𝙽💝", bot_id=7048220980),
        ],
        [
           InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")
        ],
        [

InlineKeyboardButton(text=_["S_B_5"], user_id=5493923823),
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
InlineKeyboardButton(text=_["S_B_7"], url=f"https://t.me/Miss_Mahi_Bot?startgroup=true")
        
        ],
    ]

    return buttons