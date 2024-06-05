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
# .autogrow | .farmstop
# scope: hikka_only
# meta developer: @AuroraModules

from .. import loader, utils
import asyncio

class WarpigsMod(loader.Module):
    """Автоматизирует работу с Warpigs Bot"""

    strings = {"name": "Warpigs"}

    async def autogrowcmd(self, message):
        """Автоматическое выращивание свинки."""
        await message.edit("<b> 🐷 Автоматическое выращивание свинки включено.</b>")
        self.set("grow", True)
        while self.get("grow"):
            await message.reply("/grow")
            await asyncio.sleep(86400)

    async def ungrowcmd(self,message):
        """Отключает автоматическое выращивание."""
        self.set("grow", False)
        await utils.answer(message, "<b> 🐷 Автоматическое выращивание свинки выключено.</b>")

    async def autofightcmd(self,message):
        """Автоматическое выставление свинки на бой."""
        await message.edit("<b>⚔️ Автоматическое выставление свинки на бой включено.</b>")
        self.set("fight", True)
        while self.get("fight"):
            await message.reply("/fight")
            await asyncio.sleep(86400)

    async def unfightcmd(self,message):
        """Отключает автоматическое выставление свинки на бой."""
        self.set("fight",False)
        await utils.answer(message, "<b> ⚔️ Автоматическое выставление свинки на бой выключена.</b>")

    async def namesetcmd(self,message):
        """Устанавливает имя вашей свинки."""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "<code> ❌ Укажите имя для свинки!\n nameset 'имя вашей свинки'</code>")
            return
        
        await message.respond(f"/name {args}")
        await message.edit(f"<b> ✅ Имя вашей свинки успешно изменено!\n<b>🐷 Новое имя:</b> <code>{args}</code>")
