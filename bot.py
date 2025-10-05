import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# ===== تنظیمات پایه =====
BOT_TOKEN = "8457013459:AAF394yMjOQQ04EVGFh3v-oB-7VVIh-ba1k"  # توکن ربات
FRIEND_CHAT_ID = 54810458  # chat_id دوست

# ===== تابع اصلی فوروارد =====
async def forward_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    # اگر این آپدیت هیچ پیام ندارد، خروج
    if message is None:
        return

    # بررسی برای صوت یا فایل mp3
    if message.audio or (message.document and message.document.mime_type == "audio/mpeg"):
        await context.bot.send_message(FRIEND_CHAT_ID, "🎵 موزیک جدید از کانال:")
        await message.forward(FRIEND_CHAT_ID)

# ===== راه‌اندازی اپلیکیشن =====
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.AUDIO | filters.Document.ALL, forward_music))

    print("ربات فعال شد و در حال گوش دادن است...")
    app.run_polling()
