# Name: RandomAvatars
# Author: Felix?
# Commands:
# .RandomNumber
# scope: hikka_only
# meta developer: @AuroraModules

__version__ = (1, 0, 1)

from telethon.tl.types import Message
from .. import loader, utils
import random

@loader.tds
class RandomNumberMod(loader.Module):
    """Генератор рандомных чисел"""
    strings = {
        "name": "RandomNumber",
        "rnumber": "<emoji document_id=5285372392086976148>🦋</emoji>  <b>The number dropped</b>",
        "cfg_Number_Min": "Minimum number to be drawn",
        "cfg_Number_Max": "Maximum number rolled", 
    }

    strings_ru = {
        "rnumber": "<emoji document_id=5285372392086976148>🦋</emoji>  <b>Выпало число</b>",
        "cfg_Number_Min": "Минимальное число в выпадении",
        "cfg_Number_Max": "Максимальное число в выпадении",
    }

    strings_uz = {
        "rnumber": "<emoji document_id=5285372392086976148>🦋</emoji>  <b>Chiqqan raqam</b>",
        "cfg_Number_Min": "Chiqqan eng kichik raqam",
        "cfg_Number_Max": "Chiqqan eng katta raqam",
    }

    strings_de = {
        "rnumber": "<emoji document_id=5285372392086976148>🦋</emoji>  <b>Die Zahl ist gefallen</b>",
        "cfg_Number_Min": "Mindestanzahl beim Wurf",
        "cfg_Number_Max": "Maximale Anzahl beim Wurf",
    }

    strings_es = {
        "rnumber": "<emoji document_id=5285372392086976148>🦋</emoji>  <b>El número ha caído</b>",
        "cfg_Number_Min": "Número mínimo en la caída",
        "cfg_Number_Max": "Número máximo en la caída",
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
                1000,
                lambda: self.strings["cfg_Number_Max"],
                validator=loader.validators.Integer(),
               ),
        )

    @loader.command(
        ru_doc="Случайное число",
        uz_doc="Tasodifiy raqam",
        de_doc="Zufallszahl",
        es_doc="Número aleatorio", 
    )
    async def RandomNumber(self, message: Message):
        """Random number"""
        min_number = min(self.config["Number_Min"], self.config["Number_Max"])
        max_number = max(self.config["Number_Min"], self.config["Number_Max"])
        Number = random.randint(min_number, max_number)
        result = Number
        await utils.answer(message, f"{self.strings('rnumber')}: {result}")
