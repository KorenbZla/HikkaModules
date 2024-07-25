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

# Name: Warpigs
# Author: dend1yya
# Commands: 
# .autogrow | .ungrow | .autofight | .unfight | .nameset
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/a37fb86b3a00c03dee661.jpg

from .. import loader, utils
import asyncio

class WarpigsMod(loader.Module):
    """Automates work with @warpigs_bot"""

    strings = {
        "name": "Warpigs",
        "pig_growth_on": "<emoji document_id=5316581501360420451>🐷</emoji> <b>Automatic pig growth: <i>Activated.</i></b>",
        "pig_growth_off": "<emoji document_id=5316581501360420451>🐷</emoji> <b>Automatic pig growth: <i>Deactivated.</i></b>",
        "pig_fights_on": "<emoji document_id=5316581501360420451>⚔️</emoji> <b>Automatic pig fights: <i>Activated.</i></b>",
        "pig_fights_off": "<emoji document_id=5316581501360420451>⚔️</emoji> <b>Automatic pig fights: <i>Deactivated.</i></b>",
        "no_name": "<emoji document_id=5778527486270770928>❌</emoji> <b>Specify a name for the pig.</b>",
        "name_set": "<emoji document_id=5774022692642492953>✅</emoji> <b>Your pig's name has been successfully changed!</b>",
        "new_name": "<emoji document_id=5316581501360420451>🐷</emoji> <b>New name</b>",
    }

    strings_ru = {
        "pig_growth_on": "<emoji document_id=5316581501360420451>🐷</emoji> <b>Автоматический рост свиней: <i>Включен.</i></b>",
        "pig_growth_off": "<emoji document_id=5316581501360420451>🐷</emoji> <b>Автоматический рост свиней: <i>Выключен.</i></b>",
        "pig_fights_on": "<emoji document_id=5316581501360420451>⚔️</emoji> <b>Автоматические свиные бои: <i>Включены.</i></b>",
        "pig_fights_off": "<emoji document_id=5316581501360420451>⚔️</emoji> <b>Автоматические свиные бои: <i>Выключены.</i></b>",
        "no_name": "<emoji document_id=5778527486270770928>❌</emoji> <b>Укажите имя для свиньи.</b>",
        "name_set": "<emoji document_id=5774022692642492953>✅</emoji> <b>Имя вашей свиньи успешно изменено!</b>",
        "new_name": "<emoji document_id=5316581501360420451>🐷</emoji> <b>Новое имя</b>",
    }

    strings_uz = {
        "pig_growth_on": "<emoji document_id=5316581501360420451>🐷</emoji> <b>Avtomatik cho'chqa o'sishi: <i>Yoqilgan.</i></b>",
        "pig_growth_off": "<emoji document_id=5316581501360420451>🐷</emoji> <b>Avtomatik cho'chqa o'sishi: <i>O'chirilgan.</i></b>",
        "pig_fights_on": "<emoji document_id=5316581501360420451>⚔️</emoji> <b>Avtomatik cho'chqa janglari: <i>Yoqilgan.</i></b>",
        "pig_fights_off": "<emoji document_id=5316581501360420451>⚔️</emoji> <b>Avtomatik cho'chqa janglari: <i>O'chirilgan.</i></b>",
        "no_name": "<emoji document_id=5778527486270770928>❌</emoji> <b>Cho'chqaga ism kiriting.</b>",
        "name_set": "<emoji document_id=5774022692642492953>✅</emoji> <b>Cho'chqangizning ismi muvaffaqiyatli o'zgartirildi!</b>",
        "new_name": "<emoji document_id=5316581501360420451>🐷</emoji> <b>Yangi ism</b>",
    }

    strings_de = {
        "pig_growth_on": "<emoji document_id=5316581501360420451>🐷</emoji> <b>Automatisches Schweinewachstum: <i>Aktiviert.</i></b>",
        "pig_growth_off": "<emoji document_id=5316581501360420451>🐷</emoji> <b>Automatisches Schweinewachstum: <i>Deaktiviert.</i></b>",
        "pig_fights_on": "<emoji document_id=5316581501360420451>⚔️</emoji> <b>Automatische Schweinekämpfe: <i>Aktiviert.</i></b>",
        "pig_fights_off": "<emoji document_id=5316581501360420451>⚔️</emoji> <b>Automatische Schweinekämpfe: <i>Deaktiviert.</i></b>",
        "no_name": "<emoji document_id=5778527486270770928>❌</emoji> <b>Geben Sie einen Namen für das Schwein an.</b>",
        "name_set": "<emoji document_id=5774022692642492953>✅</emoji> <b>Der Name Ihres Schweins wurde erfolgreich geändert!</b>",
        "new_name": "<emoji document_id=5316581501360420451>🐷</emoji> <b>Neuer Name</b>",
    }

    strings_es = {
        "pig_growth_on": "<emoji document_id=5316581501360420451>🐷</emoji> <b>Crecimiento automático de cerdos: <i>Activado.</i></b>",
        "pig_growth_off": "<emoji document_id=5316581501360420451>🐷</emoji> <b>Crecimiento automático de cerdos: <i>Desactivado.</i></b>",
        "pig_fights_on": "<emoji document_id=5316581501360420451>⚔️</emoji> <b>Combates automáticos de cerdos: <i>Activado.</i></b>",
        "pig_fights_off": "<emoji document_id=5316581501360420451>⚔️</emoji> <b>Combates automáticos de cerdos: <i>Desactivado.</i></b>",
        "no_name": "<emoji document_id=5778527486270770928>❌</emoji> <b>Especifica un nombre para el cerdo.</b>",
        "name_set": "<emoji document_id=5774022692642492953>✅</emoji> <b>¡El nombre de tu cerdo ha sido cambiado exitosamente!</b>",
        "new_name": "<emoji document_id=5316581501360420451>🐷</emoji> <b>Nuevo nombre</b>",
    }

    @loader.command(
        ru_doc="Автоматический рост свиньи.",
        uz_doc="Avtomatik cho'chqa o'sishi.",
        de_doc="Automatisches Schweinewachstum.",
        es_doc="Crecimiento automático de cerdos.",
    )
    async def autogrow(self, message):
        """Automatic pig growth"""
        await message.edit(self.strings("pig_growth_on"))
        self.set("grow", True)
        while self.get("grow"):
            await message.reply("/grow")
            await asyncio.sleep(86400)

    @loader.command(
        ru_doc="Отключить автоматический рост.",
        uz_doc="Avtomatik o'sishni o'chirish.",
        de_doc="Automatisches Wachstum deaktivieren.",
        es_doc="Desactivar el crecimiento automático.",
    )
    async def ungrow(self,message):
        """Disable automatic growth."""
        self.set("grow", False)
        await utils.answer(message, self.strings("pig_growth_off"))

    @loader.command(
        ru_doc="Включить автоматические бои свиней.",
        uz_doc="Avtomatik cho'chqa janglarini yoqish.",
        de_doc="Automatische Schweinekämpfe aktivieren.",
        es_doc="Habilitar peleas automáticas de cerdos.",
    )
    async def autofight(self,message):
        """Enable automatic pig fights"""
        await message.edit(self.strings("pig_fights_on"))
        self.set("fight", True)
        while self.get("fight"):
            await message.reply("/fight")
            await asyncio.sleep(86400)

    @loader.command(
        ru_doc="Отключить автоматические бои свиней.",
        uz_doc="Avtomatik cho'chqa janglarini o'chirish.",
        de_doc="Automatische Schweinekämpfe deaktivieren.",
        es_doc="Deshabilitar peleas automáticas de cerdos.",
    )
    async def unfight(self,message):
        """Disable automatic pig fights"""
        self.set("fight",False)
        await utils.answer(message, self.strings("pig_fights_off"))

    @loader.command(
        ru_doc="[name] - Установить имя вашей свиньи.",
        uz_doc="[name] - Cho'chqangizning nomini o'rnatadi.",
        de_doc="[name] - Setze den Namen deines Schweins.",
        es_doc="[name] - Establece el nombre de tu cerdo.",
    )
    async def nameset(self,message):
        """[name] - Set the name of your pig"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no_name"))
            return
        
        name_set = self.strings("name_set")
        new_name = self.strings("new_name")
        await message.respond(f"/name {args}")
        await message.edit(f"{name_set}\n{new_name}: <code>{args}</code>")
