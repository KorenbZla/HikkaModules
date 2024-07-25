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

# Name: Deanon
# Author: Felix?
# Commands:
# .deanon
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/9bf5a040f3fcab0caf689.jpg

__version__ = (1, 0, 0)

from telethon.tl.types import Message # type: ignore
from .. import loader

@loader.tds
class Deanon(loader.Module):

    strings = {
        "name": "Deanon",
        "try_d1": "<b><i>You can't do that. An Internet hero.</i></b>",
        "try_d2": "<b><i>Once again, I will delete the account for such jokes.</i></b>",
    }

    strings_ru = {
        "try_d1": "<b><i>Нельзя таким заниматься. Интернет - герой.</i></b>",
        "try_d2": "<b><i>Еще раз и удалю аккаунт за такие приколы.</i></b>",
    }
    strings_uz = {
        "try_d1": "<b><i>Siz buni qila olmaysiz. Internet qahramoni.</i></b>",
        "try_d2": "<b><i>Bunday hazillar uchun yana bir bor o'z akkauntimni o'chirib tashlayman.</i></b>",
    }
    strings_de = {
        "try_d1": "<b><i>Das kannst du nicht machen. Internetheld.</i></b>",
        "try_d2": "<b><i>Noch einmal werde ich meinen Account für solche Witze löschen.</i></b>",
    }
    strings_es = {
        "try_d1": "<b><i>No puedes hacer eso. Héroe de Internet.</i></b>",
        "try_d2": "<b><i>Una vez más eliminaré mi cuenta por este tipo de bromas.</i></b>",
    }

    @loader.command(
        ru_doc="Поиск по @UserName/Number/Email",
        uz_doc="Qidiruv @UserName/Number/Email",
        de_doc="Suche nach @UserName/Number/Email",
        es_doc="Buscar por @UserName/Number/Email",
    )
    async def deanon(self, message: Message):
        """Search by @UserName/Number/Email"""
        await message.delete()
        if not hasattr(self, "flag"):
            self.flag = 1
        else:
            self.flag += 1

        if self.flag <= 1:
            await self.client.send_message(message.peer_id, self.strings["try_d1"])
        else:
            await self.client.send_message(message.peer_id, self.strings["try_d2"])
