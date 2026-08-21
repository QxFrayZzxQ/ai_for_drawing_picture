import telebot
from config1 import TOKEN, POLLINATIONS_API_KEY
from logic1 import Polination_ai

bot = telebot.TeleBot(TOKEN)
polination = Polination_ai(POLLINATIONS_API_KEY)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет, я бот для создания фоток с помощью нейросети \n"
  "напиши свой промт для создания картинки ")


@bot.message_handler(func=lambda m: True)
def generate(message):
    
    status_msg = bot.reply_to(message, "🎨 Генерирую изображение...")

    
    prompt = message.text

    
    image = polination.generation_image(prompt)

    if image:
        
        bot.send_photo(message.chat.id, photo=image)
        
        bot.delete_message(message.chat.id, status_msg.message_id)
    else:
        bot.edit_message_text(
            "Не удалось сгенерировать изображение. Проверь ключ API или баланс.",
            chat_id=message.chat.id,
            message_id=status_msg.message_id
        )

if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()