import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN", "8457013459:AAF394yMjOQQ04EVGFh3v-oB-7VVIh-ba1k")
FRIEND_CHAT_ID = int(os.getenv("FRIEND_CHAT_ID", 54810458))

async def forward_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message.audio or (message.document and message.document.mime_type == "audio/mpeg"):
        await context.bot.send_message(FRIEND_CHAT_ID, "🎵 موزیک جدید از کانال:")
        await message.forward(FRIEND_CHAT_ID)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.AUDIO | filters.Document.Mp3, forward_music))
app.run_polling()
