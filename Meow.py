# Name: Meow
# Author: Felix? 
# Commands:
# .meow | .stopmeow
# scope: hikka_only
# meta developer: @AuroraModules


version = (1, 0, 0)


from .. import loader, utils
import asyncio

@loader.tds
class MeowMod(loader.Module):
    """Мяуканье на всех языках"""
    strings = {"name": "Meow"}

    async def meowcmd(self, message):
        """Начать мяукать на всех языках"""
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
              ]
        self.playing_meow = True
        for line in lyrics:
            await asyncio.sleep(2)
            await utils.answer(message, line)
            if not self.playing_meow:
              break
        self.playing_meow = False

    async def stopmeowcmd(self, message):
        """Остановить МЯУ"""
        if self.playing_meow:
            self.playing_meow = False 
            await utils.answer(message, "🎧<b>Воспроизведение мяуканье остановлено.</b>")
        else:
            await utils.answer(message, "❌<b>В данный момент мяуканье не воспроизводится.</b>")
        