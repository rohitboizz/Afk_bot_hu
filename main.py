import telebot

TOKEN = "APNA_TOKEN_YAHA_DAALO"
bot = telebot.TeleBot(TOKEN)

afk_users = {}

@bot.message_handler(commands=['afk'])
def set_afk(message):
    reason = " ".join(message.text.split()[1:]) or "AFK hu"
    afk_users[message.from_user.id] = reason
    bot.reply_to(message, f"Tu AFK ho gaya: {reason}")

@bot.message_handler(commands=['back'])
def back(message):
    afk_users.pop(message.from_user.id, None)
    bot.reply_to(message, "Wapas aa gaya!")

@bot.message_handler(func=lambda m: True)
def check_afk(message):
    for user_id, reason in afk_users.items():
        if f"@{message.from_user.username}" in message.text or str(user_id) in message.text:
            bot.reply_to(message, f"Wo abhi AFK hai: {reason}")
            return

bot.polling()
