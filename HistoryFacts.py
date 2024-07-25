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

# Name: HistoryFacts
# Author: dend1yya
# Commands:
# .rfact | .hfact | .mfact | .sfact 
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/388d6138470f2036d08ed.jpg

__version__ = (1, 1, 0)

import json
import aiohttp
import asyncio
import random
from random import choice
from .. import loader, utils
from telethon.tl.types import Message # type: ignore

@loader.tds
class HistoryFactMod(loader.Module):
    """Get a random historical fact"""

    strings = {
        "name": "HistoryFact",
        "fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Random interesting fact about the Great Patriotic War:\n {}</b>",
        "adolf_fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Random fact about Adolf Hitler:\n{}</b>",
        "mussolini_fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Random fact about Benito Mussolini:\n{}</b>",
        "stalin_fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Random fact about Iosif Stalin:\n{}</b>",
        "error_key": "<b><i>Error: Key not found.</i></b>",
        "error_decoding": "<b><i>Error: The JSON could not be decoded.</i></b>",
        "error_uploading_data": "<b><i>Error loading data</i></b>",
        "error_valid_args": "<b><i>Please enter valid arguments!</i></b>",
    }

    strings_ru = {
        "fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Случайный интересный факт о Великой Отечественной войне:\n{}</b>",
        "adolf_fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Случайный факт об Адольфе Гитлере:\n{}</b>",
        "mussolini_fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Случайный факт о Бенито Муссолини:\n{}</b>",
        "stalin_fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Случайный факт об Иосифе Сталине:\n{}</b>",
        "error_key": "<b><i>Error: ключ не найден.</i></b>",
        "error_decoding": "<b><i>Error: не удалось декодировать JSON.</i></b>",
        "error_uploading_data": "<b><i>Ошибка при загрузке данных</i></b>",
        "error_valid_args": "<b><i>Введите корректные аргументы!</i></b>",
    }

    strings_uz = {
        "fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Buyuk Vatan jangiga oid qiziq fikr:\n{}</b>",
        "adolf_fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Adolf Gitler haqida tasodifiy fakt:\n{}</b>",
        "mussolini_fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Benito Mussolini haqida tasodifiy fakt:\n{}</b>",
        "stalin_fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Iosif Stalin haqida tasodifiy fakt:\n{}</b>",
        "error_key": "<b><i>Error: калити топилмади.</i></b>",
        "error_decoding": "<b><i>Error: JSON декодлаш муваффақиятли амалга ошмади.</i></b>",
        "error_uploading_data": "<b><i>Маълумотлар юклаб олинмади</i></b>",
        "error_valid_args": "<b><i>Iltimos, to'g'ri dalillarni kiriting!</i></b>",
    }

    strings_de = {
        "fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Zufällige interessante Tatsache über den Großen Vaterländischen Krieg:\n{}</b>",
        "adolf_fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Zufällige Tatsache über Adolf Hitler:\n{}</b>",
        "mussolini_fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Zufällige Tatsache über Benito Mussolini:\n{}</b>",
        "stalin_fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Zufällige Tatsache über Iosif Stalin:\n{}</b>",
        "error_key": "<b><i>Error: Der Schlüssel wurde nicht gefunden.</i></b>",
        "error_decoding": "<b><i>Error: JSON konnte nicht decodiert werden.</i></b>",
        "error_uploading_data": "<b><i>Fehler beim Hochladen der Daten</i></b>",
        "error_valid_args": "<b><i>Bitte geben Sie gültige Argumente ein!</i></b>",
    }

    strings_es = {
        "fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Hecho interesante aleatorio sobre la Gran Guerra Patria:\n{}</b>",
        "adolf_fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Hecho aleatorio sobre Adolf Hitler:\n{}</b>",
        "mussolini_fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Hecho aleatorio sobre Benito Mussolini:\n{}</b>",
        "stalin_fact": "<b><emoji document_id=5386596911463541476>📚</emoji> Hecho aleatorio sobre Iosif Stalin:\n{}</b>",
        "error_key": "<b><i>Error: No se encontró la clave.</i></b>",
        "error_decoding": "<b><i>Error: No se pudo decodificar JSON.</i></b>",
        "error_uploading_data": "<b><i>Error al cargar los datos</i></b>",
        "error_valid_args": "<b><i>¡Por favor ingrese argumentos válidos!</i></b>",
    }

    @loader.command(
        ru_doc="Вывод случайного исторического факта",
        uz_doc="tasodifiy tarixiy faktlar chiqarish",
        de_doc="Gibt eine zufällige historische Tatsache aus",
        es_doc="Muestra un hecho histórico aleatorio",
    )
    async def rfact(self, message):
        """Output a random historical fact"""
        url = "https://raw.githubusercontent.com/KorenbZla/HikkaModules/main/HistoryFacts.json"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    response_text = await response.text()
                    try:
                        data = json.loads(response_text)
                        if "RandomFact" in data and isinstance(data["RandomFact"], list) and data["RandomFact"]:
                            text = choice(data["RandomFact"])
                            await utils.answer(message, self.strings['fact'].format(text))
                        else:
                            await utils.answer(message, self.strings["error_key"])
                    except json.JSONDecodeError:
                        await utils.answer(message, self.strings["error_decoding"])
                else:
                    await utils.answer(message, f"{self.strings('error_uploading_data')}: {response.status}")
    
    @loader.command(
        ru_doc="Вывод случайного факта об Адольфе Гитлере",
        uz_doc="Adolf Gitler haqida tasodifiy faktlar chiqarish",
        de_doc="Gibt eine zufällige Tatsache über Adolf Hitler aus",
        es_doc="Muestra un hecho aleatorio sobre Adolf Hitler",
    )
    async def hfact(self, message):
        """To deduce a random fact about Adolf Hitler"""
        url = "https://raw.githubusercontent.com/KorenbZla/HikkaModules/main/HistoryFacts.json"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    response_text = await response.text()
                    try:
                        data = json.loads(response_text)
                        if "AdolfFact" in data and isinstance(data["AdolfFact"], list) and data["AdolfFact"]:
                            text = choice(data["AdolfFact"])
                            await utils.answer(message, self.strings['adolf_fact'].format(text))
                        else:
                            await utils.answer(message, self.strings["error_key"])
                    except json.JSONDecodeError:
                        await utils.answer(message, self.strings["error_decoding"])
                else:
                    await utils.answer(message, f"{self.strings('error_uploading_data')}: {response.status}")

    @loader.command(
        ru_doc="Вывести случайный факт о Бенито Муссолини",
        uz_doc="Benito Mussolini haqida tasodifiy faktlar chiqarish",
        de_doc="Gibt eine zufällige Tatsache über Benito Mussolini aus",
        es_doc="Muestra un hecho aleatorio sobre Benito Mussolini",
    )
    async def mfact(self, message):
        """To deduce a random fact about Benito Mussolini"""
        url = "https://raw.githubusercontent.com/KorenbZla/HikkaModules/main/HistoryFacts.json"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    response_text = await response.text()
                    try:
                        data = json.loads(response_text)
                        if "MussoliniFact" in data and isinstance(data["MussoliniFact"], list) and data["MussoliniFact"]:
                            text = choice(data["MussoliniFact"])
                            await utils.answer(message, self.strings['mussolini_fact'].format(text))
                        else:
                            await utils.answer(message, self.strings["error_key"])
                    except json.JSONDecodeError:
                        await utils.answer(message, self.strings["error_decoding"])
                else:
                    await utils.answer(message, f"{self.strings('error_uploading_data')}: {response.status}")

    @loader.command(
        ru_doc="Вывести случайный факт о Иосифе Сталине",
        uz_doc="Iosif Stalin haqida tasodifiy faktlar chiqarish",
        de_doc="Gibt eine zufällige Tatsache über Joseph Stalin aus",
        es_doc="Muestra un hecho aleatorio sobre Joseph Stalin",
    )
    async def sfact(self, message):
        """To deduce a random fact about Joseph Stalin"""
        url = "https://raw.githubusercontent.com/KorenbZla/HikkaModules/main/HistoryFacts.json"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    response_text = await response.text()
                    try:
                        data = json.loads(response_text)
                        if "StalinFact" in data and isinstance(data["StalinFact"], list) and data["StalinFact"]:
                            text = choice(data["StalinFact"])
                            await utils.answer(message, self.strings['stalin_fact'].format(text))
                        else:
                            await utils.answer(message, self.strings["error_key"])
                    except json.JSONDecodeError:
                        await utils.answer(message, self.strings["error_decoding"])
                else:
                    await utils.answer(message, f"{self.strings('error_uploading_data')}: {response.status}")
