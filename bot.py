from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "YOUR_TOKEN_HERE"  # Yahan apna token paste karna
GROUP_LINK = "https://t.me/+R_UpvvhNyQw1NDQ9"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "🎉 *Aye bhai, swagat hai tera!*\n\n"
        "Ek aisi jagah jahan:\n"
        "💬 Bindaas baatein hoti hain\n"
        "😂 Masti aur mazak chalti rehti hai\n"
        "🤝 Asli log, asli yaari\n\n"
        "Akela kyun baitha hai? \n"
        "Aa ja group mein aur family ka hissa ban ja! 👇🔥"
    )

    keyboard = [[InlineKeyboardButton("🚀 Abhi Join Karo!", url=GROUP_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        welcome_text,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot chal raha hai...")
    app.run_polling()

if __name__ == "__main__":
    main()
