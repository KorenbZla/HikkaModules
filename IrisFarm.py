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
# Author: dend1yya
# Commands:
# .farmon | .farmoff | .bag
# scope: hikka_only
# meta developer: @AuroraModules

__version__ = (1, 0, 0)


import asyncio
import logging
from .. import loader,utils

logging = logging.getLogger("IrisFarm")

@loader.tds
class IrisFarmMod(loader.Module):
    """Автоматизирует вашу работу в Iris Chat Manager"""

    strings = {
        "name": "IrisFarm",
        "loading": "<b><emoji document_id=5253952855185829086>⚙️</emoji> Loading..</b>",
        "group_id": "Group ID",
        "enable": "<b><emoji document_id=5226828654947874694>✅</emoji> Iris Farm succefully started.</b>",
        "disable": "<b><emoji document_id=5404553572727660202>❌</emoji> Iris Farm succefully disabled.</b>"
    }

    strings_ru = {
        "loading": "<b><emoji document_id=5253952855185829086>⚙️</emoji> Загрузка..</b>",
        "group_id": "Айди группы",
        "enable": "<b><emoji document_id=5226828654947874694>✅</emoji> Iris Farm успешно запущен.</b>",
        "disable": "<b><emoji document_id=5404553572727660202>❌</emoji> Iris Farm успешно выключен.</b>"
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

    async def farmoncmd(self, message):
        """Включает фарм в Iris Chat Manager"""
        await utils.answer(message, self.strings["loading"])
        group_id = self.config.get("group_id", None)
        self.db.set("IrisFarm", "status", True)

        if group_id is None or group_id == 0:
            bot_dialog = await message.client.get_entity("@iris_black_bot")
            async with message.client.conversation(bot_dialog) as conv:
                await utils.answer(message, self.strings["enable"])
                while self.db.get("IrisFarm", "status"):
                    await conv.send_message("Фармить")
                    await asyncio.sleep(14444)
        else:
            await utils.answer(message, self.strings["enable"])
            while self.db.get("IrisFarm", "status"):
                await message.client.send_message(int(group_id), "Фармить")
                await asyncio.sleep(14444)

    async def farmoffcmd(self, message):
        """Выключает фарм в Iris Chat Manager"""
        self.db.set("IrisFarm", "status", False)
        await utils.answer(message, self.strings["disable"])

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

    async def bagcmd(self, message):
        """Показывает ваш мешок"""
        bot_dialog = await message.client.get_entity("@iris_black_bot")
        async with message.client.conversation(bot_dialog) as conv:
            await conv.send_message("Мешок")
            response = await conv.get_response()
            await utils.answer(message, f"<b>{(response.text)}</b>")
