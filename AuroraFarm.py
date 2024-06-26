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

# Name: AuroraFarm
# Author: dend1yya 
# Commands:
# .afarm | .chatid
# scope: hikka_only
# meta developer: @AuroraModules

__version__ = (1, 0, 0)

import asyncio
import logging
from .. import loader,utils

logging = logging.getLogger("AuroraFarm")

@loader.tds
class AuroraFarmMod(loader.Module):
    """Автоматизирует вашу работу в Aurora Kynimeister"""

    strings = {
        "name": "AuroraFarm",
        "loading": "<b><emoji document_id=5253952855185829086>⚙️</emoji> Loading..</b>",
        "group_id": "Group ID",
        "enable": "<b><emoji document_id=5226828654947874694>✅</emoji> Aurora Farm succefully started.</b>",
        "disable": "<b><emoji document_id=5404553572727660202>❌</emoji> Aurora Farm succefully disabled.</b>"
    }

    strings_ru = {
        "loading": "<b><emoji document_id=5253952855185829086>⚙️</emoji> Загрузка..</b>",
        "group_id": "Айди группы",
        "enable": "<b><emoji document_id=5226828654947874694>✅</emoji> Aurora Farm успешно запущен.</b>",
        "disable": "<b><emoji document_id=5404553572727660202>❌</emoji> Aurora Farm успешно выключен.</b>"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "group_id",
                None,
                lambda: self.strings["group_id"]
            ),
        )
    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    async def afarmcmd(self, message):
        """Включает фарм в AuroraKynimeister"""
        try:
            status = self.db.get("farm_status", "status")
            msg = await utils.answer(message, self.strings["loading"])
            text = "Куни"
            group_id = self.config.get("group_id", None)

            if group_id is None: 
                bot_dialog = await message.client.get_entity("@kynimeister_bot")
                async with message.client.conversation(bot_dialog) as conv:
                    while not status:  
                        self.db.set("farm_status", "status", True)
                        await utils.answer(message, self.strings["enable"])
                        while self.db.get("farm_status", "status"):
                            await conv.send_message(text)
                            await asyncio.sleep(14444)
                if status:
                    self.db.set("farm_status", "status", False)
                    await utils.answer(message, self.strings["disable"])                            
                return

            if status:
                self.db.set("farm_status", "status", False)
                await utils.answer(message, self.strings["disable"])
            else:
                self.db.set("farm_status", "status", True)
                await utils.answer(message, self.strings["enable"])
                while self.db.get("farm_status", "status"):
                    await message.client.send_message(int(group_id), text)
                    await asyncio.sleep(14444)

        except Exception as e:
            await utils.answer(
                message,
                f"Something went wrong..\nError: {e}\n\nIf the error persists,"
                " please write about the error to me in PM: https://t.me/KorenbZla"
            )
            logging.info("An error has occurred")


    async def chatidcmd(self, message):
        """Команда .chatid показывает ID чата."""
        if message.is_private:
            return await message.edit("<b>Это не чат!</b>")
        args = utils.get_args_raw(message)
        to_chat = None

        try:
            if args:
                to_chat = int(args) if args.isdigit() else args
            else:
                to_chat = message.chat_id

        except ValueError:
            to_chat = message.chat_id

        chat = await message.client.get_entity(to_chat)

        await message.edit(
            f"<b>Название:</b> <code>{chat.title}</code>\n"
            f"<b>ID</b>: <code>{chat.id}</code>"
        )
