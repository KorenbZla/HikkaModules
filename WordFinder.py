# *      _                             __  __           _       _
# *     / \  _   _ _ __ ___  _ __ __ _|  \/  | ___   __| |_   _| | ___  ___ 
# *    / _ \| | | | '__/ _ \| '__/ _` | |\/| |/ _ \ / _` | | | | |/ _ \/ __|
# *   / ___ \ |_| | | | (_) | | | (_| | |  | | (_) | (_| | |_| | |  __/\__ \
# *  /_/   \_\__,_|_|  \___/|_|  \__,_|_|  |_|\___/ \__,_|\__,_|_|\___||___/
# *
# *                          © Copyright 2024
# *
# *                      https://t.me/AuroraModules
# *
# * 🔒 Code is licensed under GNU AGPLv3
# * 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# * ⛔️ You CANNOT edit this file without direct permission from the author.
# * ⛔️ You CANNOT distribute this file if you have modified it without the direct permission of the author.

# Name: WordFinder
# Author: Felix?
# Commands:
# .wfind
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/c34c0a11aabd6a1fb6210.jpg

__version__ = (1, 0, 0)

from aiogram.types import Message as AiogramMessage
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .. import loader, utils

@loader.tds
class WordFinderMod(loader.Module):
    """Universal module for searching for certain words in the text."""
    
    strings = {
        "name": "WordFinder",
        "status_t": "<emoji document_id=5879785854284599288>ℹ️</emoji> <b>Module status: <i>Works</i></b>",
        "status_f": "<emoji document_id=5879785854284599288>ℹ️</emoji> <b>Module status: <i>Does not work</i></b>",
        "chat_id_error": "<emoji document_id=5879813604068298387>❗️</emoji> <b>There is no value in the chat_id config or it is incorrect.</b>",
        "words_error": "<emoji document_id=5879813604068298387>❗️</emoji> </b>There is no value in the words config or it is incorrect.</b>",
        "enabled": "<emoji document_id=5776375003280838798>✅</emoji> <b>The module is enabled.</b>",
        "disabled": "<emoji document_id=5776375003280838798>✅</emoji> <b>The module is disabled.</b>",
        "incorrect_args": "<emoji document_id=5778527486270770928>❌</emoji> <b>Incorrect arguments have been entered.</b>",
        "message_found": "⚠ <b>New message has been found</b> ⚠\n\n<code>{}</code>\n\n<b>The found word: <i>{}</i></b>",   
        "": "",
        "cfg_chat_id": "Enter the id of the chats or channels in which the words from the words config will be searched.",
        "cfg_words": "Enter the words separated by commas that will be searched in the chats.",
        "cfg_admin_chat_id": "Enter the chat id where notifications will be sent, if the value is None, the chat for notifications will be Word-Finder.",
    }
    
    strings_ru = {
        "status_t": "<emoji document_id=5879785854284599288>ℹ️</emoji> <b>Статус модуля: <i>Работает</i></b>",
        "status_f": "<emoji document_id=5879785854284599288>ℹ️</emoji> <b>Статус модуля: <i>Не работает</i></b>",
        "chat_id_error": "<emoji document_id=5879813604068298387>❗️</emoji> <b>В конфиге chat_id нет значения или оно неверное.</b>",
        "words_error": "<emoji document_id=5879813604068298387>❗️</emoji> <b>В конфиге words нет значения или оно неверное.</b>",
        "enabled": "<emoji document_id=5776375003280838798>✅</emoji> <b>Модуль включен.</b>",
        "disabled": "<emoji document_id=5776375003280838798>✅</emoji> <b>Модуль отключен.</b>",
        "incorrect_args": "<emoji document_id=5778527486270770928>❌</emoji> <b>Были введены неверные аргументы.</b>",
        "message_found": "⚠ <b>Найдено новое сообщение</b> ⚠\n\n<code>{}</code>\n\n<b>Найденное слово: <i>{}</i></b>",
        "cfg_chat_id": "Введите id чатов или каналов, в которых будут искаться слова из конфига words.",
        "cfg_words": "Введите слова через запятую, которые будут искаться в чатах.",
        "cfg_admin_chat_id": "Введите id чата, куда будут присылаться уведомления, если значение None, чатом для уведомлений будет Word-Finder.",
    }

    strings_uz = {
        "status_t": "<emoji document_id=5879785854284599288>ℹ️</emoji> <b>Modul holati: <i>Faol</i></b>",
        "status_f": "<emoji document_id=5879785854284599288>ℹ️</emoji> <b>Modul holati: <i>Faol emas</i></b>",
        "chat_id_error": "<emoji document_id=5879813604068298387>❗️</emoji> <b>Konfiguratsiyada chat_id qiymati mavjud emas yoki noto'g'ri.</b>",
        "words_error": "<emoji document_id=5879813604068298387>❗️</emoji> <b>Konfiguratsiyada words qiymati mavjud emas yoki noto'g'ri.</b>",
        "enabled": "<emoji document_id=5776375003280838798>✅</emoji> <b>Modul yoqildi.</b>",
        "disabled": "<emoji document_id=5776375003280838798>✅</emoji> <b>Modul o'chirildi.</b>",
        "incorrect_args": "<emoji document_id=5778527486270770928>❌</emoji> <b>Noto'g'ri argumentlar kiritildi.</b>",
        "message_found": "⚠ <b>Yangi xabar topildi</b> ⚠\n\n<code>{}</code>\n\n<b>Topilgan so'z: <i>{}</i></b>",
        "cfg_chat_id": "So'zlar izlanadigan chat yoki kanal idlarini kiriting.",
        "cfg_words": "Chatlarda izlanadigan so'zlarni vergul bilan ajratib kiriting.",
        "cfg_admin_chat_id": "Bildirishnomalar yuboriladigan chat idini kiriting. Agar None bo'lsa, Word-Finder bildirishnomalar uchun ishlatiladi.",
    }

    strings_de = {
        "status_t": "<emoji document_id=5879785854284599288>ℹ️</emoji> <b>Modulstatus: <i>Aktiv</i></b>",
        "status_f": "<emoji document_id=5879785854284599288>ℹ️</emoji> <b>Modulstatus: <i>Inaktiv</i></b>",
        "chat_id_error": "<emoji document_id=5879813604068298387>❗️</emoji> <b>Im Konfigurationswert chat_id fehlt oder ist ungültig.</b>",
        "words_error": "<emoji document_id=5879813604068298387>❗️</emoji> <b>Im Konfigurationswert words fehlt oder ist ungültig.</b>",
        "enabled": "<emoji document_id=5776375003280838798>✅</emoji> <b>Modul aktiviert.</b>",
        "disabled": "<emoji document_id=5776375003280838798>✅</emoji> <b>Modul deaktiviert.</b>",
        "incorrect_args": "<emoji document_id=5778527486270770928>❌</emoji> <b>Ungültige Argumente eingegeben.</b>",
        "message_found": "⚠ <b>Neue Nachricht gefunden</b> ⚠\n\n<code>{}</code>\n\n<b>Gefundenes Wort: <i>{}</i></b>",
        "cfg_chat_id": "Geben Sie die IDs der Chats oder Kanäle ein, in denen nach Wörtern aus der Konfiguration gesucht werden soll.",
        "cfg_words": "Geben Sie die zu suchenden Wörter in den Chats durch Kommas getrennt ein.",
        "cfg_admin_chat_id": "Geben Sie die ID des Chats ein, in dem Benachrichtigungen gesendet werden sollen. Wenn None, wird Word-Finder für Benachrichtigungen verwendet.",
    }

    strings_es = {
        "status_t": "<emoji document_id=5879785854284599288>ℹ️</emoji> <b>Estado del módulo: <i>Activo</i></b>",
        "status_f": "<emoji document_id=5879785854284599288>ℹ️</emoji> <b>Estado del módulo: <i>Inactivo</i></b>",
        "chat_id_error": "<emoji document_id=5879813604068298387>❗️</emoji> <b>El valor de chat_id en la configuración no está presente o es incorrecto.</b>",
        "words_error": "<emoji document_id=5879813604068298387>❗️</emoji> <b>El valor de words en la configuración no está presente o es incorrecto.</b>",
        "enabled": "<emoji document_id=5776375003280838798>✅</emoji> <b>Módulo activado.</b>",
        "disabled": "<emoji document_id=5776375003280838798>✅</emoji> <b>Módulo desactivado.</b>",
        "incorrect_args": "<emoji document_id=5778527486270770928>❌</emoji> <b>Se ingresaron argumentos incorrectos.</b>",
        "message_found": "⚠ <b>Se encontró un nuevo mensaje</b> ⚠\n\n<code>{}</code>\n\n<b>Palabra encontrada: <i>{}</i></b>",
        "cfg_chat_id": "Ingrese las IDs de los chats o canales donde se buscarán las palabras de la configuración.",
        "cfg_words": "Ingrese las palabras a buscar en los chats separadas por comas.",
        "cfg_admin_chat_id": "Ingrese la ID del chat donde se enviarán las notificaciones. Si es None, se utilizará Word-Finder para las notificaciones.",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "chat_id",
                None,
                lambda: self.strings("cfg_chat_id")
            ),
            loader.ConfigValue(
                "words",
                [],
                lambda: self.strings("cfg_words")
            ),
            loader.ConfigValue(
                "admin_chat_id",
                None,
                lambda: self.strings("cfg_admin_chat_id")
            ),
        )

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.c, _ = await utils.asset_channel(
            self.client,
            "Word-Finder",
            "Chat for receiving notifications about finding a word in the text.",
            silent=True,
            invite_bot=True,
        )
        self.chat = f"-100{self.c.id}"

    @loader.command(
        ru_doc="<on/off> - установить статус работы модуля",
        uz_doc="<on/off> - o'rnatish modulining ish holati",
        de_doc="<on/off> - den Betriebsstatus des Moduls festlegen",
        es_doc="<on/off> - establecer el estado de funcionamiento del módulo",
    )
    async def wfind(self, message):
        """<on/off> - set the module operation status"""
        
        args = utils.get_args_raw(message).lower()
        chat_id = self.config["chat_id"]
        words = self.config["words"]
        
        if not args:
            if self.db.get("WordFinder", "status"):
                status = self.strings("status_t")
            else:
                status = self.strings("status_f")
            await utils.answer(message, status)
            return

        if chat_id == None:
            await utils.answer(message, self.strings("chat_id_error"))
            return
        if words is None or words == []:
            await utils.answer(message, self.strings("words_error"))
            return
        
        if args == "on":
            self.db.set("WordFinder", "status", True)
            await utils.answer(message, self.strings("enabled"))
            return
        elif args == "off":
            self.db.set("WordFinder", "status", False)
            await utils.answer(message, self.strings("disabled"))
            return
        else:
            await utils.answer(message, self.strings("incorrect_args"))
            return
        
    async def watcher(self, message: AiogramMessage):
        if not self.db.get("WordFinder", "status", False):
            return

        chat_id = self.config["chat_id"]
        words = self.config["words"]
        admin_chat_id = self.config["admin_chat_id"]

        if isinstance(chat_id, int):
            chat_ids = [chat_id]
        elif isinstance(chat_id, list):
            chat_ids = chat_id
        else:
            return

        if isinstance(words, str):
            words = [word.strip() for word in words.split(',')]

        if message.chat_id not in chat_ids:
            return

        if not message.text:
            return
        
        if any(word in message.text.lower().split() for word in words):
            
            found_words = [word for word in words if word in message.text.lower()]
            if found_words:
                found_word = ', '.join(found_words)

            
            if message.is_private:
                message_url = f"tg://openmessage?user_id={message.chat_id}"
            else:
                message_url = f"https://t.me/c/{message.chat.id}/{message.id}"

            if self.config["admin_chat_id"] == None:
                reply_markup = InlineKeyboardMarkup()
                reply_markup.add(InlineKeyboardButton(text="🔗 Link", url=message_url))
                await self.inline.bot.send_message(
                    self.chat,
                    self.strings("message_found").format(message.text, found_word),
                    reply_markup=reply_markup
                )
            else:
                await self.inline.form(
                    message=admin_chat_id,
                    text=self.strings("message_found").format(message.text, found_word),
                    reply_markup=[
                        [
                            {"text": "🔗 Link", "url": message_url}
                        ],
                    ],
                )