from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from googletrans import Translator

updater = Updater('5071491964:AAEPAHpy7dFhmWCN0aTD0qeH58LAxFK6kfo',use_context = True )

def start(updater,context):
 updater.message.reply_text("👋🏻Salom, Men Tarjimon botman!Botga tarjima qilmoqchi bo'lgan so'zingizni jo'nating!")
 
def echo(updater,context):
 usr_msg =updater.message.text
 translator = Translator()
 translation = translator.translate(usr_msg,dest='hi') 
 updater.message.reply_text(translation.text)
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
