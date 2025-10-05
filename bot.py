import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = "8457013459:AAF394yMjOQQ04EVGFh3v-oB-7VVIh-ba1k"
FRIEND_CHAT_ID = 54810458

WEBHOOK_URL = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{BOT_TOKEN}"

async def forward_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message is None:
        return
    if message.audio or (message.document and message.document.mime_type == "audio/mpeg"):
        await context.bot.send_message(FRIEND_CHAT_ID, "🎵 موزیک جدید از کانال:")
        await message.forward(FRIEND_CHAT_ID)

# ساخت اپلیکیشن
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.AUDIO | filters.Document.ALL, forward_music))

# ثبت وبهوک قبل از اجرا
async def init_webhook():
    await app.bot.set_webhook(url=WEBHOOK_URL)

asyncio.get_event_loop().run_until_complete(init_webhook())

# اجرای وبهوک
app.run_webhook(
    listen="0.0.0.0",
    port=int(os.environ.get("PORT", 8443)),
    url_path=BOT_TOKEN,
    webhook_url=WEBHOOK_URL
)
