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

# Name: Meow
# Author: Felix? 
# Commands:
# .meow | .stopmeow
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/21c1c48baffc8c6236c0f.jpg

version = (1, 0, 1)

from .. import loader, utils
import asyncio

@loader.tds
class MeowMod(loader.Module):
    """Start meowing in different languages"""

    strings = {
        "name": "Meow",
        "stopmeow": "<emoji document_id=5172447776205702031>🎵</emoji><b>You've stopped meowing.</b>",
        "not_meow": "<emoji document_id=5084923566848213749>🐾</emoji><b>You are not meowing at the moment.</b>",
    }

    strings_ru = {
        "stopmeow": "<emoji document_id=5172447776205702031>🎵</emoji><b>Ты перестал мяукать.</b>",
        "not_meow": "<emoji document_id=5084923566848213749>🐾</emoji><b>Ты сейчас не мяукаешь.</b>",
    }

    strings_uz = {
        "stopmeow": "<emoji document_id=5172447776205702031>🎵</emoji><b>Sen miyolishni to'xtadingiz.</b>",
        "not_meow": "<emoji document_id=5084923566848213749>🐾</emoji><b>Siz hozir miyolmaysiz.</b>",
    }

    strings_de = {
        "stopmeow": "<emoji document_id=5172447776205702031>🎵</emoji><b>Du hast aufgehört zu miauen.</b>",
        "not_meow": "<emoji document_id=5084923566848213749>🐾</emoji><b>Du miaust gerade nicht.</b>",
    }

    strings_es = {
        "stopmeow": "<emoji document_id=5172447776205702031>🎵</emoji><b>Has dejado de maullar.</b>",
        "not_meow": "<emoji document_id=5084923566848213749>🐾</emoji><b>No estás maullando en este momento.</b>",
    }

    @loader.command(
        ru_doc="Начать мяукать на разных языках",
        uz_doc="Turli tillarda miyovlashni boshlang",
        de_doc="Fangen Sie an, auf verschiedenen Sprachen zu miauen",
        es_doc="Comience a maullar en diferentes idiomas",
    )
    async def meow(self, message):
        """Start meowing in different languages"""
        lyrics = [
              "Мяу",
              "Meow",
              "Miaou",
              "Miau",
              "Miao",
              "야옹",
              "Miauczeć",
              "miyav",
              "Мяу",
              "maullar",
              "Мјау",
              "مواء",
              "myau",
              "Мияу",
              "Мөө",
              "喵喵",
              "Niau",
              "म्याऊं",
              "မကွာ",
              "নিঃ",
              "กิน",
              "მაიო",
              "म्याँऊँ",
              "ມີອູດ",
              "မြှောက်",
              "මීයා",
              "מיאו",
              "մյուռ",
              "میاو",
              "म्याऊं",
              "ಮ್ಯಾವ್",
              "មែយវ៉េ",
              "മിയാവ്",
              "мйаоу",
              "მიაუ",
              "میاو",
              "میائو",
              "เหมียว",
              "မြကွေး",
              ]
        self.playing_meow = True
        for line in lyrics:
            await asyncio.sleep(2)
            await utils.answer(message, line)
            if not self.playing_meow:
              break
        self.playing_meow = False

    @loader.command(
        ru_doc="Остановить мяуканье на разных языках",
        uz_doc="Turli tillarda miyovlashni to'xtatish",
        de_doc="Hören Sie auf, auf verschiedenen Sprachen zu miauen",
        es_doc="Detener el maullido en diferentes idiomas",
    )
    async def stopmeow(self, message):
        """Stop meowing in different languages"""
        if self.playing_meow:
            self.playing_meow = False 
            await utils.answer(message, self.strings["stopmeow"])
        else:
            await utils.answer(message, self.strings["not_meow"])
        
