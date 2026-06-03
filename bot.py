import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 1. Enable logging to see bot activity and errors in the Render logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 2. Define the /start command handler
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message when the user issues the /start command."""
    welcome_text = (
        "👋 Welcome to Friendly Chat!\n"
        "Start a friendly conversation, ask questions, and chat anytime.\n"
        "Have a great day! 😊"
    )
    # Reply directly to the user who sent the command
    await update.message.reply_text(welcome_text)

# 3. Main function to start the bot
def main() -> None:
    """Start the bot."""
    # Retrieve the bot token from Render's environment variables
    bot_token = os.environ.get("BOT_TOKEN")
    
    if not bot_token:
        logger.error("Critical Error: BOT_TOKEN environment variable not found!")
        return

    # Create the Application and pass it your bot's token
    application = Application.builder().token(bot_token).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start_command))

    # Run the bot using polling mode (perfect for Background Workers)
    logger.info("Friendly Chat Bot is starting polling...")
    application.run_polling()

if __name__ == '__main__':
    main()
