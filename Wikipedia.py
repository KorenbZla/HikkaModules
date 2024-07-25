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

# Name: Wikipedia
# Author: dend1yya
# Commands:
# .wikiru | wikien
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/ee1bb476a643bb85b5723.jpg

version = (1, 0, 0)

import wikipedia # type: ignore
from .. import loader, utils

class WikipediaMod(loader.Module):
    """Search for information on Wikipedia"""

    strings = {
        "name": "Wikipedia",
        "EnterRequest": "<emoji document_id=5778527486270770928>❌</emoji> <b>Enter your search term on Wikipedia.</b>",
        "SResult": "<emoji document_id=5823396554345549784>✔️</emoji> <b>Wikipedia search result:</b>",
        "IncorrectRequest": "<emoji document_id=5285372392086976148>🦋</emoji> <b>Several possible options have been found. Specify your request:</b>",
        "NotFound": "<emoji document_id=5778527486270770928>❌</emoji> <b>Nothing was found for your query.</b>",
        "ErrorRequest": "<emoji document_id=5778527486270770928>❌</emoji> <b>An error occurred while executing the request:</b>",
    }

    strings_ru = {
        "EnterRequest": "<emoji document_id=5778527486270770928>❌</emoji> <b>Введите свой поисковый запрос на Википедии.</b>",
        "SResult": "<emoji document_id=5823396554345549784>✔️</emoji> <b>Результат поиска на Википедии:</b>",
        "IncorrectRequest": "<emoji document_id=5285372392086976148>🦋</emoji> <b>Было найдено несколько возможных вариантов. Уточните ваш запрос:</b>",
        "NotFound": "<emoji document_id=5778527486270770928>❌</emoji> <b>По вашему запросу ничего не найдено.</b>",
        "ErrorRequest": "<emoji document_id=5778527486270770928>❌</emoji> <b>При выполнении запроса произошла ошибка:</b>",
    }

    strings_uz = {
        "EnterRequest": "<emoji document_id=5778527486270770928>❌</emoji> <b>Vikipediya da qidirish so'zini kiriting.</b>",
        "SResult": "<emoji document_id=5823396554345549784>✔️</emoji> <b>Vikipediya qidiruv natijasi:</b>",
        "IncorrectRequest": "<emoji document_id=5285372392086976148>🦋</emoji> <b>Bir nechta mumkin variant topildi. So'rovingizni aniqlang:</b>",
        "NotFound": "<emoji document_id=5778527486270770928>❌</emoji> <b>Sizning so'rovingiz uchun hech narsa topilmadi.</b>",
        "ErrorRequest": "<emoji document_id=5778527486270770928>❌</emoji> <b>So'rovni bajarish jarayonida xatolik yuz berdi:</b>",
    }

    strings_de = {
        "EnterRequest": "<emoji document_id=5778527486270770928>❌</emoji> <b>Geben Sie Ihren Suchbegriff auf Wikipedia ein.</b>",
        "SResult": "<emoji document_id=5823396554345549784>✔️</emoji> <b>Wikipedia-Suchergebnis:</b>",
        "IncorrectRequest": "<emoji document_id=5285372392086976148>🦋</emoji> <b>Mehrere mögliche Optionen wurden gefunden. Präzisieren Sie Ihre Anfrage:</b>",
        "NotFound": "<emoji document_id=5778527486270770928>❌</emoji> <b>Für Ihre Anfrage wurde nichts gefunden.</b>",
        "ErrorRequest": "<emoji document_id=5778527486270770928>❌</emoji> <b>Beim Ausführen der Anfrage ist ein Fehler aufgetreten:</b>",
    }

    strings_es = {
        "EnterRequest": "<emoji document_id=5778527486270770928>❌</emoji> <b>Ingrese su término de búsqueda en Wikipedia.</b>",
        "SResult": "<emoji document_id=5823396554345549784>✔️</emoji> <b>Resultado de la búsqueda en Wikipedia:</b>",
        "IncorrectRequest": "<emoji document_id=5285372392086976148>🦋</emoji> <b>Se encontraron varias opciones posibles. Especifique su solicitud:</b>",
        "NotFound": "<emoji document_id=5778527486270770928>❌</emoji> <b>No se encontró nada para su consulta.</b>",
        "ErrorRequest": "<emoji document_id=5778527486270770928>❌</emoji> <b>Se produjo un error al ejecutar la solicitud:</b>",
    }

    @loader.command(
        ru_doc="[prompt] - Поиск материала в Википедии на русском языке.",
        uz_doc="[prompt] - Vikipediyada materialni rus tilida qidiring.",
        de_doc="[prompt] - Material in der Wikipedia auf Russisch suchen.",
        es_doc="[prompt] - Buscar material en Wikipedia en ruso.",
    )
    async def wikiru(self, message):
        """[prompt] - Search for material in Wikipedia in Russian."""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings['EnterRequest'])
            return

        try:
            wikipedia.set_lang("ru")
            _search_result = wikipedia.summary(args)
            await utils.answer(message, f"{self.strings_ru['SResult']}\n\n<i>{_search_result}</i>")
        except wikipedia.DisambiguationError as e:
            await utils.answer(message, f"{self.strings['IncorrectRequest']}\n{', '.join(e.options)}")
        except wikipedia.PageError:
            await utils.answer(message, self.strings['NotFound'])
        except Exception as e:
            await utils.answer(message, f"{self.strings['ErrorRequest']} {e}")

    @loader.command(
        ru_doc="[prompt] - Поиск материала в Википедии на английском языке.",
        uz_doc="[prompt] - Vikipediyada materialni ingliz tilida qidiring.",
        de_doc="[prompt] - Material in der Wikipedia auf Englisch suchen.",
        es_doc="[prompt] - Buscar material en Wikipedia en inglés.",
    )
    async def wikien(self, message):
        """[prompt] - Search for material in Wikipedia in English."""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings['EnterRequest'])
            return
        
        try:
            wikipedia.set_lang("en")
            _search_result = wikipedia.summary(args)
            await utils.answer(message, f"{self.strings['SResult']}\n\n{_search_result}")
        except wikipedia.DisambiguationError as e:
            await utils.answer(message, f"{self.strings['IncorrectRequest']}\n{', '.join(e.options)}")
        except wikipedia.PageError:
            await utils.answer(message, self.strings['NotFound'])
        except Exception as e:
            await utils.answer(message, f"{self.strings['ErrorRequest']} {e}</b>")
