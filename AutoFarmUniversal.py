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

# Name: AutoFarmUniversal
# Author: Felix?
# Commands:
# .ufarm
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/77e64e3d33263a669125f.jpg

__version__ = (1, 0, 0)

import asyncio
import random
from .. import loader, utils

@loader.tds
class AutoFarmUniversalMod(loader.Module):
    """Universal auto farmer with settings in the config"""

    strings = {
        "name": "AutoFarmUniversal",
        "status": "<emoji document_id=6028435952299413210>ℹ️</emoji> Module operation status",
        "s_1": "Active.",
        "s_0": "Inactive.",
        "on": "Activated.",
        "off": "Deactivated.",
        "n_args": "<emoji document_id=5285372392086976148>🚫</emoji> Specify the arguments",
        "error_cfg": "<emoji document_id=5287611315588707430>❌</emoji> <b>Error! Incorrect config value.</b>",
        "cfg_chat_id": "Enter the chat identifier.",
        "cfg_text": "Enter the text that will be sent.",
        "cfg_time_delay": "Enter the delay in seconds",
        "random_time_delay_min": "Enter the minimum value after how long the command will be sent",
        "random_time_delay_max": "Enter the maximum value after how long the command will be sent",
    }
    
    strings_ru = {
        "status": "<emoji document_id=6028435952299413210>ℹ️</emoji> Статус работы модуля",
        "s_1": "Активно.",
        "s_0": "Неактивно.",
        "on": "Активировано.",
        "off": "Деактивировано.",
        "n_args": "<emoji document_id=5285372392086976148>🚫</emoji> Укажите аргументы",
        "error_cfg": "<emoji document_id=5287611315588707430>❌</emoji> <b>Ошибка! Неверное значение конфигурации.</b>",
        "cfg_chat_id": "Введите идентификатор чата.",
        "cfg_text": "Введите текст, который будет отправлен.",
        "cfg_time_delay": "Введите задержку в секундах",
        "random_time_delay_min": "Введите минимальное значение времени, через которое будет отправлена команда",
        "random_time_delay_max": "Введите максимальное значение времени, через которое будет отправлена команда",
    }

    strings_uz = {
        "status": "<emoji document_id=6028435952299413210>ℹ️</emoji> Modul ishlash holati",
        "s_1": "Faol.",
        "s_0": "Faol emas.",
        "on": "Faollashtirildi.",
        "off": "O'chirildi.",
        "n_args": "<emoji document_id=5285372392086976148>🚫</emoji> Argumentlarni kiriting",
        "error_cfg": "<emoji document_id=5287611315588707430>❌</emoji> <b>Xato! Noto'g'ri konfiguratsiya qiymati.</b>",
        "cfg_chat_id": "Chat identifikatorini kiriting.",
        "cfg_text": "Yuboriladigan matnni kiriting.",
        "cfg_time_delay": "Kechikishni sekundlarda kiriting",
        "random_time_delay_min": "Buyruq yuboriladigan minimal vaqtni kiriting",
        "random_time_delay_max": "Buyruq yuboriladigan maksimal vaqtni kiriting",
    }

    strings_de = {
        "status": "<emoji document_id=6028435952299413210>ℹ️</emoji> Modulbetriebsstatus",
        "s_1": "Aktiv.",
        "s_0": "Inaktiv.",
        "on": "Aktiviert.",
        "off": "Deaktiviert.",
        "n_args": "<emoji document_id=5285372392086976148>🚫</emoji> Geben Sie die Argumente an",
        "error_cfg": "<emoji document_id=5287611315588707430>❌</emoji> <b>Fehler! Ungültiger Konfigurationswert.</b>",
        "cfg_chat_id": "Geben Sie die Chat-ID ein.",
        "cfg_text": "Geben Sie den zu sendenden Text ein.",
        "cfg_time_delay": "Geben Sie die Verzögerung in Sekunden ein",
        "random_time_delay_min": "Geben Sie den minimalen Wert an, nach dem der Befehl gesendet wird",
        "random_time_delay_max": "Geben Sie den maximalen Wert an, nach dem der Befehl gesendet wird",
    }

    strings_es = {
        "status": "<emoji document_id=6028435952299413210>ℹ️</emoji> Estado de operación del módulo",
        "s_1": "Activo.",
        "s_0": "Inactivo.",
        "on": "Activado.",
        "off": "Desactivado.",
        "n_args": "<emoji document_id=5285372392086976148>🚫</emoji> Especifica los argumentos",
        "error_cfg": "<emoji document_id=5287611315588707430>❌</emoji> <b>Error! Valor de configuración incorrecto.</b>",
        "cfg_chat_id": "Introduce el identificador del chat.",
        "cfg_text": "Introduce el texto que se enviará.",
        "cfg_time_delay": "Introduce el retraso en segundos",
        "random_time_delay_min": "Introduce el valor mínimo después del cual se enviará el comando",
        "random_time_delay_max": "Introduce el valor máximo después del cual se enviará el comando",
    }


    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "chat_id",
                None,
                lambda: self.strings["cfg_chat_id"]
            ),
            loader.ConfigValue(
                "text",
                None,
                lambda: self.strings["cfg_text"]
            ),
            loader.ConfigValue(
                "time_delay",
                None,
                lambda: self.strings["cfg_time_delay"],
                validator=loader.validators.Integer(minimum=1),
            ),
            loader.ConfigValue(
                "random_time_delay_min",
                None,
                lambda: self.strings["cfg_random_time_delay_min"],
                validator=loader.validators.Integer(minimum=1),
            ),
            loader.ConfigValue(
                "random_time_delay_max",
                None,
                lambda: self.strings["cfg_random_time_delay_max"],
                validator=loader.validators.Integer(minimum=2),
            ),
        )

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    @loader.command(
        ru_doc="{on/off} - включить или выключить автоматическую фарминг",
        uz_doc="{on/off} - avtomatik fermani yoqish yoki o'chirish",
        de_doc="{on/off} - Auto-Farm ein- oder ausschalten",
        es_doc="{on/off} - activar o desactivar la auto-granja",
    )
    async def ufarm(self, message):
        """{on/off} - turn auto farm on or off"""            
        args = utils.get_args_raw(message).lower()
        
        status_result_True = self.db.get("AutoFarmUniversal", "status", True)
        if status_result_True:
            status_result = self.strings("s_1")
        else:
            status_result = self.strings("s_0")
        
        error_cfg = self.strings("error_cfg")
        time_delay = self.config["time_delay"] 
        random_time_delay = self.config["random_time_delay_min"] or self.config["random_time_delay_max"] 
        if self.config["chat_id"] == None:
            await utils.answer(message, f"<b>{error_cfg}</b>")
            self.db.set("AutoFarmUniversal", "status", False)
            await self.allmodules.commands["config"](await message.client.send_message(message.chat_id, f"{self.get_prefix()}cfg AutoFarmUniversal"))
            return
        if self.config["text"] == None:
            await utils.answer(message, f"<b>{error_cfg}</b>")
            self.db.set("AutoFarmUniversal", "status", False)
            await self.allmodules.commands["config"](await message.client.send_message(message.chat_id, f"{self.get_prefix()}cfg AutoFarmUniversal"))
            return
        if (time_delay is not None and time_delay != 0) and (random_time_delay is not None and random_time_delay != 0):
            await utils.answer(message, f"<b>{error_cfg}</b>")
            self.db.set("AutoFarmUniversal", "status", False)
            await self.allmodules.commands["config"](await message.client.send_message(message.chat_id, f"{self.get_prefix()}cfg AutoFarmUniversal"))
            return
        if (time_delay is None or time_delay == 0) and (random_time_delay is None or random_time_delay == 0):
            await utils.answer(message, f"<b>{error_cfg}</b>")
            self.db.set("AutoFarmUniversal", "status", False)
            await self.allmodules.commands["config"](await message.client.send_message(message.chat_id, f"{self.get_prefix()}cfg AutoFarmUniversal"))
            return
        
        if not args:
            status = self.strings("status")
            await utils.answer(message, f"<b>{status}: <i>{status_result}</i></b>")
            return

        if args == "on":
            args_s = self.strings("on")
            self.db.set("AutoFarmUniversal", "status", True)
            await utils.answer(message, f"<emoji document_id=5287692511945437157>✅</emoji> <b>AutoFarmUniversal: <i>{args_s}</i></b>")
        elif args == "off":
            args_s = self.strings("off")
            self.db.set("AutoFarmUniversal", "status", False)
            await utils.answer(message, f"<emoji document_id=5287692511945437157>✅</emoji> <b>AutoFarmUniversal: <i>{args_s}</i></b>")
        else:
            n_args = self.strings("n_args")
            await utils.answer(message, f"<b>{n_args}</b>")
            return
        
        chat_id = self.config["chat_id"]
        text = self.config["text"]
    
        if time_delay is not None and time_delay != 0:
            while self.db.get("AutoFarmUniversal", "status"):
                await message.client.send_message(chat_id, str(text))
                time = self.config["time_delay"]
                await asyncio.sleep(time)

        if random_time_delay is not None and random_time_delay != 0:
            while self.db.get("AutoFarmUniversal", "status"):
                min_delay = self.config['random_time_delay_min']
                max_delay = self.config['random_time_delay_max']
                r_time = random.randint(min_delay, max_delay)
                await message.client.send_message(chat_id, str(text))
                await asyncio.sleep(r_time)
