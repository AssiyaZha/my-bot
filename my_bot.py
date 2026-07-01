import telebot
from telebot import types

# ВАШ НОВЫЙ ТОКЕН
TOKEN = '8582261966:AAHxn8VvqvPbYcSCKXKFhwU2CeC62D0k_94'
MY_ID = 267329584  

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🏠 Sell Property", "🏢 Sell Business", "🔍 Buy Property", "📞 Request Call")
    
    welcome_text = (
        "Hello! I am the Digital Assistant for Assiya from RE/MAX Top Nest. 😊\n\n"
        "Whether you are looking to buy or sell a property or a business in New York, "
        "I am here to help you get started. How can I assist you today?"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    actions = ["🏠 Sell Property", "🏢 Sell Business", "🔍 Buy Property", "📞 Request Call"]
    
    if message.text in actions:
        bot.send_message(message.chat.id, "Great! Please provide your details (such as the property address, business description, or your phone number), and Assiya will get back to you shortly.")
        bot.send_message(MY_ID, f"🔔 New inquiry: {message.text}\nFrom: @{message.from_user.username or 'No username'}\nID: {message.chat.id}")
        
    else:
        bot.send_message(message.chat.id, "Thank you! I have forwarded your message to Assiya, and she will reach out to you soon.")
        bot.send_message(MY_ID, f"📩 New message from @{message.from_user.username or 'No username'}:\n\n{message.text}")

print("Bot is running!")
bot.polling(none_stop=True)