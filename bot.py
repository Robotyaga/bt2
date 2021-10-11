import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, "Кароче юзаєш /Понеділок1 або /Понеділок2 шоб знать розклад 1 або 2 тижня")
@bot.message_handler(commands=['Понеділок1'])
def ponedilok1(message):
	bot.send_message(message.chat.id, "1 пара - Інформаційні технології 4.203(Лекція) \n 2 пара - Основи автоматизації обробки інформації 11.110(Лекція)")	

@bot.message_handler(commands=['Вівторок1'])
def vivtorok1(message):
	bot.send_message(message.chat.id, "1 пара - Фізика 1.349(Практіка)\n2 пара - Фахова іноземна мова 5.315(Практіка)")

@bot.message_handler(commands=['Середа1'])
def sereda1(message):
	bot.send_message(message.chat.id, "2 пара - ВишМат 8.106(Лекція) \n 3 пара - ОК 4.203(Лекція)\n 4 пара - ВишМат 11.214(Практіка)")

@bot.message_handler(commands=['Четвер1'])
def chetver1(message):
	bot.send_message(message.chat.id, "2 пара - ІТ 11.209(Практіка) \n 3 пара - ІТ 11.412(Лаба) \n 4 пара - ІТ 11.412(Лаба)\n 5 пара - ОК 11.104(Лаба)")

@bot.message_handler(commands=['Пятниця1'])
def pyatnica1(message):
	bot.send_message(message.chat.id, "3 пара - Фізика 4.201(Лекція)\n 4 пара - Історія 4.203")

@bot.message_handler(commands=['Понеділок2'])
def ponedilok2(message):
	bot.send_message(message.chat.id, "1 пара - Фізика 1.424(Лаба) \n2 пара - Фізика 1.424(Лаба) \n 3 пара - Історія 3.513(Практіка)")

@bot.message_handler(commands=['Вівторок2'])
def vivtorok2(message):
	bot.send_message(message.chat.id, "1 пара - ІТ 11.109(Практіка)\n 2 пара - ВишМат 3.211(Практіка)")

@bot.message_handler(commands=['Середа2'])
def sereda2(message):
	bot.send_message(message.chat.id, "1 пара - ІТ 4.203(Лекція)\n2 пара - ВишМат 8.106(Лекція\n3 пара - ОК 4.203(Лекція))")

@bot.message_handler(commands=['Четвер2'])
def chetver2(message):
	bot.send_message(message.chat.id, "1 пара - ОК 11.116(Лаба)\n2 пара - Фахова іноземна мова 3.213 (Практіка)\n3 пара - Фізика 6.201(Лекція)\n4 пара - Основи автоматизації обробки інформації 4.203(Лекція)")

@bot.message_handler(commands=['Пятниця2'])
def pyatnica2(message):
	bot.send_message(message.chat.id, "1 пара - ВишМат 11.215(Практіка)\n2 пара - Основи автоматизації обробки інформації 11.421 (Лаба)")


bot.polling(none_stop=True)
