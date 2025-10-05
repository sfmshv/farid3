import zipfile
import os

# محتواهای فایل bot.py
bot_code = """import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8457013459:AAF394yMjOQQ04EVGFh3v-oB-7VVIh-ba1k"
FRIEND_CHAT_ID = 54810458

async def forward_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message.audio or (message.document and message.document.mime_type == "audio/mpeg"):
        await context.bot.send_message(FRIEND_CHAT_ID, "🎵 موزیک جدید از کانال:")
        await message.forward(FRIEND_CHAT_ID)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.AUDIO | filters.Document.ALL, forward_music))

app.run_polling()
"""

# محتواهای فایل requirements.txt
requirements_content = """python-telegram-bot==20.3
"""

# محتواهای فایل Procfile
procfile_content = """worker: python bot.py
"""

# مسیر ذخیره پکیج
zip_path = '/mnt/data/telegram_bot_render_fixed.zip'

# ساخت فایل‌های موقت
os.makedirs('/mnt/data/telegram_bot_render_fixed', exist_ok=True)
with open('/mnt/data/telegram_bot_render_fixed/bot.py', 'w') as f:
    f.write(bot_code)
with open('/mnt/data/telegram_bot_render_fixed/requirements.txt', 'w') as f:
    f.write(requirements_content)
with open('/mnt/data/telegram_bot_render_fixed/Procfile', 'w') as f:
    f.write(procfile_content)

# فشرده‌سازی
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write('/mnt/data/telegram_bot_render_fixed/bot.py', arcname='bot.py')
    zipf.write('/mnt/data/telegram_bot_render_fixed/requirements.txt', arcname='requirements.txt')
    zipf.write('/mnt/data/telegram_bot_render_fixed/Procfile', arcname='Procfile')

zip_path
