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

# Name: Reports
# Author: dend1yya
# Commands:
# .addadmins | .chaton | .chatoff | .report
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/5131a980bd2f80ad463ad.jpg

__version__ = (1, 0, 0)

from hikkatl.types import Message  # type: ignore
from telethon.tl.functions.channels import InviteToChannelRequest  # type: ignore
from telethon.tl.functions.users import GetFullUserRequest #type: ignore
from telethon.tl.functions.channels import CreateChannelRequest, InviteToChannelRequest #type: ignore
from telethon.tl.types import ChatAdminRights #type: ignore
from .. import loader, utils
import logging

logger = logging.getLogger(__name__)

@loader.tds
class ReportsMod(loader.Module):
    """Module for sending reports to the administration."""

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

    strings_uz = {
        "admin_id": "ADMIN_ID",
        "loading": "<b>Yuklanmoqda...</b>",
        "group_created": "<b>Hisobot kanali ochildi va agar ko'rsatilgan bo'lsa, administrator(lar) taklif qilindi.</b>",
        "group_error": "<b>Hisobot kanaliga kirishda xato yuz berdi.</b>",
        "no_admins": "<b>Taklif qilish uchun administratorlar mavjud emas.</b>",
        "reports_enabled": "<b>Hisobot qabul qilish ushbu chatda yoqilgan.</b>",
        "reports_disabled": "<b>Hisobot qabul qilish ushbu chatda o'chirilgan.</b>",
        "reports_not_enabled": "<b>Hisobot ushbu chatda yoqilmagan.</b>",
        "not_args": "<b>Foydalanish: .report {userID/@username} (sababi)</b>",
        "parts_both_2": "<b>Iltimos, foydalanuvchi va sababni taqdim eting.</b>",
        "success": "<b>Hisobot muvaffaqiyatli yuborildi.</b>",
        "fail": "<b>Hisobot yuborishda xato yuz berdi.</b>",
    }

    strings_de = {
        "admin_id": "ADMIN_ID",
        "loading": "<b>Wird geladen...</b>",
        "group_created": "<b>Berichtskanal aufgerufen und Administrator(en) eingeladen, falls angegeben.</b>",
        "group_error": "<b>Fehler beim Zugreifen auf den Berichtskanal.</b>",
        "no_admins": "<b>Keine Administratoren konfiguriert, um einzuladen.</b>",
        "reports_enabled": "<b>Berichtserfassung in diesem Chat aktiviert.</b>",
        "reports_disabled": "<b>Berichtserfassung in diesem Chat deaktiviert.</b>",
        "reports_not_enabled": "<b>Berichte in diesem Chat nicht aktiviert.</b>",
        "not_args": "<b>Verwendung: .report {userID/@username} (Grund)</b>",
        "parts_both_2": "<b>Bitte sowohl einen Benutzer als auch einen Grund angeben.</b>",
        "success": "<b>Bericht erfolgreich eingereicht.</b>",
        "fail": "<b>Fehler beim Einreichen des Berichts.</b>",
    }

    strings_es = {
        "admin_id": "ADMIN_ID",
        "loading": "<b>Cargando...</b>",
        "group_created": "<b>Canal de informes accedido y administrador(es) invitado(s) si se especificó.</b>",
        "group_error": "<b>Error al acceder al canal de informes.</b>",
        "no_admins": "<b>No hay administradores configurados para invitar.</b>",
        "reports_enabled": "<b>Recepción de informes habilitada en este chat.</b>",
        "reports_disabled": "<b>Recepción de informes deshabilitada en este chat.</b>",
        "reports_not_enabled": "<b>Los informes no están habilitados en este chat.</b>",
        "not_args": "<b>Uso: .report {userID/@username} (razón)</b>",
        "parts_both_2": "<b>Por favor, proporcione tanto un usuario como una razón.</b>",
        "success": "<b>Informe enviado con éxito.</b>",
        "fail": "<b>Error al enviar el informe.</b>",
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
        try:
            result = await client(CreateChannelRequest(
                title="Aurora-Reports",
                about="🐬 chat for reports from users",
                megagroup=True
            ))
            self.Aurora_Reports = result.chats[0]
        except Exception as e:
            logger.error(f"Failed to create report group: {str(e)}")

    @loader.command(
        ru_doc="Добавить администраторов из конфигурации в группу.",
        uz_doc="Konfiguratsiyadan administratorlarni guruhga qo'shadi.",
        de_doc="Fügt Administratoren aus der Konfiguration zur Gruppe hinzu.",
        es_doc="Agrega administradores desde la configuración al grupo.",
    )
    async def addadmins(self, message):
        """Add administrators from the config to the group"""
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

    @loader.command(
        ru_doc="Включает чат для репортов.",
        uz_doc="Hisobotlar uchun chatni yoqadi.",
        de_doc="Aktiviert den Chat für Berichte.",
        es_doc="Habilita el chat para informes.",
    )
    async def chaton(self, message):
        """Enable chat for reports"""
        chat_id = str(message.chat_id)
        self.db.set("ReportsMod", f"report_active_{chat_id}", True)
        await utils.answer(message, self.strings["reports_enabled"])

    @loader.command(
        ru_doc="Отключает чат для репортов.",
        uz_doc="Hisobotlar uchun chatni o'chiradi.",
        de_doc="Deaktiviert den Chat für Berichte.",
        es_doc="Desactiva el chat para informes.",
    )
    async def chatoff(self, message):
        """Disable chat for reports"""
        chat_id = str(message.chat_id)
        self.db.set("ReportsMod", f"report_active_{chat_id}", False)
        await utils.answer(message, self.strings["reports_disabled"])

    @loader.command(
        ru_doc="Отправляет репорт администрации.",
        uz_doc="Ma'muriyatga hisobot yuboradi.",
        de_doc="Sendet einen Bericht an die Verwaltung.",
        es_doc="Envía un informe a la administración.",
    )
    async def report(self, message):
        """Sends a report to the administration."""
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
