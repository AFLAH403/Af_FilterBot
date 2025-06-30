import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('ഹലോ! ഞാൻ FilterBot ആണു!')

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('എന്തെങ്കിലും ചോദിക്കൂ, ഞാൻ സഹായിക്കും.')

# Basic filter - echoes messages
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if 'filter' in text.lower():
        await update.message.reply_text('ഇത് Filter ചെയ്ത ഒരു മെസേജാണ്!')
    else:
        await update.message.reply_text('നിനക്ക് എന്തേണമെങ്കിലും പറയാൻ ഉണ്ടോ?')

# Main function
def main():
    import os
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        print("⚠️ BOT_TOKEN environment variable not set!")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Bot started...")
    app.run_polling()

if __name__ == '__main__':
    main()