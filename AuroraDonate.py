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

# Name: AuroraDonate
# Author: Felix?
# Commands:
# .dme
# scope: hikka_only
# meta developer: @AuroraModules

# meta pic: https://i.postimg.cc/Hx3Zm8rB/logo.png
# meta banner: https://te.legra.ph/file/d3f0f14e90ce2f82d8f1f.jpg

__version__ = (1, 2, 1)

from hikkatl.types import Message # type: ignore
from .. import loader, utils

@loader.tds
class AuroraDonateMod(loader.Module):
    """Module for creating a message with your details for donations"""
    
    strings = {
        "name": "AuroraDonate",
        "cfg_custom_text": "Enter the custom message to be sent with your donation details.",
        "cfg_hide_text": "Enter the text that will be sent when using the '-h' argument to show hidden or private credentials.",
        "cfg_banner_url": "Enter the URL of the image to be sent with your donation details.",
        "cfg_CryptoBot": "Enter the URL to your multi-account in @CryptoBot.",
        "cfg_xRocket": "Enter the URL to your multi-account in @xRocket.",
    }

    strings_ru = {
        "cfg_custom_text": "Введите кастомное сообщение, которое будет отправляться с вашими реквизитами для донатов.",
        "cfg_hide_text": "Введите текст, который будет отправляться при аргументе '-h', чтобы показать скрытые или приватные реквизиты.",
        "cfg_banner_url": "Введите ссылку на изображение, которое будет отправляться с вашими реквизитами для донатов.",
        "cfg_CryptoBot": "Введите ссылку на мультисчет в @CryptoBot.",
        "cfg_xRocket": "Введите ссылку на мультисчет в @xRocket.",
    }

    strings_uz = {
        "cfg_custom_text": "Donat qilish uchun ma'lumotlaringiz bilan yuboriladigan maxsus xabarni kiriting.",
        "cfg_hide_text": "Yashirin yoki shaxsiy ma’lumotlarni ko‘rsatish uchun '-h' argumenti ishlatilganda yuboriladigan matnni kiriting.",
        "cfg_banner_url": "Donat qilish uchun ma'lumotlaringiz bilan yuboriladigan rasm havolasini kiriting.",
        "cfg_CryptoBot": "@CryptoBot dagi multischet havolasini kiriting.",
        "cfg_xRocket": "@xRocket dagi multischet havolasini kiriting.",
    }

    strings_de = {
        "cfg_custom_text": "Geben Sie eine benutzerdefinierte Nachricht ein, die mit Ihren Spendeninformationen gesendet wird.",
        "cfg_hide_text": "Geben Sie den Text ein, der beim Argument '-h' gesendet wird, um versteckte oder private Zugangsdaten anzuzeigen.",
        "cfg_banner_url": "Geben Sie den Link zu einem Bild ein, das mit Ihren Spendeninformationen gesendet wird.",
        "cfg_CryptoBot": "Geben Sie den Link zu Ihrem Multikonto bei @CryptoBot ein.",
        "cfg_xRocket": "Geben Sie den Link zu Ihrem Multikonto bei @xRocket ein.",
    }

    strings_es = {
        "cfg_custom_text": "Ingrese un mensaje personalizado que se enviará con sus detalles de donación.",
        "cfg_hide_text": "Introduce el texto que se enviará al usar el argumento '-h' para mostrar credenciales ocultas o privadas.",
        "cfg_banner_url": "Ingrese el enlace de la imagen que se enviará con sus detalles de donación.",
        "cfg_CryptoBot": "Ingrese el enlace a su cuenta múltiple en @CryptoBot.",
        "cfg_xRocket": "Ingrese el enlace a su cuenta múltiple en @xRocket.",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "custom_text",
                "<b><i>Created by: @AuroraModules</i></b>",
                lambda: self.strings["cfg_custom_text"],
            ),
            loader.ConfigValue(
                "hide_text",
                None,
                lambda: self.strings["cfg_hide_text"],
            ),
            loader.ConfigValue(
                "banner_url",
                "https://te.legra.ph/file/a596292807cc71508b7db.jpg",
                lambda: self.strings["cfg_banner_url"],
                validator=loader.validators.Link(),
            ),
            loader.ConfigValue(
                "CryptoBot",
                None,
                lambda: self.strings["cfg_CryptoBot"],
                validator=loader.validators.Link(),
            ),
            loader.ConfigValue(
                "xRocket",
                None,
                lambda: self.strings["cfg_xRocket"],
                validator=loader.validators.Link(),
            ),
        )

    @loader.command(
        ru_doc="{-h} - Открыть реквизиты для донатов",
        uz_doc="{-h} - Donatlar uchun ma'lumotlarni ochish",
        de_doc="{-h} - Details für Spenden öffnen",
        es_doc="{-h} - Abrir detalles para donaciones",
    )
    async def dme(self, message):
        """{-h} - Open details for donations"""
        
        args = utils.get_args_raw(message).split()
        
        CryptoBot = self.config["CryptoBot"]
        xRocket = self.config["xRocket"]
        banner_url = self.config["banner_url"]
        custom_text = self.config["custom_text"] 
        hide_text = self.config["hide_text"]

        if len(args) > 0 and args[0] == '-h':
            if hide_text == None:
                custom_text = custom_text
            else:
                custom_text = hide_text
        else:
            custom_text = custom_text
    
        if CryptoBot is None and xRocket is None:
            if banner_url is None:
                await utils.answer(message, custom_text)
            else:
                await self.client.send_file(
                    message.chat_id,
                    banner_url,
                    caption=custom_text
                )
                await message.delete()
        else:
            await self.inline.form(
                message=message,
                text=str(custom_text),
                photo=banner_url,
                reply_markup=[
                    [
                        {"text": "👛 CryptoBot", "url": CryptoBot},
                        {"text": "🚀 xRocket", "url": xRocket},
                    ],
                    [
                        {"text": "🔻 Закрыть", "callback": self.delete}  
                    ],
                ],
            )

    async def delete(self, call):
        await call.delete()
