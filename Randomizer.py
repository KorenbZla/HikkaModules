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

# Name: Randomizer
# Author: dend1yya | Felix?
# Commands:
# .cube | .monetka | .rnum
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/201288f407537011ce0ed.jpg

__version__ = (1, 1, 1)

import random
import asyncio
from telethon.tl.types import Message # type: ignore
from .. import loader, utils

@loader.tds
class RandomizerMod(loader.Module):
    """Module for playing with dice, heads/tails and other games."""

    strings = {
        "name": "Randomizer",
        "invalid_number": "🚫 <b>Invalid number! Please choose a number between 1 and 6.</b>",
        "rolled": "🎲 <b>Rolled the cube, got:</b> <code>{}</code>",
        "win": "🎉 <b>Congratulations! You guessed it right!</b>",
        "lose": "😞 <b>Sorry, you didn't guess it right. Try again!</b>",
        "invalid_monetka": "🚫 <b>Invalid choice! Please choose 'Heads' or 'Tails'.</b>",
        "flipping": "🔄 <b>Flipping the coin...</b>",
        "flipped": "🪙 <b>Coin flipped, it's:</b> <code>{}</code>",
        "cfg_Number_Min": "Minimum number to be drawn",
        "cfg_Number_Max": "Maximum number rolled",
        "rnumber": "<emoji document_id=5285372392086976148>🦋</emoji>  <b>The number dropped</b>", 
        "error_min": "<emoji document_id=5287611315588707430>❌</emoji> <b>Error: Value is less than the minimum number from the configuration.</b>",       
        "error_max": "<emoji document_id=5287611315588707430>❌</emoji> <b>Error: Value is greater than the maximum number from the configuration.",
        "invalid_rnumber": "🚫 <b>The number is specified incorrectly or is not a number.</b>",
    }

    strings_ru = {
        "invalid_number": "🚫<b>Указано неверное число! Пожалуйста выберите число от 1 до 6.</b>",
        "rolled": "🎲<b>Подробсил кубик и получил:</b> <code>{}</code>",
        "win": "🎉<b>Поздравляем! Вы выйграли</b>",
        "lose": "😞<b>Вы проиграли, вы загадали неверное число. Попробуйте ещё раз!</b>",
        "invalid_monetka": "🚫<b>Неверный выбор! Пожалуйста выберите 'орёл' или 'решка'</b>",
        "flipping": "🔄<b>Подрбасываю монетку...</b>",
        "flipped": "🪙<b>Монетка подброшена, выпало:</b> <code>{}</code>",
        "cfg_Number_Min": "Минимальное число в выпадении",
        "cfg_Number_Max": "Максимальное число в выпадении",
        "rnumber": "<emoji document_id=5285372392086976148>🦋</emoji>  <b>Выпало число</b>",
        "error_min": "<emoji document_id=5287611315588707430>❌</emoji> <b>Error: Значение меньше минимального числа из конфигурации.</b>",
        "error_max": "<emoji document_id=5287611315588707430>❌</emoji> <b>Error: Значение больше максимального числа из конфигурации.</b>",
        "invalid_rnumber": "🚫 <b>Число указано неправильно или не является им.</b>",
    }

    strings_uz = {
        "invalid_number": "🚫<b>Noto'g'ri raqam kiritildi! Iltimos, 1 dan 6 gacha bo'lgan bir raqam tanlang.</b>",
        "rolled": "🎲<b>Zar ni chiqarib oldi:</b> <code>{}</code>",
        "win": "🎉<b>Tabriklaymiz! Siz yutdingiz</b>",
        "lose": "😞<b>Siz yo'qotdingiz, siz noto'g'ri raqam o'yladiz. Qaytadan urinib ko'ring!</b>",
        "invalid_monetka": "🚫<b>Noto'g'ri tanlov! Iltimos, 'to'g' va 'yuqori' tanlang</b>",
        "flipping": "🔄<b>Yig'ishni zarba shaklida qilmoqda...</b>",
        "flipped": "🪙<b>Zarba qilindi, natija:</b> <code>{}</code>",
        "cfg_Number_Min": "Chiqqan eng kichik raqam",
        "cfg_Number_Max": "Chiqqan eng katta raqam",
        "rnumber": "<emoji document_id=5285372392086976148>🦋</emoji>  <b>Chiqqan raqam</b>",
        "error_min": "<emoji document_id=5287611315588707430>❌</emoji> <b>Error: Qiymat sozlamadan minimal sonidan kichik.</b>",
        "error_max": "<emoji document_id=5287611315588707430>❌</emoji> <b>Error: Qiymat sozlamadan maksimal sonidan katta.</b>",
        "invalid_rnumber": "🚫 <b>Raqam noto'g'ri kiritilgan yoki u raqam emas.</b>",
    }

    strings_de = {
        "invalid_number": "🚫<b>Ungültige Zahl angegeben! Bitte wählen Sie eine Zahl zwischen 1 und 6.</b>",
        "rolled": "🎲<b>Der Würfel wurde geworfen und ergab:</b> <code>{}</code>",
        "win": "🎉<b>Herzlichen Glückwunsch! Sie haben gewonnen</b>",
        "lose": "😞<b>Sie haben verloren, Sie haben eine falsche Zahl erraten. Versuchen Sie es erneut!</b>",
        "invalid_monetka": "🚫<b>Falsche Auswahl! Bitte wählen Sie 'Kopf' oder 'Zahl'</b>",
        "flipping": "🔄<b>Die Münze wird geworfen...</b>",
        "flipped": "🪙<b>Die Münze wurde geworfen, das Ergebnis ist:</b> <code>{}</code>",
        "cfg_Number_Min": "Mindestanzahl beim Wurf",
        "cfg_Number_Max": "Maximale Anzahl beim Wurf",
        "rnumber": "<emoji document_id=5285372392086976148>🦋</emoji>  <b>Die Zahl ist gefallen</b>",
        "error_min": "<emoji document_id=5287611315588707430>❌</emoji> <b>Error: Wert ist kleiner als die minimale Zahl in der Konfiguration.</b>",
        "error_max": "<emoji document_id=5287611315588707430>❌</emoji> <b>Error: Wert ist größer als die maximale Zahl in der Konfiguration.</b>",
        "invalid_rnumber": "🚫 <b>Die Zahl ist falsch angegeben oder keine Zahl.</b>",
    }

    strings_es = {
        "invalid_number": "🚫<b>¡Número invalido especificado! Por favor elige un número entre 1 y 6.</b>",
        "rolled": "🎲<b>El dado fue lanzado y obtuvo:</b> <code>{}</code>",
        "win": "🎉<b>¡Felicidades! Has ganado</b>",
        "lose": "😞<b>Has perdido, has adivinado un número incorrecto. ¡Inténtalo de nuevo!</b>",
        "invalid_monetka": "🚫<b>¡Selección no válida! Por favor elige 'cara' o 'cruz'</b>",
        "flipping": "🔄<b>Lanzando la moneda...</b>",
        "flipped": "🪙<b>La moneda ha sido lanzada, el resultado es:</b> <code>{}</code>",
        "cfg_Number_Min": "Número mínimo en la caída",
        "cfg_Number_Max": "Número máximo en la caída",
        "rnumber": "<emoji document_id=5285372392086976148>🦋</emoji>  <b>El número ha caído</b>",
        "error_min": "<emoji document_id=5287611315588707430>❌</emoji> <b>Error: El valor es menor que el número mínimo de la configuración.</b>",
        "error_max": "<emoji document_id=5287611315588707430>❌</emoji> <b>Error: El valor es mayor que el número máximo de la configuración.</b>",
        "invalid_rnumber": "🚫 <b>El número está especificado incorrectamente o no es un número.</b>",
    }


    def __init__(self):
        self.config = loader.ModuleConfig(
        loader.ConfigValue(
                "Number_Min",
                0,
                lambda: self.strings["cfg_Number_Min"],
                validator=loader.validators.Integer(),
               ),
        loader.ConfigValue(
                "Number_Max",
                10,
                lambda: self.strings["cfg_Number_Max"],
                validator=loader.validators.Integer(),
               ),
        )

    @loader.command(
        ru_doc="[0-6] - Бросить кубик с числом",
        uz_doc="[0-6] - Son bilan zar tashlash",
        de_doc="[0-6] - Würfeln mit einer Zahl",
        es_doc="[0-6] - Tirar un dado con un número",
    )
    async def cube(self, message: Message):
        """[0-6] - Roll a dice with a number"""
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

    @loader.command(
        ru_doc="[орёл/решка] - Подбрасывает монетку, и выдает случайный результат",
        uz_doc="[орёл/решка] - Chiqqan va tasodifiy natijani ko'rsatadi",
        de_doc="[орёл/решка] - Wirft eine Münze und gibt ein zufälliges Ergebnis aus",
        es_doc="[орёл/решка] - Voltea una moneda y da un resultado aleatorio",
    )
    async def monetka(self, message: Message):
        """[орёл/решка] - Flips a coin and gives a random result"""
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

    @loader.command(
        ru_doc="[number] - Случайное число",
        uz_doc="[number] - Tasodifiy raqam",
        de_doc="[number] - Zufallszahl",
        es_doc="[number] - Número aleatorio", 
    )
    async def rnum(self, message: Message):
        """[number] - Random number"""
        args = utils.get_args_raw(message)
        min_number = min(self.config["Number_Min"], self.config["Number_Max"])
        max_number = max(self.config["Number_Min"], self.config["Number_Max"])
    
        try:
            number_guess = int(args)
        except ValueError:
            await utils.answer(message, self.strings("invalid_rnumber"))
            return

        if number_guess < min_number:
            await utils.answer(message, self.strings["error_min"])
            return
        elif number_guess > max_number:
            await utils.answer(message, self.strings("error_max"))
            return
    
        Number = random.randint(min_number, max_number)
        result = Number
        await utils.answer(message, f"{self.strings('rnumber')}: {result}")

        if number_guess == result:
            await asyncio.sleep(1.3)
            await utils.answer(message, self.strings("win"))
