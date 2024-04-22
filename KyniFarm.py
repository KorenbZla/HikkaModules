# *
# *              $$\       $$\   $$\                                   $$\           $$\
# *              $$ |      \__|  $$ |                                  $$ |          $$ |
# *     $$$$$$$\ $$$$$$$\  $$\ $$$$$$\   $$$$$$\$$$$\   $$$$$$\   $$$$$$$ |$$\   $$\ $$ | $$$$$$\   $$$$$$$\
# *    $$  _____|$$  __$$\ $$ |\_$$  _|  $$  _$$  _$$\ $$  __$$\ $$  __$$ |$$ |  $$ |$$ |$$  __$$\ $$  _____|
# *    \$$$$$$\  $$ |  $$ |$$ |  $$ |    $$ / $$ / $$ |$$ /  $$ |$$ /  $$ |$$ |  $$ |$$ |$$$$$$$$ |\$$$$$$\
# *     \____$$\ $$ |  $$ |$$ |  $$ |$$\ $$ | $$ | $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |$$   ____| \____$$\
# *    $$$$$$$  |$$ |  $$ |$$ |  \$$$$  |$$ | $$ | $$ |\$$$$$$  |\$$$$$$$ |\$$$$$$  |$$ |\$$$$$$$\ $$$$$$$  |
# *    \_______/ \__|  \__|\__|   \____/ \__| \__| \__| \______/  \_______| \______/ \__| \_______|\_______/
# *
# *
# *            © Copyright 2023
# *
# *         https://t.me/shitmodules
# *
# 🔒 Code is licensed under CC-BY-NC-ND 4.0 unless otherwise specified.
# 🌐 https://creativecommons.org/licenses/by-nc-nd/4.0/
# You CANNOT edit this file without direct permission from the author.
# You can redistribute this file without any changes.

# This module is a fork, I did not want to offend or offend the author, but if I did it anyway, please write to me, I will be ready to apologize.
# Channel of the author of the original module: https://t.me/shitmodules
# Original module: https://github.com/kamolgks/Hikkamods/blob/main/FarmPA.py

# Name: AuroraFarm
# Author: kamolgks
# Commands:
# .chatid | .kynifarm
# scope: hikka_only
# meta developer: @AuroraModules


__version__ = (1, 0, 2)


import asyncio
import logging

from telethon.tl.types import Message

from .. import loader, utils

logging = logging.getLogger("AuroraFarm")


@loader.tds
class AuroraFarm(loader.Module):


    strings = {
        "name": "AuroraFarm",
        "group_id": "Group ID",
        "enable": "<b>AuroraFarm successfully launched</b>",
        "disable": "<b>AuroraFarm successfully stopped</b>",
        "loading": "<b>Loading...</b>",
        "id_error": (
            "<b>No group id for farming. Use: </b><code>.config AuroraFarm</code> <b>to"
            " enter group id.</b>"
        ),
    }

    strings_ru = {
        "group_id": "Айди группы",
        "enable": "<b>AuroraFarm успешно запущен</b>",
        "disable": "<b>AuroraFarm успешно остановлен</b>",
        "loading": "<b>Загрузка...</b>",
        "id_error": (
            "<b>Не указан айди группы для фарма. Используй: </b><code>.config"
            " AuroraFarm</code> <b>для ввода ийди группы.</b>"
        ),
    }

    strings_uz = {
        "group_id": "Guruh ID-si",
        "enable": "<b>AuroraFarm muvaffaqiyatli ishga tushirildi</b>",
        "disable": "<b>AuroraFarm muvaffaqiyatli to'xtatildi</b>",
        "loading": "<b>Yuklanmoqda...</b>",
        "id_error": (
            "<b>Dehqonchilik uchun guruh identifikatori yo'q. Guruh identifikatorini"
            " kiritish uchun </b><code>.config AuroraFarm</code> <b>dan foydalaning.</b>"
        ),
    }

    strings_de = {
        "group_id": "Gruppen-ID",
        "enable": "<b>AuroraFarm erfolgreich gestartet</b>",
        "disable": "<b>AuroraFarm erfolgreich deaktiviert</b>",
        "loading": "<b>Laden...</b>",
        "id_error": (
            "<b>Es gibt keine Gruppen-ID für die Landwirtschaft. Verwenden Sie"
            " </b><code>.config AuroraFarm</code> <b>, um eine Gruppen-ID einzugeben.</b>"
        ),
    }

    strings_es = {
        "group_id": "Identificación del grupo",
        "enable": "<b>AuroraFarm se inició correctamente</b>",
        "disable": "<b>AuroraFarm deshabilitado con éxito</b>",
        "loading": "<b>Cargando...</b>",
        "id_error": (
            "<b>No hay ID de grupo para la agricultura. Usa </b><code>.config"
            " AuroraFarm</code> <b> para ingresar una ID de grupo.</b>"
        ),
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "group_id",
                None,
                lambda: self.strings["group_id"],
            ),
        )

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    @loader.command(
        ru_doc="Включить/отключить режим автоматического фарма для бота Aurora.",
        uz_doc="Aurora boti uchun avtomatik dehqonchilik rejimini yoqadi/o‘chiradi.",
        de_doc="Aktiviert/deaktiviert den Auto-Farming-Modus für den Aurora-Bot.",
        es_doc="Habilita/deshabilita el modo de cultivo automático para el bot Aurora.",
    )
    async def kynifarm(self, message: Message):
        """
        Turns on/off automatic farming mode for the Aurora bot.
        """
        try:
            status = self.db.get("farm_status", "status")
            msg = await utils.answer(message, self.strings["loading"])
            text = "/kyni"
            group_id = self.config["group_id"]
            if not group_id:
                await msg.edit(self.strings["id_error"])
                return
            if status:
                self.db.set("farm_status", "status", False)
                await utils.answer(message, self.strings["disable"])
            else:
                self.db.set("farm_status", "status", True)
                await utils.answer(message, self.strings["enable"])
                while self.db.get("farm_status", "status"):
                    await message.client.send_message(int(group_id), text)
                    await asyncio.sleep(7500)
        except Exception as e:
            await utils.answer(
                message,
                (
                    f"Something went wrong..\nError: {e}\n\nIf the error persists,"
                    " Please write about the error to me in PM:"
                    " https://t.me/KorenbZla"
                ),
            )
            logging.info("An error has occurred")

    @loader.command(
        ru_doc="Команда .chatid показывает идентификатор чата.",
        uz_doc=".chatid buyrug'i suhbat identifikatorini ko'rsatadi.",
        de_doc="Der Befehl .chatid zeigt die Chat-ID an.",
        es_doc="El comando .chatid muestra la identificación del chat.",
    )

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
