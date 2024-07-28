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

# Name: AutoDeleteMessages
# Author: Felix?
# Commands:
# .autodel
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/b3e9c4bef7348c0fda21e.jpg

__version__ = (1, 0, 0)

import asyncio
from hikkatl.types import Message # type: ignore
from .. import loader, utils

class AutoDeleteMessagesMod(loader.Module):
    """Automatically deletes all your messages in the specified chats."""
    
    strings = {
        "name": "AutoDeleteMessages",
        "status": "<emoji document_id=6028435952299413210>ℹ️</emoji> Status of AutoDeleteMessages",
        "s_True": "Active.",
        "s_False": "Inactive.",
        "on": "Activated.",
        "off": "Deactivated.",
        "n_args": "<emoji document_id=5285372392086976148>🚫</emoji> Please provide arguments",
        "error": "Error: {}",
        "cfg_chat_id": "Enter the chat ID where messages will be deleted",
        "cfg_time_delete": "Enter the interval in minutes after which your messages will be deleted",
        "cfg_error": "Configuration error or value not specified",
    }

    strings_ru = {
        "status": "<emoji document_id=6028435952299413210>ℹ️</emoji> Статус работы AutoDeleteMessages",
        "s_True": "Активно.",
        "s_False": "Неактивно.",
        "on": "Включено.",
        "off": "Выключено.",
        "n_args": "<emoji document_id=5285372392086976148>🚫</emoji> Укажите аргументы",
        "error": "Error: {}",
        "cfg_chat_id": "Введите идентификатор чата, в котором будут удаляться сообщения",
        "cfg_time_delete": "Введите интервал в минутах, через который будут удаляться ваши сообщения",
        "cfg_error": "Ошибка в конфигурации или не указано значение",
    }

    
    strings_uz = {
        "status": "<emoji document_id=6028435952299413210>ℹ️</emoji> AutoDeleteMessages holati",
        "s_True": "Faol.",
        "s_False": "Faol emas.",
        "on": "Faollashtirildi.",
        "off": "O'chirildi.",
        "n_args": "<emoji document_id=5285372392086976148>🚫</emoji> Iltimos, argumentlarni kiriting",
        "error": "Error: {}",
        "cfg_chat_id": "Xabarlar o'chiriladigan chat ID'sini kiriting",
        "cfg_time_delete": "Xabarlaringiz qachon o'chirilishini daqiqalarda kiriting",
        "cfg_error": "Konfiguratsiya xatosi yoki qiymat ko'rsatilmagan",
    }

    strings_de = {
        "status": "<emoji document_id=6028435952299413210>ℹ️</emoji> Status von AutoDeleteMessages",
        "s_True": "Aktiv.",
        "s_False": "Inaktiv.",
        "on": "Aktiviert.",
        "off": "Deaktiviert.",
        "n_args": "<emoji document_id=5285372392086976148>🚫</emoji> Bitte geben Sie Argumente an",
        "error": "Error: {}",
        "cfg_chat_id": "Geben Sie die Chat-ID ein, in der Nachrichten gelöscht werden sollen",
        "cfg_time_delete": "Geben Sie das Intervall in Minuten ein, nach dem Ihre Nachrichten gelöscht werden",
        "cfg_error": "Konfigurationsfehler oder Wert nicht angegeben",
    }

    strings_es = {
        "status": "<emoji document_id=6028435952299413210>ℹ️</emoji> Estado de AutoDeleteMessages",
        "s_True": "Activo.",
        "s_False": "Inactivo.",
        "on": "Activado.",
        "off": "Desactivado.",
        "n_args": "<emoji document_id=5285372392086976148>🚫</emoji> Por favor, proporcione argumentos",
        "error": "Error: {}",
        "cfg_chat_id": "Ingrese el ID del chat donde se eliminarán los mensajes",
        "cfg_time_delete": "Ingrese el intervalo en minutos después del cual se eliminarán sus mensajes",
        "cfg_error": "Error de configuración o valor no especificado",
    }
    
    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "chat_id",
                [],
                lambda: self.strings["cfg_chat_id"],
            ),
            loader.ConfigValue(
                "time_delete",
                15,
                lambda: self.strings["cfg_time_delete"],
                validator=loader.validators.Integer(minimum=1),
            ),
        )
        
    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        
    @loader.command(
        ru_doc="<on/off> - установить статус работы модуля.",
        uz_doc="<on/off> - modulning ish holatini sozlash.",
        de_doc="<on/off> - Den Status des Moduls festlegen.",
        es_doc="<on/off> - Establecer el estado de operación del módulo.",
    )
    async def autodel(self, message):
        """<on/off> - set the module operation status"""
        args = utils.get_args_raw(message).lower()

        if self.config["chat_id"] is None or self.config["chat_id"] == []:
            await utils.answer(message, self.strings("cfg_error"))
            return
        else:
            chat_ids = self.config["chat_id"]
        if isinstance(chat_ids, int):
            chat_ids = [chat_ids]
        elif not isinstance(chat_ids, list):
            chat_ids = []
            
        if self.config["time_delete"] == None:
            await utils.answer(message, self.strings("cfg_error"))
            return
        else:
            time = self.config["time_delete"]

        status_result_True = self.db.get("AutoDeleteMessages", "status", True)
        if status_result_True:
            status_result = self.strings("s_True")
        else:
            status_result = self.strings("s_False")
        
        if not args:
            status = self.strings("status")
            await utils.answer(message, f"<b>{status}: <i>{status_result}</i></b>")
            return

        if args == "on":
            args_s = self.strings("on")
            self.db.set("AutoDeleteMessages", "status", True)
            await utils.answer(message, f"<emoji document_id=5287692511945437157>✅</emoji> <b>AutoDeleteMessages: <i>{args_s}</i></b>")
        elif args == "off":
            args_s = self.strings("off")
            self.db.set("AutoDeleteMessages", "status", False)
            await utils.answer(message, f"<emoji document_id=5287692511945437157>✅</emoji> <b>AutoDeleteMessages: <i>{args_s}</i></b>")
        else:
            n_args = self.strings("n_args")
            await utils.answer(message, f"<b>{n_args}</b>")
            return

        await asyncio.sleep(time)
        while self.db.get("AutoDeleteMessages", "status"):
            for chat_id in chat_ids:
                try:
                    async for msg in self.client.iter_messages(chat_id, from_user="me"):
                        await msg.delete()
                except Exception as e:
                    await utils.answer(message, self.strings['error'].format(e))
            await asyncio.sleep(time)