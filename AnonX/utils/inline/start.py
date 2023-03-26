from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ 𝗔𝗱𝗱 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽 ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❰ 𝙨𝙚𝙩𝙩𝙞𝙣𝙜 ❱", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ 𝗔𝗱𝗱 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽 ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="❰𝗚𝗿𝗼𝘂𝗽❱ ", url=f"https://t.me/ADVENTURE_FAMILYS"
            ),
            InlineKeyboardButton(
                text="❰𝘂𝗽𝗱𝗮𝘁𝗲𝘀❱ ", url=f"https://t.me/GJ516_DISCUSS_GROUP"
            )
        ],
        [
            InlineKeyboardButton(
                text="❰𝙊𝙬𝙣𝙚𝙧❱", user_id=OWNER
            )
        ],
     ]
    return buttons
