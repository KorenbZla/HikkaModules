# Name: MyDoljniki
# Author: Dend1yya | Felix?
# Commands:
# .dadd | .dinfo | .ddel | .dlist | .ddellall
# scope: hikka_only
# meta developer: @AuroraModules


__version__ = (1, 0, 0)


import logging

from telethon.tl.types import Message

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class MyDoljnikiMod(loader.Module):
    """Модуль для управления, добавления, и удаления ваших должников."""

    strings = {
        "name": "MyDoljniki",
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

    async def client_ready(self):
        self._debtors = self.get("debtors", {})

    async def daddcmd(self, message: Message):
        """<name> <amount> - Добавить должника"""
        args = utils.get_args_raw(message)

        if not args:
            await utils.answer(message, self.strings("no_reply"))
            return

        debtor_name, amount = args.split(maxsplit=1)

        if not (debtor_name and amount):
            await utils.answer(message, self.strings("no_name"))
            return

        amount = float(amount)

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

    async def dinfocmd(self, message: Message):
        """<name> - Узнать информацию о должнике"""
        debtor_name = utils.get_args_raw(message)

        if not debtor_name:
            await utils.answer(message, self.strings("no_name"))
            return

        amount = self._get_debtor(debtor_name)

        if amount is not None:
            await utils.answer(message, f"💸 <b>{debtor_name} долг:</b> {amount}")
        else:
            await utils.answer(message, self.strings("no_debtor"))

    async def ddelcmd(self, message: Message):
        """<name> - Убрать должника"""
        debtor_name = utils.get_args_raw(message)

        if not debtor_name:
            await utils.answer(message, self.strings("no_name"))
            return

        if self._del_debtor(debtor_name):
            await utils.answer(message, self.strings("deleted").format(debtor_name))
        else:
            await utils.answer(message, self.strings("no_debtor"))

    async def dlistcmd(self, message: Message):
        """ Список всех ваших должников"""
        result = self.strings("available_debtors")

        if not self._debtors:
            await utils.answer(message, self.strings("no_debtors"))
            return

        for debtor_name, amount in self._debtors.items():
            result += f"\n💸 <b>{debtor_name}:</b> {amount}"

        await utils.answer(message, result)


    async def ddellallcmd(self, message: Message):
        """Убрать всех ваших должников"""
        self._debtors = {}
        self.set("debtors", self._debtors)
        await utils.answer(message, self.strings("all_deleted"))

    async def dsetcmd(self, message: Message):
        """<name> <amount> - Изменить долг"""
        args = utils.get_args_raw(message)

        if not args:
            await utils.answer(message, self.strings("no_reply"))
            return

        debtor_name, new_amount = args.split(maxsplit=1)

        if not (debtor_name and new_amount):
            await utils.answer(message, self.strings("no_name"))
            return

        new_amount = float(new_amount)

        if debtor_name in self._debtors:
            self._debtors[debtor_name] = new_amount
            self.set("debtors", self._debtors)
            await utils.answer(message, self.strings("changed").format(debtor_name, new_amount))
        else:
            await utils.answer(message, self.strings("no_debtor"))
