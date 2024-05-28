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
# * 🔒 Code is licensed under CC-BY-NC-ND 4.0 unless otherwise specified.
# * 🌐 https://creativecommons.org/licenses/by-nc-nd/4.0/
# * ⛔️ You CANNOT edit this file without direct permission from the author.
# * ⛔️ You can redistribute this file without any changes.

# Name: RandomAvatars
# Author: Felix?
# Commands:
# .rpavatars
# scope: hikka_only
# meta developer: @AuroraModules

__version__ = (1, 2, 1)

from .. import loader, utils
import os

@loader.tds
class RandomAvatars(loader.Module):

    strings = {
        "name": "RandomAvatars",
        "loading_avatars": "<emoji document_id=5215327832040811010>⏳</emoji> <b>loading the avatars</b>",
        "error_loading": "<b>Failed to get avatars. Please check the PM with the bot @anime_4bot</b>",
    }

    strings_ru = {
        "loading_avatars": "<emoji document_id=5215327832040811010>⏳</emoji> <b>загрузка аватарок</b>",
        "error_loading": "<b>Не удалось получить аватарки. Пожалуйста проверьте ЛС с ботом @anime_4bot</b>",
    }

    strings_uz = {
        "loading_avatars": "<emoji document_id=5215327832040811010>⏳</emoji> <b>avatarlarni yuklash</b>",
        "error_loading": "<b>Avatarlar olinmadi. Iltimos, PMni @anime_4bot boti bilan tekshiring</b>",
    }

    strings_de= {
        "loading_avatars": "<emoji document_id=5215327832040811010>⏳</emoji> <b>Laden der Avatare</b>",
        "error_loading": "<b>Avatare konnten nicht abgerufen werden. Bitte überprüfen Sie die PM mit dem Bot @anime_4bot</b>",
    }

    strings_es = {
        "loading_avatars": "<emoji document_id=5215327832040811010>⏳</emoji> <b>cargando los avatares</b>",
        "error_loading": "<b>No se pudieron obtener avatares. Por favor revisa el MP con el bot @anime_4bot</b>",
    }

    @loader.command(
        ru_doc="Поиск случайных парных аватарок",
        uz_doc="Tasodifiy juftlashtirilgan avatarlarni qidiring",
        de_doc="Suchen Sie nach zufällig gepaarten Avataren",
        es_doc="Buscar avatares emparejados aleatoriamente",
    )
    async def rpavatarscmd(self, message):
        """random paired avatars"""
        await utils.answer(message, (self.strings["loading_avatars"]))
        async with self._client.conversation("@anime_4bot") as conv:
            await conv.send_message("🎎 Парные аватарки")
        
            response1 = await conv.get_response()
          
            if response1.photo:
                media1 = await self._client.download_media(response1.photo, "avatars")
            
                response2 = await conv.get_response()
            
                if response2.photo:
                    media2 = await self._client.download_media(response2.photo, "avatars")
                
                    # Отправляем файлы как сообщения
                    await message.client.send_message(
                        message.peer_id,
                        file=media1,
                    )
                    await message.client.send_message(
                        message.peer_id,
                        file=media2,
                    )    
                
                    # Удаляем временные файлы
                    os.remove(media1)
                    os.remove(media2)
                
                    await message.delete()

