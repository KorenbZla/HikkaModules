# Name: AuroraSpam
# Author: Felix?
# Commands:
# .aspam
# scope: hikka_only
# meta developer: @AuroraModules

__version__ = (1, 1, 6)

import asyncio
from .. import loader, utils
from telethon.tl.types import Message

@loader.tds
class AuroraSpamMod(loader.Module):
    """Module for mailings message"""

    strings = {
        "name": "AuroraSpam",
        "successfully_spam": "<emoji document_id=5823396554345549784>✔️</emoji> <b><i>The newsletter has been successfully completed, all messages have been delivered.</i></b>",
        "error_cfg_group_id": "<emoji document_id=5778527486270770928>❌</emoji>Error! The config value was entered incorrectly or it does not exist.",
        "cfg_group_id": "Enter the group identifier in the format СhatId , СhatId",
        "cfg_custom_text": "Enter a custom text for the mailing",
        "cfg_photo_url": "Enter a link to send media with text.",
        }

    strings_ru = {
        "successfully_spam": "<emoji document_id=5823396554345549784>✔️</emoji> <b><i>Рассылка успешно завершена, все сообщения были доставлены.</i></b>",
        "error_cfg_group_id": "<emoji document_id=5778527486270770928>❌</emoji>Error! Неправильно введено значение конфига или его не существует.",
        "cfg_group_id": "Введите индификатор группы в формате СhatID , ChatID",
        "cfg_custom_text": "Введите кастомный текст для рассылки",
        "cfg_photo_url": "Введите ссылку для отправки медиа с текстом.",
    }

    strings_uz = {
        "successfully_spam": "<emoji document_id=5823396554345549784>✔️</emoji> <b><i>Yuborish muvaffaqiyatli yakunlandi, barcha xabarlarni yetkazib berildi.</i></b>",
        "error_cfg_group_id": "<emoji document_id=5778527486270770928>❌</emoji>Error! Konfiguratsiya qiymati noto'g'ri yoki mavjud emas.",
        "cfg_group_id": "Guruh identifikatorini ChatID, ChatID formatida kiriting",
        "cfg_custom_text": "Yuborish uchun maxsus matnni kiriting",
        "cfg_photo_url": "Matnli media yuborish uchun havolani kiriting.",
    }

    strings_de = {
        "successfully_spam": "<emoji document_id=5823396554345549784>✔️</emoji> <b><i>Die Verteilung wurde erfolgreich abgeschlossen, alle Nachrichten wurden zugestellt.</i></b>",
        "error_cfg_group_id": "<emoji document_id=5778527486270770928>❌</emoji>Error! Falscher oder nicht vorhandener Konfigurationswert.",
        "cfg_group_id": "Geben Sie die Gruppenkennung im Format ChatID, ChatID ein",
        "cfg_custom_text": "Geben Sie den benutzerdefinierten Text für die Verteilung ein",
        "cfg_photo_url": "Geben Sie einen Link ein, um Medien mit Text zu senden.",
    }

    strings_es = {
        "successfully_spam": "<emoji document_id=5823396554345549784>✔️</emoji> <b><i>La distribución se ha completado con éxito, todos los mensajes han sido entregados.</i></b>",
        "error_cfg_group_id": "<emoji document_id=5778527486270770928>❌</emoji>Error! Valor de configuración incorrecto o inexistente",
        "cfg_group_id": "Ingrese el identificador del grupo en formato ChatID, ChatID",
        "cfg_custom_text": "Ingrese el texto personalizado para la distribución",
        "cfg_photo_url": "Enter the ",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "group_id",
                None,
                lambda: self.strings["cfg_group_id"],
                validator=loader.validators.Series(
                    validator=loader.validators.Union(
                        loader.validators.TelegramID(),
                        loader.validators.RegExp("[0-9]"),
                    ),
                ),
            ),
            loader.ConfigValue(
                "custom_text",
                "The module was created by @AuroraModules",
                lambda: self.strings["cfg_custom_text"],
            ),
            loader.ConfigValue(
                "photo_url",
                None,
                lambda: self.strings("cfg_photo_url"),
                validator=loader.validators.Link(),
            ),
        )

    @loader.command(
        ru_doc="Начать рассылку сообщений.",
        uz_doc="Xabarlarni yuborishni boshlang.",
        de_doc="Starten Sie den Versand von Nachrichten.",
        es_doc="Empezar a enviar mensajes.",
    )
    async def aspamcmd(self, message: Message):
        """Start sending messages."""
        ccid = self.config["group_id"]
        text = self.config["custom_text"]
        photo = self.config["photo_url"]
        sp = self.strings["successfully_spam"]
    
        if ccid is None or ccid == []:
            await utils.answer(message, self.strings["error_cfg_group_id"])  
            return

        for i in ccid:
            if self.config["photo_url"] == None:
                await self.client.send_message(i, text)
            else:
                await self.client.send_file(
                    i,
                    photo,
                    caption=text,
                )
        await utils.answer(message, sp)
        await asyncio.sleep(6)
        await message.delete()
