from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8080540085:AAG65x6WWyLkVI4hjfG2r4gcwhMPhZx8UBg"

trigger_words = ['men', 'man', 'мен', 'ман']

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        message_text = update.message.text.lower()
        if any(word in message_text for word in trigger_words):
            await update.message.reply_text("@Nargizaopa1 Amirovaga yozing")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()