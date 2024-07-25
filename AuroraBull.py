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

# Name: AuroraBull
# Author: Felix?
# Commands:
# .abull | .abullspam | .abulloff
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/7612b5506856c1eb34c56.jpg

version = (1, 0, 0)

import json
import aiohttp
import asyncio
from random import choice
from .. import loader, utils
from telethon.tl.types import Message # type: ignore

@loader.tds
class AuroraBullMod(loader.Module):
    """Module for insults, make the interlocutor depressed."""

    strings = {
        "name": "AuroraBull",
        "error_key": "<b><i>Error: Key 'BullText' not found.</i></b>",
        "error_decoding": "<b><i>Error: The JSON could not be decoded.</i></b>",
        "error_uploading_data": "<b><i>Error loading data</i></b>",
        "error_valid_args": "<b><i>Please enter valid arguments!</i></b>",
        "launched": "<b><i>AuroraBull launched!</i></b>\n\n<b><i>Use <code>.abulloff</code> to stop the attack.</i></b>",
        "stopped": "<b><i>AuroraBull has stopped.</i></b>",
    }

    strings_ru = {
        "error_key": "<b><i>Error: ключ 'BullText' не найден.</i></b>",
        "error_decoding": "<b><i>Error: не удалось декодировать JSON.</i></b>",
        "error_uploading_data": "<b><i>Ошибка при загрузке данных</i></b>",
        "error_valid_args": "<b><i>Введите корректные аргументы!</i></b>",
        "launched": "<b><i>AuroraBull запущен!</i></b>\n\n<b><i>Используйте <code>.abulloff</code>, чтобы остановить атаку.</i></b>",
        "stopped": "<b><i>AuroraBull остановлен.</i></b>",
    }

    strings_uz = {
        "error_key": "<b><i>Error: 'BullText' калити топилмади.</i></b>",
        "error_decoding": "<b><i>Error: JSON декодлаш муваффақиятли амалга ошмади.</i></b>",
        "error_uploading_data": "<b><i>Маълумотлар юклаб олинмади</i></b>",
        "error_valid_args": "<b><i>Iltimos, to'g'ri dalillarni kiriting!</i></b>",
        "launched": "<b><i>AuroraBull ishga tushirildi!</i></b>\n\n<b><i>Hujumni toʻxtatish uchun <code>.abulloff</code> dan foydalaning.</i></b>",
        "stopped": "<b><i>AuroraBull to'xtadi.</i></b>",
    }

    strings_de = {
        "error_key": "<b><i>Error: Der Schlüssel 'BullText' wurde nicht gefunden.</i></b>",
        "error_decoding": "<b><i>Error: JSON konnte nicht decodiert werden.</i></b>",
        "error_uploading_data": "<b><i>Fehler beim Hochladen der Daten</i></b>",
        "error_valid_args": "<b><i>Bitte geben Sie gültige Argumente ein!</i></b>",
        "launched": "<b><i>AuroraBull gestartet!</i></b>\n\n<b><i>Verwenden Sie <code>.abulloff</code>, um den Angriff zu stoppen.</i></b>",
        "stopped": "<b><i>AuroraBull hat angehalten.</i></b>",
    }

    strings_es = {
        "error_key": "<b><i>Error: No se encontró la clave 'BullText'.</i></b>",
        "error_decoding": "<b><i>Error: No se pudo decodificar JSON.</i></b>",
        "error_uploading_data": "<b><i>Error al cargar los datos</i></b>",
        "error_valid_args": "<b><i>¡Por favor ingrese argumentos válidos!</i></b>",
        "launched": "<b><i>¡AuroraBull lanzado!</i></b>\n\n<b><i>Utiliza <code>.abulloff</code> para detener el ataque.</i></b>",
        "stopped": "<b><i>AuroraBull se ha detenido.</i></b>",
        
    }

    @loader.command(
        ru_doc="Оскорбите вашего собеседника.",
        uz_doc="Suhbatdoshingizni insult qiling.",
        de_doc="Beleidigen Sie Ihren Gesprächspartner.",
        es_doc="Insulta a tu interlocutor.",
    )
    async def abull(self, message):
        """Insult your interlocutor"""
        url = "https://raw.githubusercontent.com/KorenbZla/HikkaModules/main/AuroraBull.json"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    response = await response.text()
                    try:
                        data = json.loads(response)
                        if "BullText" in data and isinstance(data["BullText"], list) and data["BullText"]:
                            text = choice(data["BullText"])
                            await utils.answer(message, text)
                        else:
                            await utils.answer(message, self.strings("error_key"))
                    except json.JSONDecodeError:
                        await utils.answer(message, self.strings("error_decoding"))
                else:
                    await utils.answer(message, f"{self.strings('error_uploading_data')}: {response.status}")

    @loader.command(
        ru_doc="[time] [text] - Заспамте оскорблениями вашего собеседника",
        uz_doc="[time] [text] - Suhbatdoshingizni haqorat bilan spam qiling",
        de_doc="[time] [text] - Spammen Sie Ihren Gesprächspartner mit Beleidigungen zu",
        es_doc="[time] [text] - Spamea a tu interlocutor con insultos",
    )
    async def abullspam(self, message: Message):
        """[time] [text] - Spam your interlocutor with insults"""
        url = "https://raw.githubusercontent.com/KorenbZla/HikkaModules/main/AuroraBull.json"
        args = utils.get_args(message)

        if not args:
            await utils.answer(message, self.strings("error_valid_args"))
            return
        else:
            self.db.set(self.strings["AuroraBull"], "state", True)

        try:
            time = float(args[0])
            text = ' '.join(args[1:]) + " " if len(args) > 1 else ""
        except ValueError:
            await utils.answer(message, self.strings("error_valid_args"))
            return

        await utils.answer(message, self.strings("launched"))
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    response = await response.text()
                    
                    data = json.loads(response)
                    if "BullText" in data and isinstance(data["BullText"], list) and data["BullText"]:
                        while self.db.get(self.strings["AuroraBull"], "state"):
                            bull_text = choice(data["BullText"])
                            await message.respond(text + bull_text)
                            await asyncio.sleep(time)
                        else:
                            await utils.answer(message, self.strings("error_key"))
                    else:
                        await utils.answer(message, f"{self.strings('error_uploading_data')}: {response.status}")

    @loader.command(
        ru_doc="Остановить оскорбления",
        uz_doc="Haqoratlarni to'xtating",
        de_doc="Hört auf mit den Beleidigungen",
        es_doc="basta de insultos",
    )
    async def abulloff(self, message: Message):
        """Stop the insults"""
        self.db.set(self.strings["AuroraBull"], "state", False)
        await utils.answer(message, self.strings("stopped"))
        return
