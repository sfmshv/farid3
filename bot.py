import os
import asyncio
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, ChannelPostHandler, filters

BOT_TOKEN = "8457013459:AAF394yMjOQQ04EVGFh3v-oB-7VVIh-ba1k"
FRIEND_CHAT_ID = 54810458

# آدرس و پورت برای Render
PORT = int(os.environ.get("PORT", 5000))
WEBHOOK_URL = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/webhook"


async def forward_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """دریافت پیام‌ها و فوروارد کردن فایل‌های mp3 به چت مقصد"""
    # گرفتن پیام از کانال یا چت خصوصی
    message = update.channel_post or update.message
    if message is None:
        print("No message in update. Skipping.")
        return

    print(f"Received update type: {type(message)}")
    print(f"Message content: {message}")

    # بررسی نوع فایل صوتی
    if message.document and message.document.mime_type == "audio/mpeg":
        try:
            await context.bot.forward_message(
                chat_id=FRIEND_CHAT_ID,
                from_chat_id=message.chat.id,
                message_id=message.message_id
            )
            print("✅ Forwarded audio/mpeg successfully")
        except Exception as e:
            print(f"❌ Forward error: {e}")
    else:
        print("Message ignored: not audio/mpeg")


async def init_webhook(app: Application):
    """ثبت وبهوک در تلگرام"""
    try:
        await app.bot.set_webhook(url=WEBHOOK_URL)
        print(f"✅ Webhook set to: {WEBHOOK_URL}")
    except Exception as e:
        print(f"❌ Error in set_webhook: {e}")


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # گرفتن پیام‌ها از کانال
    app.add_handler(ChannelPostHandler(forward_music, filters.ALL))
    # گرفتن پیام‌ها از چت خصوصی
    app.add_handler(MessageHandler(filters.ALL, forward_music))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_webhook(app))

    print("🤖 Bot is live and listening via webhook...")
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path="webhook"
    )


if __name__ == "__main__":
    main()
