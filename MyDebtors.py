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

# Name: MyDebtors
# Author: dend1yya | Felix?
# Commands:
# .dadd | .dinfo | .ddel | .dlist | .ddelall
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/7d7a4c3ff3711e0e1ee88.jpg

__version__ = (1, 1, 0)

from telethon.tl.types import Message # type: ignore
from .. import loader, utils

@loader.tds
class MyDebtorsMod(loader.Module):
    """Module for managing, adding, and deleting your debtors."""

    strings = {
        "name": "MyDebtors",
        "saved": "💾 <b>Debtor added:</b>\n<code>{}</code> - <b>Amount:</b> {}",
        "no_reply": "🚫 <b>Reply with debtor name and amount.</b>",
        "no_name": "🚫 <b>Specify debtor's name and amount.</b>",
        "no_debtor": "🚫 <b>Debtor not found.</b>",
        "available_debtors": "💾 <b>Current debtors:</b>\n",
        "no_debtors": "😔 <b>You have no debtors yet.</b>",
        "deleted": "🙂 <b>Debtor removed:</b> <code>{}</code>",
        "all_deleted": "🙂 <b>All debtors have been removed.</b>",
        "changed": "🔄 <b>Debtor's debt changed:</b> <code>{}</code> - <b>New amount:</b> {}",
    }

    strings_ru = {
        "saved":"💾 <b>Должник добавлен: </b>\n<code>{}</code> - <b>Сумма: </b> {}",
        "no_reply": "🚫 <b>Требуется реплай на контент должника, и суммы.</b>",
        "no_name": "🚫 <b>Укажите имя должника, и сумму.</b>",
        "no_debtor": "🚫 <b>Должник не найден.</b>",
        "available_debtors": "💾 <b>Текущие должники:</b>\n",
        "no_debtors": "😔 <b>У вас нету должников.</b>",
        "deleted": "🙂 <b>Должник удален:</b> <code>{}</code>",
        "all_deleted": "🙂 <b>Все ваши должники были удалены.</b>",
        "changed": "🔄 <b>Долг должника изменен:</b> <code>{}</code> - <b>Новая сумма:</b> {}",
    }

    strings_uz = {
        "saved":"💾 <b>Qarzdor qo'shildi:</b>\n<code>{}</code> - <b>Summa:</b> {}",
        "no_reply": "🚫 <b>Qarzdor nomi va miqdorini javob bering.</b>",
        "no_name": "🚫 <b>Qarzdor nomini va miqdorini kiriting.</b>",
        "no_debtor": "🚫 <b>Qarzdor topilmadi.</b>",
        "available_debtors": "💾 <b>Hoziroq qarz beruvchilar:</b>\n",
        "no_debtors": "😔 <b>Sizda hozircha qarzdorlar yo'q.</b>",
        "deleted": "🙂 <b>Qarzdor o'chirildi:</b> <code>{}</code>",
        "all_deleted": "🙂 <b>Barcha qarzdorlar o'chirildi.</b>",
        "changed": "🔄 <b>Qarzdor qarzi o'zgartirildi:</b> <code>{}</code> - <b>Yangi miqdor:</b> {}",
    }

    strings_de = {
        "saved":"💾 <b>Schuldner hinzugefügt:</b>\n<code>{}</code> - <b>Betrag:</b> {}",
        "no_reply": "🚫 <b>Antworten Sie mit dem Namen des Schuldners und dem Betrag.</b>",
        "no_name": "🚫 <b>Geben Sie den Namen und den Betrag des Schuldners an.</b>",
        "no_debtor": "🚫 <b>Schuldner nicht gefunden.</b>",
        "available_debtors": "💾 <b>Aktuelle Schuldner:</b>\n",
        "no_debtors": "😔 <b>Sie haben noch keine Schuldner.</b>",
        "deleted": "🙂 <b>Schuldner entfernt:</b> <code>{}</code>",
        "all_deleted": "🙂 <b>Alle Schuldner wurden entfernt.</b>",
        "changed": "🔄 <b>Schulden des Schuldners geändert:</b> <code>{}</code> - <b>Neuer Betrag:</b> {}",
    }

    strings_es = {
        "saved":"💾 <b>Deudor agregado:</b>\n<code>{}</code> - <b>Monto:</b> {}",
        "no_reply": "🚫 <b>Responder con el nombre del deudor y el monto.</b>",
        "no_name": "🚫 <b>Especifique el nombre y el monto del deudor.</b>",
        "no_debtor": "🚫 <b>Deudor no encontrado.</b>",
        "available_debtors": "💾 <b>Deudores actuales:</b>\n",
        "no_debtors": "😔 <b>No tienes deudores aún.</b>",
        "deleted": "🙂 <b>Deudor eliminado:</b> <code>{}</code>",
        "all_deleted": "🙂 <b>Se han eliminado todos los deudores.</b>",
        "changed": "🔄 <b>Deuda del deudor cambiada:</b> <code>{}</code> - <b>Nuevo monto:</b> {}",
    }

    async def client_ready(self):
        self._debtors = self.get("debtors", {})

    @loader.command(
        ru_doc="<name> <amount> - Добавить должника",
        uz_doc="<name> <amount> - Qarzdor qo'shish",
        de_doc="<name> <amount> - Schuldner hinzufügen",
        es_doc="<name> <amount> - Agregar un deudor",
    )
    async def dadd(self, message: Message):
        """<name> <amount> - add a debtor"""
        args = utils.get_args_raw(message)

        if not args:
            await utils.answer(message, self.strings("no_reply"))
            return

        debtor_name, amount = args.split(maxsplit=1)

        if not (debtor_name and amount):
            await utils.answer(message, self.strings("no_name"))
            return

        amount = int(amount)

        if debtor_name not in self._debtors:
            self._debtors[debtor_name] = 0

        self._debtors[debtor_name] += amount

        self.set("debtors", self._debtors)

        await utils.answer(message, self.strings("saved").format(debtor_name, amount))

    def _get_debtor(self, name):
        return self._debtors.get(name)

    def _del_debtor(self, name):
        if name in self._debtors:
            del self._debtors[name]
            self.set("debtors", self._debtors)
            return True

        return False

    @loader.command(
        ru_doc="<name> - Узнать информацию о должнике",
        uz_doc="<name> - Qarzdor haqida ma'lumot olish",
        de_doc="<name> - Informationen über den Schuldner erhalten",
        es_doc="<name> - Obtener información sobre el deudor",
    )
    async def dinfo(self, message: Message):
        """<name> - Find out information about the debtor"""
        debtor_name = utils.get_args_raw(message)

        if not debtor_name:
            await utils.answer(message, self.strings("no_name"))
            return

        amount = self._get_debtor(debtor_name)

        if amount is not None:
            await utils.answer(message, f"💸 <b>{debtor_name} долг:</b> {amount}")
        else:
            await utils.answer(message, self.strings("no_debtor"))

    @loader.command(
        ru_doc="<name> - Удалить должника",
        uz_doc="<name> - Qarzdorni olib tashlash",
        de_doc="<name> - Schuldner entfernen",
        es_doc="<name> - Eliminar al deudor",
    )
    async def ddel(self, message: Message):
        """<name> - Remove the debtor"""
        debtor_name = utils.get_args_raw(message)

        if not debtor_name:
            await utils.answer(message, self.strings("no_name"))
            return

        if self._del_debtor(debtor_name):
            await utils.answer(message, self.strings("deleted").format(debtor_name))
        else:
            await utils.answer(message, self.strings("no_debtor"))

    @loader.command(
        ru_doc="Список всех ваших должников",
        uz_doc="Sizning qarz berganlar ro'yxati",
        de_doc="Liste aller Ihrer Schuldner",
        es_doc="Lista de todos sus deudores",
    )
    async def dlist(self, message: Message):
        """List of all your debtors"""
        result = self.strings("available_debtors")

        if not self._debtors:
            await utils.answer(message, self.strings("no_debtors"))
            return

        for debtor_name, amount in self._debtors.items():
            result += f"\n💸 <b>{debtor_name}:</b> {amount}"

        await utils.answer(message, result)

    @loader.command(
        ru_doc="Удалить всех ваших должников",
        uz_doc="Sizning barcha qarz berganlaringizni olib tashlash",
        de_doc="Alle Ihre Schuldner entfernen",
        es_doc="Eliminar a todos sus deudores",
    )
    async def ddelall(self, message: Message):
        """Remove all your debtors"""
        self._debtors = {}
        self.set("debtors", self._debtors)
        await utils.answer(message, self.strings("all_deleted"))

    @loader.command(
        ru_doc="<name> <amount> - Изменить долг",
        uz_doc="<name> <amount> - Qarzni o'zgartirish",
        de_doc="<name> <amount> - Schulden ändern",
        es_doc="<name> <amount> - Cambiar la deuda",
    )
    async def dset(self, message: Message):
        """<name> <amount> - Change the debt"""
        args = utils.get_args_raw(message)

        if not args:
            await utils.answer(message, self.strings("no_reply"))
            return

        debtor_name, new_amount = args.split(maxsplit=1)

        if not (debtor_name and new_amount):
            await utils.answer(message, self.strings("no_name"))
            return

        new_amount = int(new_amount)

        if debtor_name in self._debtors:
            self._debtors[debtor_name] = new_amount
            self.set("debtors", self._debtors)
            await utils.answer(message, self.strings("changed").format(debtor_name, new_amount))
        else:
            await utils.answer(message, self.strings("no_debtor"))
