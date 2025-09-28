from datetime import datetime
from telegram.ext import Updater, CommandHandler, Filters

# Reference workday: your friend worked on this date
reference_workday = datetime(2025, 9, 26)

def check_day(update, context):
    if not context.args:
        update.message.reply_text("Please provide a date in YYYY-MM-DD format.")
        return

    try:
        date_str = context.args[0]
        check_date = datetime.strptime(date_str, "%Y-%m-%d")
        delta_days = (check_date - reference_workday).days
        remainder = delta_days % 3

        if remainder == 0:
            reply = f"{date_str} → Work day ✅"
        else:
            reply = f"{date_str} → Rest day 😴"
    except ValueError:
        reply = "Invalid date format. Please use YYYY-MM-DD."

    update.message.reply_text(reply)

def main():
    # Replace this with your BotFather token
    updater = Updater("8399402481:AAE_tz_qytzakjLjHMwKoKurnKq8l58TWzU", use_context=True)
    dp = updater.dispatcher

    # This filter allows the bot to respond in both private and group chats
    dp.add_handler(CommandHandler("check", check_day, filters=Filters.chat_type.groups | Filters.chat_type.private))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
