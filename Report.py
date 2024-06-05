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

# Name: Report
# Author: dend1yya
# Commands:
# .addadmins | .chaton | .chatoff | .report
# scope: hikka_only
# meta developer: @AuroraModules

__version__ = (1, 0, 0)

from hikkatl.types import Message  # type: ignore
from telethon.tl.functions.channels import InviteToChannelRequest  # type: ignore
from telethon.tl.functions.users import GetFullUserRequest #type: ingore
from telethon.tl.functions.channels import CreateChannelRequest, InviteToChannelRequest #type: ignore
from telethon.tl.types import ChatAdminRights #type: ignore
from .. import loader, utils
import logging

logger = logging.getLogger(__name__)

@loader.tds
class ReportsMod(loader.Module):
    """Модуль для отправки репортов."""
    strings = {
        "name": "Reports",
        "admin_id": "ADMIN_ID",
        "loading": "<b>Loading...</b>",
        "group_created": "<b>Report Channel accessed and admin(s) invited if specified.</b>",
        "group_error": "<b>Error accessing the report channel.</b>",
        "no_admins": "<b>No admins configered to ivnite.</b>",
        "reports_enabled": "Report reception enabled in this chat.",
        "reports_disabled": "Report reception disabled in this chat.",
        "reports_not_enabled": "<b>Reports not enabled in this chat.</b>",
        "not_args": "<b>Usage: .report {userID/@username} (reason)</b>",
        "parts_both_2": "<b>Please provide both a user and a reason.</b>",
        "success": "<b>Report submitted successfully.</b>",
        "fail": "<b>Failed to submit the report.</b>",
    }

    strings_ru = {
        "admin_id": "ADMIN_ID",
        "loading": "<b>Загрузка...</b>",
        "group_created": "<b>Группа для репортов создана, и администраторы были приглашены.</b>",
        "group_error": "<b>Ошибка при создании канала с репортами.",
        "no_admins": "<b>Нету администраторов которых можно добавить в группу.</b>",
        "reports_enabled": "<b>Репорты включены в этом чате</b>",
        "reports_disabled": "<b>Репорты выключены в этом чате</b>",
        "reports_not_enabled": "<b>Репорты не включены в этом чате.</b>",
        "not_args": "<b>Использование: .report{userID/@username} (причина)</b>",
        "parts_both_2": "<b>Пожалуйста введите имя пользователя и причину.</b>",
        "success": "<b>Репорт успешно отправлен.</b>",
        "fail": "<b>Ошибка при отправке репорта.</b>"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "admin_id",
            None,
            lambda: self.strings["admin_id"]
        )

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        logger.info("AuroraReports installed!")
        try:
            result = await client(CreateChannelRequest(
                title="Aurora-Reports",
                about="Группа, куда приходят репорты",
                megagroup=True
            ))
            self.Aurora_Reports = result.chats[0]
        except Exception as e:
            logger.error(f"Failed to create report group: {str(e)}")

    async def addadminscmd(self, message):
        """Приглашает администраторов в супергруппу"""
        await utils.answer(message, self.strings["loading"])
        try:
            admin_ids = self.config.get("admin_id")
            if not admin_ids:
                await utils.answer(message, self.strings["no_admins"])
                return
            
            if isinstance(admin_ids, list):
                for admin_id in admin_ids:
                    await self.client(InviteToChannelRequest(
                        channel=self.Aurora_Reports,
                        users=[admin_id]
                    ))
            else:
                await self.client(InviteToChannelRequest(
                    channel=self.Aurora_Reports,
                    users=[admin_ids]
                ))
            await utils.answer(message, self.strings["group_created"])
        except Exception as e:
            logger.error(f"Failed to invite admins to the report group: {str(e)}")
            await utils.answer(message, self.strings["group_error"])

    async def chatoncmd(self, message):
        """Включает прием репортов в этом чате."""
        chat_id = str(message.chat_id)
        self.db.set("ReportsMod", f"report_active_{chat_id}", True)
        await utils.answer(message, self.strings["reports_enabled"])

    async def chatoffcmd(self, message):
        """Выключает прием репортов в этом чате."""
        chat_id = str(message.chat_id)
        self.db.set("ReportsMod", f"report_active_{chat_id}", False)
        await utils.answer(message, self.strings["reports_disabled"])


    async def reportcmd(self, message):
        """Отправляет репорт администрации."""
        chat_id = str(message.chat_id)
        report_active = self.db.get("ReportsMod", f"report_active_{chat_id}", False)

        if not report_active:
            await utils.answer(message, self.strings["reports_not_enabled"])
            return

        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings["not_args"])
            return

        parts = args.split(maxsplit=1)
        if len(parts) < 2:
            await utils.answer(message, self.strings["parts_both_2"])
            return

        user_id_or_name, reason = parts
        try:
            if user_id_or_name.isdigit():
                user_id = int(user_id_or_name)
            else:
                user_id = user_id_or_name

            user = await self.client.get_entity(user_id)
            reporter = await self.client.get_entity(message.sender_id)

            report_message = (f"<b>🚨 Report Submitted 🚨</b>\n\n"
                              f"<b>Reporter:</b> @{reporter.username if reporter.username else 'unknown'} (ID: {reporter.id})\n"
                              f"<b>Reported User:</b> @{user.username if user.username else 'unknown'} (ID: {user.id})\n"
                              f"<b>Reason:</b> {reason}")

            await self.client.send_message(self.Aurora_Reports, report_message)
            await utils.answer(message, self.strings["success"])
        except Exception as e:
            logger.error(f"Failed to process the report: {str(e)}")
            await utils.answer(message, self.strings["fail"])
