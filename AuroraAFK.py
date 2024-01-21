# Name: AuroraAFK
# Author: dend1yy
# Commands:
# .afk | .removestatus | .setstatus | .unafk  
# scope: hikka_only
# meta developer: @AuroraModules


version = (1,0,1)


import datetim
import logging
import time

from telethon import functions
from telethon import types

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class AuroraAFKMod(loader.Module):
    """AFK модули с функциями статусов."""

    strings = {
        "name": "AuroraAFK",
        "gone": "<b><emoji document_id=5427009714745517609>✅</emoji> Вы успешно встали в AFK!</b>",
        "back": "<b><emoji document_id=5465665476971471368>❌</emoji> Вы успешно вышли из AFK!</b>",
        "afk": "<b><emoji document_id=5217882379804221460>💤</emoji> Я AFK прямо сейчас (с {} назад).</b>",
        "afk_reason": "<b><emoji document_id=5217882379804221460>💤</emoji> Я AFK прямо сейчас (с {} назад).\<emoji document_id=5289862389552919154>🦋</emoji> Причина:</b> <i>{}</i>",
        "status_added": "<b><emoji document_id=5454096630372379732>☑️</emoji> Статус успешно установлен!</b>",
        "status_removed": "<b><emoji document_id=5255831443816327915>🗑</emoji> Статус удален. Возвращен предыдущий ник: {name}</b>",
        "no_user": "<b><emoji document_id=5780371577723948313>❗️</emoji> Не удалось получить информацию о пользователе.</b>",
        "no_previous_status": "<b><emoji document_id=5318972196121486029>🤷‍♂️</emoji> Предыдущий ник не найден.</b>",
    }

    async def client_ready(self, client, db):
        self.client = client
        self._db = db
        self._me = await client.get_me()

    async def afkcmd(self, message):
        """Устанавливает AFK режим .afk [причина]"""
        if utils.get_args_raw(message):
            self._db.set(__name__, "afk", utils.get_args_raw(message))
        else:
            self._db.set(__name__, "afk", True)
        self._db.set(__name__, "gone", time.time())
        self._db.set(__name__, "ratelimit", [])
        await self.allmodules.log("afk", data=utils.get_args_raw(message) or None)
        await utils.answer(message, self.strings("gone", message))

    async def unafkcmd(self, message):
        """Убирает режим AFK"""
        self._db.set(__name__, "afk", False)
        self._db.set(__name__, "gone", None)
        self._db.set(__name__, "ratelimit", [])
        await self.allmodules.log("unafk")
        await utils.answer(message, self.strings("back", message))

    async def setstatuscmd(self, message):
        """Устанавливает статус AFK"""
        user = await utils.get_user(message)
        if user:
            current_first_name = user.first_name
            current_last_name = user.last_name if user.last_name else ""

            if "Sleep |" in current_first_name:
                await utils.answer(message, self.strings["status_already_added"].format(name=current_first_name))
                return

            new_first_name = f"Sleep | {current_first_name}"
            new_last_name = current_last_name

            try:
                await self.client(functions.account.UpdateProfileRequest(first_name=new_first_name, last_name=new_last_name))
                await utils.answer(message, self.strings["status_added"].format(name=new_first_name))
            except Exception as e:
                await utils.answer(message, f"<b>Ошибка при добавлении статуса: {str(e)}</b>")
        else:
            await utils.answer(message, self.strings["no_user"])

    async def removestatuscmd(self, message):
        """Удаляет статус AFK"""
        user = await utils.get_user(message)
        if user:
            current_first_name = user.first_name

            if "Sleep |" in current_first_name:
                try:
                    previous_first_name = current_first_name.replace("Sleep | ", "")
                    previous_last_name = user.last_name if user.last_name else ""
                    await self.client(functions.account.UpdateProfileRequest(first_name=previous_first_name, last_name=previous_last_name))
                    await utils.answer(message, self.strings["status_removed"].format(name=previous_first_name))
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
