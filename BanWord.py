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

# Name: BanWord
# Author: dend1yya
# Commands:
# .bwadd | .bword | .bwlist | .bwordoff | .bwon | .bwdel | .bwoff
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/926b74bc3235fb03433ea.jpg

version = (1, 0, 0)

from .. import loader, utils
from datetime import timedelta

@loader.tds
class BanWordMod(loader.Module):
    """Модуль для управления запрещёнными словами в чате."""
    
    strings = {
        "name": "BanWord",
        "word_added": "<b><emoji document_id=5873153278023307367>📄</emoji> Banword successfully added:</b> <code>{}</code>",
        "kick": "<b><emoji document_id=5442879640379076105>👤</emoji> | User @{message.sender.username} used a banned word and was kicked. <emoji document_id=5253780051471642059>🛡</emoji>\n<i><emoji document_id=5231165412275668380>🥰</emoji> | Protected by AuroraModules</i>",
        "mute": "<b><emoji document_id=5442879640379076105>👤</emoji> | User @{message.sender.username} used a banned word and was muted for 1 hour. <emoji document_id=5253780051471642059>🛡</emoji></b>\n<i><emoji document_id=5231165412275668380>🥰</emoji> | Protected by AuroraModules</i>",
        "word_removed": "<b><emoji document_id=5445267414562389170>🗑</emoji> Banned word removed:</b> <code>{}</code>",
        "none_bw": "<b><emoji document_id=5287613115180006030>🤬</emoji> The list of prohibited words is empty.</b>",
        "bword_enabled": "<b><emoji document_id=5398001711786762757>✅</emoji> Banned words are included in this chat</b>",
        "bword_disabled": "<b><emoji document_id=5388785832956016892>❌</emoji> Prohibited words are disabled.</b>",
        "action_set": "<b><emoji document_id=5255999175174137421>🛡</emoji> Action set:</b> <code>{}</code>",
        "no_action": "<b><emoji document_id=5980953710157632545>❌</emoji> Action not specified. Use: kick, mute, delete</b>",
        "no_word": "<b><emoji document_id=5443038326535759644>💬</emoji> Word not specified</b>"
    }

    strings_ru = {
        "word_added": "<b><emoji document_id=5873153278023307367>📄</emoji> Запрещённое слово добавлено:</b> <code>{}</code>",
        "kick": "<b><emoji document_id=5442879640379076105>👤</emoji> | Пользователь @{message.sender.username} использовал запрещённое слово и был кикнут. <emoji document_id=5253780051471642059>🛡</emoji>\n<i><emoji document_id=5231165412275668380>🥰</emoji> | Protected by AuroraModules</i>",
        "mute": "<b><emoji document_id=5442879640379076105>👤</emoji> | Пользователь @{message.sender.username} использовал запрещённое слово и был замучен на 1 час. <emoji document_id=5253780051471642059>🛡</emoji></b>\n<i><emoji document_id=5231165412275668380>🥰</emoji> | Protected by AuroraModules</i>",
        "word_removed": "<b><emoji document_id=5445267414562389170>🗑</emoji> Запрещённое слово удалено:</b> <code>{}</code>",
        "none_bw": "<b><emoji document_id=5287613115180006030>🤬</emoji> Список запрещённых слов пуст.</b>",
        "bword_enabled": "<b><emoji document_id=5398001711786762757>✅</emoji> Банворды включены в этом чате.</b>",
        "bword_disabled": "<b><emoji document_id=5388785832956016892>❌</emoji> Банворды выключены в этом чате.</b>",
        "action_set": "<b><emoji document_id=5255999175174137421>🛡</emoji> Действие установлено:</b> <code>{}</code>",
        "no_action": "<b><emoji document_id=5980953710157632545>❌</emoji> Действие не указано. Используйте: kick, mute, delete.</b>",
        "no_word": "<b><emoji document_id=5443038326535759644>💬</emoji> Слово не указано.</b>",
    }

    strings_uz = {
        "word_added": "<b><emoji document_id=5873153278023307367>📄</emoji> Taqiqlangan so'z qo'shildi:</b> <code>{}</code>",
        "kick": "<b><emoji document_id=5442879640379076105>👤</emoji> | Foydalanuvchi @{message.sender.username} taqiqlangan soʻzni ishlatgan va haydalgan. <emoji document_id=5253780051471642059>🛡</emoji>\n<i><emoji document_id=5231165412275668380>🥰</emoji> | Protected by AuroraModules</i>",
        "mute": "<b><emoji document_id=5442879640379076105>👤</emoji> | Foydalanuvchi @{message.sender.username} taqiqlangan soʻzni ishlatgan va 1 soatga o'chirilgan. <emoji document_id=5253780051471642059>🛡</emoji></b>\n<i><emoji document_id=5231165412275668380>🥰</emoji> | Protected by AuroraModules</i>",
        "word_removed": "<b><emoji document_id=5445267414562389170>🗑</emoji> Taqiqlangan soʻz olib tashlandi:</b> <code>{}</code>",
        "bword_enabled": "<b><emoji document_id=5398001711786762757>✅</emoji> Bu chatda banwords yoqilgan.</b>",
        "bw_none": "<b><emoji document_id=5287613115180006030>🤬</emoji> Taqiqlangan so'zlar ro'yxati bo'sh.</b>",
        "bword_disabled": "<b><emoji document_id=5388785832956016892>❌</emoji> Banwords o'chirilgan.</b>",
        "action_set": "<b><emoji document_id=5255999175174137421>🛡</emoji> Harakat muvaffaqiyatli o'rnatildi:</b> <code>{}</code>",
        "no_action": "<b><emoji document_id=5980953710157632545>❌</emoji> Harakat belgilanmagan, foydalaning: kick, mute, delete</b>",
        "no_word": "<b><emoji document_id=5443038326535759644>💬</emoji> So'z belgilanmagan</b>",
    }

    strings_de = {
        "word_added": "<b><emoji document_id=5873153278023307367>📄</emoji> Verbotenes Wort hinzugefügt:</b> <code>{}</code>",
        "kick": "<b><emoji document_id=5442879640379076105>👤</emoji> | Benutzer @{message.sender.username} hat ein verbotenes Wort verwendet und wurde rausgeworfen. <emoji document_id=5253780051471642059>🛡</emoji>\n<i><emoji document_id=5231165412275668380>🥰</emoji> | Protected by AuroraModules</i>",
        "mute": "<b><emoji document_id=5442879640379076105>👤</emoji> | Benutzer @{message.sender.username} hat ein verbotenes Wort verwendet und wurde für 1 Stunde stummgeschaltet. <emoji document_id=5253780051471642059>🛡</emoji></b>\n<i><emoji document_id=5231165412275668380>🥰</emoji> | Protected by AuroraModules</i>",
        "word_removed": "<b><emoji document_id=5445267414562389170>🗑</emoji> Verbotenes Wort entfernt:</b> <code>{}</code>",
        "bw_none": "<b><emoji document_id=5287613115180006030>🤬</emoji> Die Liste der verbotenen Wörter ist leer.</b>",
        "bword_enabled": "<b><emoji document_id=5398001711786762757>✅</emoji> Banwords sind in diesem Chat aktiviert.</b>",
        "bword_disabled": "<b><emoji document_id=5388785832956016892>❌</emoji> Banwords sind in diesem Chat deaktiviert.</b>",
        "action_set": "<b><emoji document_id=5255999175174137421>🛡</emoji> Aktion erfolgreich festgelegt:</b> <code>{}</code>",
        "no_action": "<b><emoji document_id=5980953710157632545>❌</emoji> Aktion nicht angegeben, verwenden: kick, mute, delete</b>",
        "no_word": "<b><emoji document_id=5443038326535759644>💬</emoji> Das Wort ist nicht angegeben.</b>"
    }

    strings_es = {
        "word_added": "<b><emoji document_id=5873153278023307367>📄</emoji> Palabra prohibida añadida con éxito:</b> <code>{}</code>",
        "kick": "<b><emoji document_id=5442879640379076105>👤</emoji> | El usuario @{message.sender.username} utilizó una palabra prohibida y fue expulsado. <emoji document_id=5253780051471642059>🛡</emoji>\n<i><emoji document_id=5231165412275668380>🥰</emoji> | Protegido por AuroraModules</i>",
        "mute": "<b><emoji document_id=5442879640379076105>👤</emoji> | El usuario @{message.sender.username} utilizó una palabra prohibida y fue silenciado por 1 hora. <emoji document_id=5253780051471642059>🛡</emoji></b>\n<i><emoji document_id=5231165412275668380>🥰</emoji> | Protegido por AuroraModules</i>",
        "word_removed": "<b><emoji document_id=5445267414562389170>🗑</emoji> Palabra prohibida eliminada:</b> <code>{}</code>",
        "none_bw": "<b><emoji document_id=5287613115180006030>🤬</emoji> La lista de palabras prohibidas está vacía.</b>",
        "bword_enabled": "<b><emoji document_id=5398001711786762757>✅</emoji> Las palabras prohibidas están activadas en este chat</b>",
        "bword_disabled": "<b><emoji document_id=5388785832956016892>❌</emoji> Las palabras prohibidas están desactivadas.</b>",
        "action_set": "<b><emoji document_id=5255999175174137421>🛡</emoji> Acción configurada:</b> <code>{}</code>",
        "no_action": "<b><emoji document_id=5980953710157632545>❌</emoji> Acción no especificada. Usa: kick, mute, delete</b>",
        "no_word": "<b><emoji document_id=5443038326535759644>💬</emoji> Palabra no especificada</b>"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "BAN_ACTION",
                "delete",
                lambda: "Action when finding a forbidden word: kick, mute, delete",
            ),
        )

    async def watcher(self, message):
        chat_id = utils.get_chat_id(message)
        enabled_chats = self.db.get("BanWord", "enabled_chats", [])
        if str(chat_id) not in enabled_chats:
            return

        banned_words = self.db.get("BanWord", "banned_words", [])
        if any(word in message.text for word in banned_words):
            action = self.config["BAN_ACTION"]
            if action == "delete":
                await message.delete()
            elif action == "kick":
                entity = await message.client.get_input_entity(chat_id)
                await message.client.kick_participant(entity, message.sender_id)
                await message.respond(f"<b><emoji document_id=5442879640379076105>👤</emoji> | User @{message.sender.username} used a banned word and was kicked. <emoji document_id=5253780051471642059>🛡</emoji></b>\n<i><emoji document_id=5231165412275668380>🥰</emoji></i>\n<b><i>Protected by @AuroraModules</b></i>")
            elif action == "mute":
                mute_duration = timedelta(hours=1)
                until_date = message.date + mute_duration
                entity = await message.client.get_input_entity(chat_id)
                await message.client.edit_permissions(
                    entity, 
                    message.sender_id, 
                    until_date=until_date, 
                    send_messages=False
                )
                await message.respond(f"<b><emoji document_id=5442879640379076105>👤</emoji> | User @{message.sender.username} used a banned word and was muted for 1 hour. <emoji document_id=5253780051471642059>🛡</emoji></b>\n<i><emoji document_id=5231165412275668380>🥰</emoji></i>\n<b><i>Protected by @AuroraModules</b></i>")

    @loader.command(
        ru_doc = "Добавляет запрещённое слово.",
        uz_doc = "Taqiqlangan so'zni qo'shadi.",
        de_doc = "Fügt ein verbotenes Wort hinzu.",
        es_doc = "Añade una palabra prohibida.",
    )
    async def bwadd(self, message):
        """Adds a banned word."""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings["no_word"])
            return
        banned_words = self.db.get("BanWord", "banned_words", [])
        if args not in banned_words:
            banned_words.append(args)
            self.db.set("BanWord", "banned_words", banned_words)
            await utils.answer(message, self.strings["word_added"].format(args))
    
    @loader.command(
        ru_doc = "Удаляет запрещённое слово.",
        uz_doc = "Taqiqlangan so'zni olib tashlaydi.",
        de_doc = "Entfernt ein verbotenes Wort.",
        es_doc = "Elimina una palabra prohibida.",
    )
    async def bwdel(self, message):
        """Removes a banned word."""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings["no_word"])
            return
        banned_words = self.db.get("BanWord", "banned_words", [])
        if args in banned_words:
            banned_words.remove(args)
            self.db.set("BanWord", "banned_words", banned_words)
            await utils.answer(message, self.strings["word_removed"].format(args))

    @loader.command(
        ru_doc = "Включает банворды в чате.",
        uz_doc = "Chatda banwordsni yoqadi.",
        de_doc = "Aktiviert Banwords im Chat.",
        es_doc = "Activa las palabras prohibidas en el chat.",
    )
    async def bwon(self, message):
        """Enables banwords in chat."""
        chat_id = str(utils.get_chat_id(message))
        enabled_chats = self.db.get("BanWord", "enabled_chats", [])
        if chat_id not in enabled_chats:
            enabled_chats.append(chat_id)
            self.db.set("BanWord", "enabled_chats", enabled_chats)
            await utils.answer(message, self.strings["bword_enabled"])

    @loader.command(
        ru_doc = "Отключает банворды в чате.",
        uz_doc = "Chatdagi bandwordlarni o'chirib qo'yadi.",
        de_doc = "Deaktiviert Ban Words im Chat.",
        es_doc = "Desactiva las palabras prohibidas en el chat.",
    )
    async def bwoff(self, message):
        """Disable banword in chat."""
        chat_id = str(utils.get_chat_id(message))
        enabled_chats = self.db.get("BanWord", "enabled_chats", [])
        if chat_id in enabled_chats:
            enabled_chats.remove(chat_id)
            self.db.set("BanWord", "enabled_chats", enabled_chats)
            await utils.answer(message, self.strings["bword_disabled"])

    @loader.command(
        ru_doc = "Устанавливает действие при нахождении запрещённого слова (kick, mute, delete).",
        uz_doc = "Taqiqlangan so'z aniqlanganda harakatni o'rnatadi (kick, mute, delete).",
        de_doc = "Legt die Aktion fest, wenn ein verbotenes Wort gefunden wird (kick, mute, delete).",
        es_doc = "Establece la acción cuando se encuentra una palabra prohibida (expulsar, silenciar, eliminar).",
    )
    async def bword(self, message):
        """Sets the action when a prohibited word is found (kick, mute, delete)."""
        args = utils.get_args_raw(message)
        if args not in ["kick", "mute", "delete"]:
            await utils.answer(message, self.strings["no_action"])
            return
        self.config["BAN_ACTION"] = args
        await utils.answer(message, self.strings["action_set"].format(args))

    @loader.command(
        ru_doc = "Выводит список запрещённых слов.",
        uz_doc = "Taqiqlangan so'zlar ro'yxatini ko'rsatadi.",
        de_doc = "Zeigt eine Liste verbotener Wörter an.",
        es_doc = "Muestra una lista de palabras prohibidas.",
    )
    async def bwlist(self, message):
        """Displays a list of prohibited words."""
        banned_words = self.db.get("BanWord", "banned_words", [])
        if not banned_words:
            await utils.answer(message, self.strings["none_bw"])
            return

        word_list = "\n".join(f"• {word}" for word in banned_words)
        await utils.answer(message, f"<b><emoji document_id=5870984130560266604>💬</emoji> Banned Words:</b>\n<i>{word_list}</i>")
