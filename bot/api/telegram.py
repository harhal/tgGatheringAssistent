import os
import logging

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes
)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError(f"BOT_TOKEN имеет неверный формат: {BOT_TOKEN}")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

application = Application.builder().token(BOT_TOKEN).build()

async def ProcessInput(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.effective_user:
        return
    text = update.message.text
    logger.info("Сообщение от %s: %s", update.effective_user.id, text)
    await update.message.reply_text(f"Ты написал: {text}")

application.add_handler(MessageHandler(None, ProcessInput))