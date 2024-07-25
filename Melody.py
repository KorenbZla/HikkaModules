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

# Name: Melody
# Author: Felix? | dend1y
# Commands:
# .заденьгида | .LIPSIHA | .stopplay
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/787faf75b8a094553336f.jpg

version = (1, 2, 2)

from .. import loader, utils
import asyncio

@loader.tds
class MelodyMod(loader.Module):
    """Module for playing various songs in a chat"""

    strings = {
        "name": "Melody",
        "playing_music_off": "<emoji document_id=5172447776205702031>🎵</emoji><b>Music playback has been stopped.</b>",
        "not_play": "<emoji document_id=4918014360267260850>⛔️</emoji><b>The music is not playing at the moment.</b>",
    }

    strings_ru = {
        "playing_music_off": "<emoji document_id=5172447776205702031>🎵</emoji><b>Воспроизведение музыки остановлено.</b>",
        "not_play": "<emoji document_id=4918014360267260850>⛔️</emoji><b>В данный момент музыка не воспроизводится.</b>",
    }

    strings_uz = {
        "playing_music_off": "<emoji document_id=5172447776205702031>🎵</emoji><b>Musiqani to'xtatish.</b>",
        "not_play": "<emoji document_id=4918014360267260850>⛔️</emoji><b>Hozircha musiqa ijro etilmayapti.</b>",
    }

    strings_de = {
        "playing_music_off": "<emoji document_id=5172447776205702031>🎵</emoji><b>Die Musikwiedergabe wurde gestoppt.</b>",
        "not_play": "<emoji document_id=4918014360267260850>⛔️</emoji><b>Die Musik wird derzeit nicht abgespielt.</b>",
    }

    strings_es = {
        "playing_music_off": "<emoji document_id=5172447776205702031>🎵</emoji><b>La reproducción de música ha sido detenida.</b>",
        "not_play": "<emoji document_id=4918014360267260850>⛔️</emoji><b>En este momento no se está reproduciendo música.</b>",
    }


    @loader.command(
        ru_doc="Включить песню «За деньги да»",
        uz_doc="Qo'shiq ijro eting «За деньги да»",
        de_doc="Lied abspielen «За деньги да»",
        es_doc="Reproducir canción «За деньги да»",
    )
    async def заденьгида(self, message):
        """Play song «За деньги да»"""
        lyrics = [
              "Я вообще делаю что хочу",
              "Хочу импланты — звоню врачу",
              "Кто меня не любит — я вас не слышу",
              "Вы просто мне завидуете, я молчу",
              "Я не продаюсь, но за деньги — да",
              "Мой продюссер говорит я поп-звезда",
              "И кстати, мой продюссер — это мой муж, да",
              "Я не скажу в ответ ничего на вид",
              "И не скажу «привет» если бабок нет",
              "Слышу любимый звук — это звон монет",
              "Они тянут все мне руку, это мой концерт",
              "Не завожу подруг, но за деньги — да",
              "Я подумаю потом, но скажу сразу «да»",
              "За деньги, да, за деньги, да",
              "За деньги, да",
              "Деньги— Деньги— Деньги— Деньги— Да— Да— Да— Да—",
              "Играла песня «За деньги да»",
              ]
        self.playing_music = True
        for line in lyrics:
            await asyncio.sleep(3)
            await utils.answer(message, line)
            if not self.playing_music:
              break
        self.playing_music = False

    @loader.command(
        ru_doc="Включить песню «LIPSI HA»",
        uz_doc="Qo'shiq ijro eting «LIPSI HA»",
        de_doc="Lied abspielen «LIPSI HA»",
        es_doc="Reproducir canción «LIPSI HA»",
    )
    async def LIPSIHA(self, message):
        """Play song «LIPSI HA»"""
        lyrics = [
              "Деньги пахнут pussy, а",
              "Сумка Birkin, только нал",
              "Стринги, а, стринги, а",
              "В стрингах ношу капитал",
              "Juicy пахнет money, ха",
              "Сучки в Juicy мои, ха",
              "Lipsi, ха, lipsi, ха",
              "Lipsi give me money, ха",
              "Mommy на dollar",
              "Жопа на сайте, cash",
              "Я на работе",
              "Трясу огромной ass",
              "Дайте мне money",
              "Money на money, мой Ken",
              "Пахну деньгами",
              "Пахну деньгами",
              "AMA bad bitch",
              "Lipsi give me money, ха",
              "AMA hot bitch",
              "В стрингах ношу капитал",
              "Bad, bad bitch",
              "Juicy пахнет money, ха",
              "Где мои money, bitch?",
              "Где мои money?",
              "AMA bad bitch",
              "Lipsi give me money, ха",
              "AMA hot bitch",
              "В стрингах ношу капитал",
              "Bad, bad bitch" 
              "Juicy пахнет money, ха",
              "Где мои money, bitch?",
              "Где мои money?",
              "Песня «LIPSI HA»"
              ]
        self.playing_music = True
        for line in lyrics:
            await asyncio.sleep(3)
            await utils.answer(message, line)
            if not self.playing_music:
                break
        self.playing_music = False

    @loader.command(
        ru_doc="Остановить проигрывание музыки",
        uz_doc="Musiqani to'xtatish",
        de_doc="Wiedergabe von Musik stoppen",
        es_doc="Detener la reproducción de música",
    )
    async def stopplay(self, message):
        """Stop playing music"""
        if self.playing_music:
            self.playing_music = False 
            await utils.answer(message, self.strings["playing_music_off"])
        else:
            await utils.answer(message, self.strings["not_play"])
        
