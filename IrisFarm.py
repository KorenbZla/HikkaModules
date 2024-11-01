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

# Name: IrisFarm
# Author: Felix?
# Commands:
# .irfarm | .bag
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/1d547b05f967c9681b90a.jpg

__version__ = (3, 1, 1)

import asyncio
import random
from .. import loader, utils

class IrisFarmMod(loader.Module):
    """Auto farm in iris bot"""

    strings = {
        "name": "IrisFarm",
        "status": "<emoji document_id=6028435952299413210>ℹ️</emoji> Module operation status",
        "s_1": "Active.",
        "s_0": "Inactive.",
        "on": "Activated.",
        "off": "Deactivated.",
        "n_args": "<emoji document_id=5285372392086976148>🚫</emoji> Specify the arguments",
        "cfg_chat_id": "Enter the chat identifier.",
        "cfg_random_interval": "WARNING! Disabling this feature increases the risk of being banned in the bot!",
    }

    strings_ru = {
        "status": "<emoji document_id=6028435952299413210>ℹ️</emoji> Статус работы модуля",
        "s_1": "Активно.",
        "s_0": "Неактивно.",
        "on": "Активировано.",
        "off": "Деактивировано.",
        "n_args": "<emoji document_id=5285372392086976148>🚫</emoji> Укажите аргументы",
        "cfg_chat_id": "Введите идентификатор чата.",
        "cfg_random_interval": "ВНИМАНИЕ! При выключении данной функции повышается риск бана в боте!",
    }

    strings_uz = {
        "status": "<emoji document_id=6028435952299413210>ℹ️</emoji> Modul ishlash holati",
        "s_1": "Faol.",
        "s_0": "Faol emas.",
        "on": "Faollashtirildi.",
        "off": "O'chirildi.",
        "n_args": "<emoji document_id=5285372392086976148>🚫</emoji> Argumentlarni kiriting",
        "cfg_chat_id": "Chat identifikatorini kiriting.",
        "cfg_random_interval": "DIQQAT! Ushbu xususiyatni o'chirib qo'yish botda ban olish xavfini oshiradi!",
    }

    strings_de = {
        "status": "<emoji document_id=6028435952299413210>ℹ️</emoji> Modulbetriebsstatus",
        "s_1": "Aktiv.",
        "s_0": "Inaktiv.",
        "on": "Aktiviert.",
        "off": "Deaktiviert.",
        "n_args": "<emoji document_id=5285372392086976148>🚫</emoji> Geben Sie die Argumente an",
        "cfg_chat_id": "Geben Sie die Chat-ID ein.",
        "cfg_random_interval": "WARNUNG! Das Deaktivieren dieser Funktion erhöht das Risiko, im Bot gebannt zu werden!",
    }

    strings_es = {
        "status": "<emoji document_id=6028435952299413210>ℹ️</emoji> Estado de operación del módulo",
        "s_1": "Activo.",
        "s_0": "Inactivo.",
        "on": "Activado.",
        "off": "Desactivado.",
        "n_args": "<emoji document_id=5285372392086976148>🚫</emoji> Especifica los argumentos",
        "cfg_chat_id": "Introduce el identificador del chat.",
        "cfg_random_interval": "¡ADVERTENCIA! Desactivar esta función aumenta el riesgo de ser baneado en el bot.",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "chat_id",
                None,
                lambda: self.strings["cfg_chat_id"]
            ),
            loader.ConfigValue(
                "random_interval",
                False,
                lambda: self.strings["cfg_random_interval"],
                validator=loader.validators.Boolean()
            )
        )

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    @loader.command()
    async def irfarm(self, message):
        """{on/off} - turn auto farm on or off"""            
        args = utils.get_args_raw(message).lower()
        
        status_result_True = self.db.get("AuroraIrisFarm", "status", True)
        if status_result_True:
            status_result = self.strings("s_1")
        else:
            status_result = self.strings("s_0")
        
        if not args:
            status = self.strings("status")
            await utils.answer(message, f"<b>{status}: <i>{status_result}</i></b>")
            return

        if args == "on":
            args_s = self.strings("on")
            self.db.set("AuroraIrisFarm", "status", True)
            await utils.answer(message, f"<emoji document_id=5287692511945437157>✅</emoji> <b>IrisFarm: <i>{args_s}</i></b>")
        elif args == "off":
            args_s = self.strings("off")
            self.db.set("AuroraIrisFarm", "status", False)
            await utils.answer(message, f"<emoji document_id=5287692511945437157>✅</emoji> <b>IrisFarm: <i>{args_s}</i></b>")
        else:
            n_args = self.strings("n_args")
            await utils.answer(message, f"<b>{n_args}</b>")
            return
        
        if self.config["chat_id"] is None:
            chat_id = 5443619563
        else:
            chat_id = self.config["chat_id"]

        if self.config["random_interval"] == True:
            delay = random.randint(14410, 28800)
        else:
            delay = 4 * 3630

        while self.db.get("AuroraIrisFarm", "status"):
            text = "фармить"
            await message.client.send_message(chat_id, text)
            await asyncio.sleep(delay)

    @loader.command(
        ru_doc = "Заглянуть в мешок.",
        uz_doc = "Sumkaga qarang.",
        de_doc = "Schau in die Tasche.",
        es_doc = "Mira en la bolsa.",
    )
    async def bag(self, message):
        """Look into the bag"""
        bot_dialog = await message.client.get_entity("@iris_black_bot")
        async with message.client.conversation(bot_dialog) as conv:
            await conv.send_message("Мешок")
            response = await conv.get_response()
            await utils.answer(message, f"<b>{(response.text)}</b>")
