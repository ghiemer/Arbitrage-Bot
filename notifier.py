import asyncio, os
from telegram import Bot

TOKEN, CHAT = os.getenv("TELEGRAM_TOKEN"), os.getenv("TELEGRAM_CHAT_ID")
bot = Bot(TOKEN) if TOKEN else None

async def send_alert(level: str, msg: str):
    if not bot or not CHAT:
        return
    await bot.send_message(chat_id=CHAT, text=f"{level} | {msg}")
