# Name: Report
# Author: dend1yya
# Commands:
# .report | .reporton | .reportoff | .reporthelp
# scope: hikka_only
# meta developer: @AuroraModules
from telethon import functions

from .. import loader, utils

@loader.tds
class ReportsMod(loader.Module):
    """Модуль для отправки репортов"""
    strings = {
        "name": "Reports",
        "report_enabled": "<b><emoji document_id=5345863488872916640>✅</emoji> Репорты включены.\nСоздан чат 'reports'.</b>",
        "report_disabled": "<b><emoji document_id=5467928559664242360>❗️</emoji> Репорты выключены. Чат 'reports' удален.</b>",
        "report_sent": "<b><emoji document_id=5447644880824181073>⚠️</emoji> Новый репорт:</b>\n\n<b><emoji document_id=5219822691409733126>⚙️</emoji> Кто отправил:</b> {}\n<b><emoji document_id=5467666648263564704>❓</emoji> На кого отправлен:</b> {}\n<b><emoji document_id=5972183258090179945>💬</emoji> Причина:</b> {}",
        "not_enabled": "<b><emoji document_id=5467928559664242360>❗️</emoji> Репорты не включены. Включите командой .reporton.</b>",
        "already_enabled": "<b><emoji document_id=5231200819986047254>📊</emoji> Репорты уже включены.</b>",
        "already_disabled": "<b><emoji document_id=5231200819986047254>📊</emoji> Репорты уже выключены.</b>",
        "module_help": "<b><emoji document_id=5226512880362332956>📖</emoji> Краткая документация по использованию модуля:\n\n<b><emoji document_id=5447644880824181073>⚠️</emoji> Важное примечание! Модуль reports работает только для одного чата (пока что) И если вы попытаетесь использовать модуль в разных чатах, то у вас ничего не получится\n\n<emoji document_id=5382187118216879236>❓</emoji>Как разрешить команду всем пользователям? К сожалениию это можно сделать только через tsec\n\n<emoji document_id=5282843764451195532>🖥</emoji> Чтобы выдать tsec пользователю используй эту команду: tsec <user/chat/sgroup> [цель пользователя или чата] [правило (команда/модуль)] [время] - Добавить новое правило таргетированной безопасности\n\n<emoji document_id=5310044041444865824>💻</emoji>Или вы можете выдать пользователю группу Owner через команду: !owneradd (username)/(reply)</b>",
        "invalid_args": "<b><emoji document_id=5467666648263564704>❓</emoji> Укажите пользователя и причину репорта.</b>",
        "wrong_format": "<b><emoji document_id=5980953710157632545>❌</emoji> Неверный формат.\n<emoji document_id=5467928559664242360>❗️</emoji>Используйте: report (юзернейм) (причина)</b>",
        "report_sented": "<b><emoji document_id=5980930633298350051>✅</emoji> Ваш репорт успешно отправлен!</b>\n\n<i><emoji document_id=5255835635704408236>👤</emoji> Администрация свяжется с вами в ближайшее время, и вынесет вердикт.</i>"
    }
    strings_en = {
        "report_enabled": "<b>Report on.\n<emoji document_id=5895457880710058528>💬</emoji>Created chat 'report'.</b>",
        "report_disabled": "<b>Report off. Chat 'reports' deleted.</b>",
        "report_sent": "<b>New report:</b>\n\n<b>Who send:</b>{}\n<b>Sent to:</b>{}\n<b>Reason:</b> {}",
        "not_enabled": "<b>Reports not included. Turn them on comand reporton.</b>",
        "already_enabled": "<b>Reports are already inculuded</b>",
        "already_disabled": "<b>Reports already disabled.</b>",
        "module_help": "<b>Brief documentation on using the module:\n\nImportant note! The module only works for one chat (for now) And if you try to use the module in different chats, it will not work\n\nHow to allow a command to all users?\n\nUnfortunately this can only be done through tsec\n\nTo issue tsec use this command: tsec <user/chat/sgroup> [target user or chat] [rule (command/module)] [time] - Add new targeted security rule\n\nOr u cane use 'owneradd' example: owneradd(user)/(reply)</b>",
        "invalid_args": "<b>Specify the user and reason for the report.</b>",
        "wrong_format": "<b>Wrong format. Use: report (username) (reason)</b>",
        "report_sented": "<b>Report succefully sented.</b>"
    }

    async def client_ready(self, client, db):
        self.client = client
        self.reports_chat = None

    async def reportoncmd(self, message):
        """Включить репорты"""
        if not self.reports_chat:
            result = await self.client(functions.messages.CreateChatRequest(users=['reports'], title='Reports'))
            self.reports_chat = result.chats[0].id
            await utils.answer(message, self.strings["report_enabled"])
        else:
            await utils.answer(message, self.strings["already_enabled"])

    async def reportoffcmd(self, message):
        """Отключить репорты"""
        if self.reports_chat:
            await self.client(functions.messages.DeleteChatRequest(chat_id=self.reports_chat))
            self.reports_chat = None
            await utils.answer(message, self.strings["report_disabled"])
        else:
            await utils.answer(message, self.strings["already_disabled"])

    async def reportcmd(self, message):
        """Отправить репорт"""
        if self.reports_chat:
            args = utils.get_args_raw(message)
            if not args:
                return await utils.answer(message, self.strings["invalid_args"])
            try:
                target, reason = args.split(' ', 1)
            except ValueError:
                return await utils.answer(message, self.strings["wrong_format"])
            report_text = self.strings["report_sent"].format(message.sender_id, target, reason)
            await self.client.send_message(self.reports_chat, report_text)
            await utils.answer(message, self.strings["report_sented"])
        else:
            await utils.answer(message, self.strings["not_enabled"])

    async def reporthelpcmd(self, message):
        """Показать помощь по модулю."""
        await utils.answer(message, self.strings["module_help"])