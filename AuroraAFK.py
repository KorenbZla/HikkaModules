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

# Name: AuroraAFK
# Author: dend1yy | Felix?
# Commands:
# .afk | .removestatus | .setstatus | .unafk
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/f35de08579b3bd2235bc4.jpg

__version__ = (1, 0, 3)

import datetime
import logging
import time
from telethon import types, functions  # type: ignore
from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class AuroraAFKMod(loader.Module):
    """Your personal assistant to while you are in AFK mode"""

    strings = {
        "name": "AuroraAFK",
        "gone": "<b><emoji document_id=5287692511945437157>✅</emoji> You have successfully entered AFK mode!</b>",
        "back": "<b><emoji document_id=5287692511945437157>✅</emoji> You have successfully exited AFK mode!</b>",
        "afk": "<b><emoji document_id=5287613458777387650>😴</emoji> I'm currently in AFK\n<emoji document_id=5287737368583876982>🌀</emoji> Was online <code>{}</code> ago</b>",
        "afk_reason": "<b><emoji document_id=5287613458777387650>😴</emoji> I'm currently in AFK\n<emoji document_id=5287737368583876982>🌀</emoji> Was online <code>{}</code> ago\n<emoji document_id=5445161912985724546>✏️</emoji> Reason: <i>{}</i></b>",
        "status_added": "<b><emoji document_id=5285372392086976148>🦋</emoji> Status successfully set!</b>",
        "status_removed": "<b><emoji document_id=5879896690210639947>🗑</emoji> Status successfully removed!</b>",
        "no_user": "<b><emoji document_id=5287611315588707430>❌</emoji> Failed to get user information.</b>",
        "no_previous_status": "<b><emoji document_id=5287740598399285194>😵‍💫</emoji> Previous nickname not found.</b>",
    }

    strings_ru = {
        "gone": "<b><emoji document_id=5287692511945437157>✅</emoji> Вы успешно вошли в AFK режим!</b>",
        "back": "<b><emoji document_id=5287692511945437157>✅</emoji> Вы успешно вышли из AFK режима!</b>",
        "afk": "<b><emoji document_id=5287613458777387650>😴</emoji> Сейчас я нахожусь в AFK\n<emoji document_id=5287737368583876982>🌀</emoji> Был в сети <code>{}</code> назад</b>",
        "afk_reason": "<b><emoji document_id=5287613458777387650>😴</emoji> Сейчас я нахожусь в AFK\n<emoji document_id=5287737368583876982>🌀</emoji> Был в сети <code>{}</code> назад\n<emoji document_id=5445161912985724546>✏️</emoji> Причина: <i>{}</i></b>",
        "status_added": "<b><emoji document_id=5285372392086976148>🦋</emoji> Статус успешно установлен!</b>",
        "status_removed": "<b><emoji document_id=5879896690210639947>🗑</emoji> Статус успешно удалён!</b>",
        "no_user": "<b><emoji document_id=5287611315588707430>❌</emoji> Не удалось получить информацию о пользователе.</b>",
        "no_previous_status": "<b><emoji document_id=5287740598399285194>😵‍💫</emoji> Предыдущий ник не найден.</b>",
    }

    strings_uz = {
        "gone": "<b><emoji document_id=5287692511945437157>✅</emoji> AFK holatiga muvaffaqiyatli kirdingiz!</b>",
        "back": "<b><emoji document_id=5287692511945437157>✅</emoji> AFK rejimidan muvaffaqiyatli chiqdingiz!</b>",
        "afk": "<b><emoji document_id=5287613458777387650>😴</emoji> Hozir men AFK holatida\n<emoji document_id=5287737368583876982>🌀</emoji> <code>{}</code> avval onlayn bo'lgan</b>",
        "afk_reason": "<b><emoji document_id=5287613458777387650>😴</emoji> Hozir men AFK holatida\n<emoji document_id=5287737368583876982>🌀</emoji> <code>{}</code> avval onlayn bo'lgan\n<emoji document_id=5445161912985724546>✏️</emoji> Sabab: <i>{}</i></b>",
        "status_added": "<b><emoji document_id=5285372392086976148>🦋</emoji> Status muvaffaqiyatli o'rnatildi!</b>",
        "status_removed": "<b><emoji document_id=5879896690210639947>🗑</emoji> Status muvaffaqiyatli olib tashlandi!</b>",
        "no_user": "<b><emoji document_id=5287611315588707430>❌</emoji> Foydalanuvchi ma'lumotlari olishda xatolik.</b>",
        "no_previous_status": "<b><emoji document_id=5287740598399285194>😵‍💫</emoji> Avvalgi nom topilmadi.</b>",
    }

    strings_de = {
        "gone": "<b><emoji document_id=5287692511945437157>✅</emoji> Du hast den AFK-Modus erfolgreich aktiviert!</b>",
        "back": "<b><emoji document_id=5287692511945437157>✅</emoji> Du hast den AFK-Modus erfolgreich deaktiviert!</b>",
        "afk": "<b><emoji document_id=5287613458777387650>😴</emoji> Ich bin derzeit im AFK\n<emoji document_id=5287737368583876982>🌀</emoji> War vor <code>{}</code> online</b>",
        "afk_reason": "<b><emoji document_id=5287613458777387650>😴</emoji> Ich bin derzeit im AFK\n<emoji document_id=5287737368583876982>🌀</emoji> War vor <code>{}</code> online\n<emoji document_id=5445161912985724546>✏️</emoji> Grund: <i>{}</i></b>",
        "status_added": "<b><emoji document_id=5285372392086976148>🦋</emoji> Status erfolgreich gesetzt!</b>",
        "status_removed": "<b><emoji document_id=5879896690210639947>🗑</emoji> Status erfolgreich entfernt!</b>",
        "no_user": "<b><emoji document_id=5287611315588707430>❌</emoji> Benutzerinformationen konnten nicht abgerufen werden.</b>",
        "no_previous_status": "<b><emoji document_id=5287740598399285194>😵‍💫</emoji> Vorheriger Spitzname nicht gefunden.</b>",
    }

    strings_es = {
        "gone": "<b><emoji document_id=5287692511945437157>✅</emoji> ¡Has entrado correctamente en el modo AFK!</b>",
        "back": "<b><emoji document_id=5287692511945437157>✅</emoji> ¡Has salido correctamente del modo AFK!</b>",
        "afk": "<b><emoji document_id=5287613458777387650>😴</emoji> Actualmente estoy en AFK\n<emoji document_id=5287737368583876982>🌀</emoji> Estuve en línea hace <code>{}</code></b>",
        "afk_reason": "<b><emoji document_id=5287613458777387650>😴</emoji> Actualmente estoy en AFK\n<emoji document_id=5287737368583876982>🌀</emoji> Estuve en línea hace <code>{}</code>\n<emoji document_id=5445161912985724546>✏️</emoji> Razón: <i>{}</i></b>",
        "status_added": "<b><emoji document_id=5285372392086976148>🦋</emoji> ¡Estado establecido correctamente!</b>",
        "status_removed": "<b><emoji document_id=5879896690210639947>🗑</emoji> ¡Estado eliminado correctamente!</b>",
        "no_user": "<b><emoji document_id=5287611315588707430>❌</emoji> No se pudieron obtener las información del usuario.</b>",
        "no_previous_status": "<b><emoji document_id=5287740598399285194>😵‍💫</emoji> Nombre de usuario anterior no encontrado.</b>",
    }

    async def client_ready(self, client, db):
        self.client = client
        self._db = db
        self._me = await client.get_me()

    @loader.command(
        ru_doc="[reason] - Установить режим AFK",
        uz_doc="[reason] - AFK holatini sozlash",
        de_doc="[reason] - AFK-Modusstatus setzen",
        es_doc="[reason] - Establecer estado de modo AFK"
    )
    async def afk(self, message):
        """[reason] - Set AFK mode status"""
        if utils.get_args_raw(message):
            self._db.set(__name__, "afk", utils.get_args_raw(message))
        else:
            self._db.set(__name__, "afk", True)
        self._db.set(__name__, "gone", time.time())
        self._db.set(__name__, "ratelimit", [])
        await self.allmodules.log("afk", data=utils.get_args_raw(message) or None)
        await utils.answer(message, self.strings("gone", message))

    @loader.command(
        ru_doc="Выйти из режима AFK",
        uz_doc="AFK rejimidan chiqish",
        de_doc="Verlassen des AFK-Modus",
        es_doc="Salir del modo AFK"
    )
    async def unafk(self, message):
        """Exit AFK mode"""
        self._db.set(__name__, "afk", False)
        self._db.set(__name__, "gone", None)
        self._db.set(__name__, "ratelimit", [])
        await self.allmodules.log("unafk")
        await utils.answer(message, self.strings("back", message))

    @loader.command(
        ru_doc="Установить статус AFK",
        uz_doc="AFK holatini sozlash",
        de_doc="Setzt den AFK-Status",
        es_doc="Establece el estado AFK"
    )
    async def setstatus(self, message):
        """Set the AFK status"""
        user = await utils.get_user(message)
        if user:
            current_last_name = user.last_name if user.last_name else ""

            if " || AFK" in current_last_name:
                await utils.answer(message, self.strings["status_added"].format(name=current_last_name))
                return

            new_last_name = current_last_name + " || AFK"
            try:
                await self.client(functions.account.UpdateProfileRequest(last_name=new_last_name))
                await utils.answer(message, self.strings["status_added"].format(name=new_last_name))
            except Exception as e:
                await utils.answer(message, f"<b>Ошибка при добавлении статуса: {str(e)}</b>")
        else:
            await utils.answer(message, self.strings["no_user"])

    @loader.command(
        ru_doc="Удалить статус AFK",
        uz_doc="AFK holatini o'chirish",
        de_doc="Löscht den AFK-Status",
        es_doc="Eliminar el estado AFK"
    )
    async def removestatus(self, message):
        """Удалить статус AFK."""
        user = await utils.get_user(message)
        if user:
            current_last_name = user.last_name if user.last_name else ""

            if " || AFK" in current_last_name:
                try:
                    previous_first_name = user.first_name if user.first_name else ""
                    previous_last_name = current_last_name.replace(" || AFK", "")
                    await self.client(functions.account.UpdateProfileRequest(first_name=previous_first_name, last_name=previous_last_name))
                    await utils.answer(message, self.strings["status_removed"])
                except Exception as e:
                    await utils.answer(message, f"<b>Ошибка при удалении статуса: {str(e)}</b>")
            else:
                await utils.answer(message, self.strings["no_previous_status"])
        else:
            await utils.answer(message, self.strings["no_user"])

    async def watcher(self, message):
        if not isinstance(message, types.Message):
            return
        if message.mentioned or getattr(message.to_id, "user_id", None) == self._me.id:
            afk_state = self.get_afk()
            if not afk_state:
                return
            logger.debug("tagged!")
            ratelimit = self._db.get(__name__, "ratelimit", [])
            if utils.get_chat_id(message) in ratelimit:
                return
            else:
                self._db.setdefault(__name__, {}).setdefault("ratelimit", []).append(
                    utils.get_chat_id(message)
                )
                self._db.save()
            user = await utils.get_user(message)
            if user.is_self or user.bot or user.verified:
                logger.debug("User is self, bot or verified.")
                return
            if self.get_afk() is False:
                return
            now = datetime.datetime.now().replace(microsecond=0)
            gone = datetime.datetime.fromtimestamp(
                self._db.get(__name__, "gone")
            ).replace(microsecond=0)
            diff = now - gone
            if afk_state is True:
                ret = self.strings("afk", message).format(diff)
            elif afk_state is not False:
                ret = self.strings("afk_reason", message).format(diff, afk_state)
            await utils.answer(message, ret, reply_to=message)

    def get_afk(self):
        return self._db.get(__name__, "afk", False)
