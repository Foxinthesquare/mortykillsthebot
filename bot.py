import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
	# KEYBOARD
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Расписание', 'ДЗ')

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)
	bot.send_message(message.chat.id, "Приветствую, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот помощник в учебе для группы Fila-18001b.\n\n<em>Я был создан безызвестными, ленивым программистом, именуемым себя, как Foxinthesquare. Моя простая задача состоит в том, чтобы скидывать расписание занятий и домашнее задание... да, вот настолько интересна моя жизнь...</em>\n\nЧто бы начать, нажми одну из кнопок возле клавиатуры!\nВ будущем, мой создатель обещал мне, что будет добавлять новые функции и разные интересности, надеюсь он не соврал...\n\nДля связи и по всем вопросам, пиши моему создателю - <em>@foxinthesquare</em>".format(message.from_user, bot.get_me()), reply_markup=keyboard1, parse_mode='html')

@bot.message_handler(commands=['info'])
def info(message):
	bot.send_message(message.chat.id, "Это инфо, чувак!".format(message.from_user, bot.get_me()), parse_mode='html')

@bot.message_handler(commands=['all'])
def ph(message):
	bot.send_message(message.chat.id, 'Сразу все твое расписание, что бы не ебаться с кнопками! ❤\n\nP. S. Не знаю зачем вся эта фигня с кнопкапи, но походу мой создатель хотел просто поиграться с этим и разобраться, имхо.\nА вдруг кому и полезно будет :D')

	bot.send_media_group(message.chat.id, [types.InputMediaPhoto('https://imbt.ga/poczWS7NoH'), types.InputMediaPhoto('https://imbt.ga/XwNIcnAZaj'), types.InputMediaPhoto('https://imbt.ga/FOINQmsDi4'), types.InputMediaPhoto('https://imbt.ga/Rl2RWFYTb9'), types.InputMediaPhoto('https://imbt.ga/mozMd3KsP0')])

@bot.message_handler(content_types=['text'])
def yadayadayada(message):
	if message.chat.type == 'private':
		if message.text == 'Расписание':

			markup = types.InlineKeyboardMarkup()
			item1 = types.InlineKeyboardButton("😡 Понедельник", callback_data='mon',)
			item2 = types.InlineKeyboardButton("☹ Вторник", callback_data='tues')
			item3 = types.InlineKeyboardButton("😐 Среда", callback_data='wed')
			item4 = types.InlineKeyboardButton("🙂 Четверг", callback_data='thurs')
			item5 = types.InlineKeyboardButton("😀 Пятница", callback_data='fri')

			markup.add(item1, item2, item3, item4, item5)

			bot.send_message(message.chat.id, '👉 На какой день тебе скинуть расписание, друже? 👈\nИли можешь написать /all, что бы получить сразу все твое расписание на неделю! 😎', reply_markup=markup)
		elif message.text == 'ДЗ':
			bot.send_message(message.chat.id, 'Я пока что этого не умею, но меня скоро научат! :(\nА еще я смогу не только показать что тебе задали, но и ты сам сможешь записывать свои задания мне 😋')
		else:
			bot.send_message(message.chat.id, 'Даже и не знаю что сказать...')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
		if call.message:
			if call.data == 'mon':
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Твое расписание на понедельник, друже!\nНачало недели может казаться ужасным, но не унывай, это точно будет лучшая неделя в твоей жизни! 😙", reply_markup=None)
				bot.send_photo(call.message.chat.id, 'https://imbt.ga/poczWS7NoH')
			elif call.data == 'tues':
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Твое расписание на вторник, друже!\nВторник намного легче понедельника, все будет афигенно! 😉", reply_markup=None)
				bot.send_photo(call.message.chat.id, 'https://imbt.ga/XwNIcnAZaj')
			elif call.data == 'wed':
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Твое расписание на среду, друже!\nУже и среда, половина почти позади, так держать! 😋", reply_markup=None)
				bot.send_photo(call.message.chat.id, 'https://imbt.ga/FOINQmsDi4')
			elif call.data == 'thurs':
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Твое расписание на четверг, друже!\nВот и четверг уже, совсем чуточку осталось! 🤗", reply_markup=None)
				bot.send_photo(call.message.chat.id, 'https://imbt.ga/Rl2RWFYTb9')
			elif call.data == 'fri':
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Твое расписание на пятницу, друже!\nВот она, пятница! Ты молодец, еще немного и можно будет отдохнуть! 😍", reply_markup=None)
				bot.send_photo(call.message.chat.id, 'https://imbt.ga/mozMd3KsP0')

# RUN
bot.polling(none_stop=True)