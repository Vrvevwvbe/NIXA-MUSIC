import asyncio
from time import time
from datetime import datetime
from config import BOT_USERNAME
from config import GROUP_SUPPORT, UPDATES_CHANNEL, START_PIC
from NIXA.filters import command
from NIXA.command import commandpro
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from NIXA.main import bot as Client

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ( week , 60 * 60 * 24 * 7),
    ( day , 60 * 60 * 24),
    ( hour , 60 * 60),
    ( min , 60),
    ( sec , 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return  inf 
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append( {} {}{} 
                         .format(amount, unit, "" if amount == 1 else "s"))
    return  ,  .join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**اهلآ بك 
في اقوا بوت متطور مميزاته مامطروقه.
لتشغيل الاغاني في المكالمات الصوتيه..
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ اضفني الى مجموعتك ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "الاوامر الاساسيه", url=f"https://telegra.ph/%D8%B3%D9%88%D8%B1%D8%B3-%D9%83%D9%88%D8%A8%D8%B1%D8%A7-%D8%A7%D9%84%D8%A7%D9%81%D8%B6%D9%84-06-23"
                    ),
                    InlineKeyboardButton(
                        "", url="https://t.me/QABNADLIB"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "قناة السورس", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "كروب المساعدة", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/stats"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/bf9f444677e4d565542a6.jpg",
        caption=f"""اهلا بك انا اقوا بوت في التليكرام لتشغيل الاغاني.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Source Cobra", url=f"https://t.me/VFF35")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/187646e964cd12329f1de.jpg",
        caption=f"""هلاو عمري يمكنك تنصيب بوت خاص بك تواصل مع المطور""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐒𝐈𝐅 𝐂𝐎𝐁𝐑𝐀", url=f"https://t.me/QABNADLIB")
                ]
            ]
        ),
    )