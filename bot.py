# Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json
updater = Updater(token='728489691:AAGho7hgkh0UpFA4uVhKvveDgeEVvdzeLqg') # Токен API к Telegram
dispatcher = updater.dispatcher
# Обработка команд
def infoCommand(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text='/contact - контакты создателя бота')
def contactCommand(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text='Связаться с содателем бота можно туть @ErroRtm')
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Спасибо что запустил мея!!! Список команд можно узнать при помощи команды /info')
def textMessage(bot, update):
    request = apiai.ApiAI('9ae3777878c7475387f43885d2a48548').text_request() # Токен API к Dialogflow
    request.lang = 'ru' # На каком языке будет послан запрос
    request.session_id = 'BatlabAIBot' # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = update.message.text # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')
# Хендлеры
info_command_handler = CommandHandler('info', startCommand)
contact_command_handler = CommandHandler('contact', contactCommand)
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(info
                       _command_handler)
dispatcher.add_handler(contact_command_handler)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()