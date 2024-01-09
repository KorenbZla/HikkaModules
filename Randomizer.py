# Name: Randomizer
# Author: dend1yya
# Commands:
# .cube | .monetka
# scope: hikka_only
# meta developer: @AuroraModules


__version__ = (1, 0, 0)


import asyncio
from telethon.tl.types import Message

from .. import loader, utils
import random

@loader.tds
class RandomizerMod(loader.Module):
    """Модуль для игры с кубиком, орлом и решкой и другими играми."""

    strings = {
        "name": "Randomizer",
        "invalid_number": "🚫 <b>Invalid number! Please choose a number between 1 and 6.</b>",
        "rolled": "🎲 <b>Rolled the cube, got:</b> <code>{}</code>",
        "win": "🎉 <b>Congratulations! You guessed it right!</b>",
        "lose": "😞 <b>Sorry, you didn't guess it right. Try again!</b>",
        "invalid_monetka": "🚫 <b>Invalid choice! Please choose 'Heads' or 'Tails'.</b>",
        "flipping": "🔄 <b>Flipping the coin...</b>",
        "flipped": "🪙 <b>Coin flipped, it's:</b> <code>{}</code>",
    }

    strings_ru = {
        "invalid_number": "🚫<b>Указано неверное число! Пожалуйста выберите число от 1 до 6.</b>",
        "rolled": "🎲<b>Подробсил кубик и получил:</b> <code>{}</code>",
        "win": "🎉<b>Поздравляем! Вы выйграли</b>",
        "lose": "😞<b>Вы проиграли, вы загадали неверное число. Попробуйте ещё раз!</b>",
        "invalid_monetka": "🚫<b>Неверный выбор! Пожалуйста выберите 'орёл' или 'решка'</b>",
        "flipping": "🔄<b>Подрбасываю монетку...</b>",
        "flipped": "🪙<b>Монетка подброшена, выпало:</b> <code>{}</code>",
    }

    async def cubecmd(self, message: Message):
        """Бросить кубик с числом"""
        args = utils.get_args_raw(message)

        try:
            guessed_number = int(args)
        except ValueError:
            await utils.answer(message, self.strings("invalid_number"))
            return

        if not (1 <= guessed_number <= 6):
            await utils.answer(message, self.strings("invalid_number"))
            return

        result = random.randint(1, 6)

        await utils.answer(message, self.strings("rolled").format(result))
        await asyncio.sleep(2)

        if guessed_number == result:
            await utils.answer(message, self.strings("win"))
        else:
            await utils.answer(message, self.strings("lose"))

    async def monetkacmd(self, message: Message):
        """Подбрасывает монетку, и выдает случайный результат"""
        args = utils.get_args_raw(message)

        if args not in ["орёл", "решка"]:
            await utils.answer(message, self.strings("invalid_monetka"))
            return
        
        animated_text = self.strings("flipping")
        animated_message = await utils.answer(message, animated_text)
        await asyncio.sleep(1)

        result = random.choice(["орёл", "решка"])

        await animated_message.edit(self.strings("flipped").format(result))
        await asyncio.sleep(2)

        if args == result:
            await utils.answer(message, self.strings("win"))
        else:
            await utils.answer(message, self.strings("lose"))