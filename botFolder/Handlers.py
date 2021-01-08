from Estat import Estat
from GestorSkylines import GestorSkylines
from telegram import ParseMode
from telegram.ext import CommandHandler, MessageHandler, Filters

class Handlers:

    def __init__(self):
        self.text=""
        self.estat = Estat()
        self.gestorDades = GestorSkylines()
    
    # envia missatge
    def sendMessage(self, update, context, message):
        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.MARKDOWN)

    # enviar foto del buffer
    def sendPhotoBuffer(self, update, context, buffer):
        context.bot.send_photo(chat_id=update.message.chat_id, photo=buffer)

    # diferents handlers
    def getHandlers(self):
        handlers = []
        handlers.append(CommandHandler('start', self.start))
        handlers.append(CommandHandler('author', self.author))
        handlers.append(CommandHandler('help', self.help))
        handlers.append(CommandHandler('save', self.save))
        handlers.append(CommandHandler('load', self.load))
        handlers.append(CommandHandler('lst', self.lst))
        handlers.append(CommandHandler('clean', self.clean))
        handlers.append(MessageHandler(Filters.text, self.input))
        return handlers

    # benvinguda
    def start(self,update, context):
        self.sendMessage( update, context, "SkyLineBot! \nBenvinut Ignasi!")

    # display author
    def author(self,update, context):
        self.sendMessage(update, context, "SkyLineBot! \n@ Ignasi Sant i Albors, 2020")
    # display help
    def help(self, update, context):
        self.sendMessage(update, context, "Comandes:\n"+
    "/start inicia la conversa amb el Bot. \n"+
    "/help el Bot ha de contestar amb una llista de totes les possibles comandes i una breu documentació sobre el seu propòsit i ús. \n"+
    "/author el Bot ha d’escriure el nom complet de l’autor del projecte i seu correu electrònic oficial de la facultat. \n"+
    "/lst: mostra els identificadors definits i la seva corresponent àrea. \n"+
    "/clean: esborra tots els identificadors definits. \n"+
    "/save id: ha de guardar un skyline definit amb el nom id.sky. \n"+
    "/load id: ha de carregar un skyline de l’arxiu id.sky. \n")

    def clean(self,update,context):
        if update.message is not None:
            text = self.estat.clean()
            self.sendMessage(update, context, text)



    def lst(self, update, context):
        if update.message is not None:
            text = self.estat.llista()
            self.sendMessage(update, context, text)


    def save(self, update, context):
        if update.message is not None:
            id = update.message.text[6:]
            nom = update.effective_chat.first_name
            text = self.estat.save(id, nom)
            if text:
                self.sendMessage(update, context, text)
    
    def load(self, update, context):
        if update.message is not None:
            id= update.message.text[6:]
            nom = update.effective_chat.first_name
            text = self.estat.load(id, nom)
            if text:
                self.sendMessage(update, context, text)

    def input(self, update, context):
        if update.message is not None:
            input = update.message.text
            buffer, text= self.estat.inputSkyline(input)

            if buffer:
                self.sendPhotoBuffer(update, context, buffer)
            if text:
                self.sendMessage(update, context, text)

