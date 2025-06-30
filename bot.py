import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('ഹലോ! ഞാൻ FilterBot ആണു!')

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('എന്തെങ്കിലും ചോദിക്കൂ, ഞാൻ സഹായിക്കും.')

# Echo filter: reply only if "filter" word is in message
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if 'filter' in text.lower():
        await update.message.reply_text(f"നീ പറഞ്ഞത്: {text}")

# Main function
if __name__ == '__main__':
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN_HERE").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()
