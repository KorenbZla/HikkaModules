# *      _                             __  __           _       _
# *     / \  _   _ _ __ ___  _ __ __ _|  \/  | ___   __| |_   _| | ___  ___ 
# *    / _ \| | | | '__/ _ \| '__/ _` | |\/| |/ _ \ / _` | | | | |/ _ \/ __|
# *   / ___ \ |_| | | | (_) | | | (_| | |  | | (_) | (_| | |_| | |  __/\__ \
# *  /_/   \_\__,_|_|  \___/|_|  \__,_|_|  |_|\___/ \__,_|\__,_|_|\___||___/
# *
# *                          © Copyright 2026
# *
# *                      https://t.me/AuroraModules
# *
# * 🔒 Code is licensed under GNU AGPLv3
# * 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# * ⛔️ You CANNOT edit this file without direct permission from the author.
# * ⛔️ You CANNOT distribute this file if you have modified it without the direct permission of the author.

# Name: InvalidFiles
# Author: Felix?
# Commands:
# .CreateInvalidFile (cifile) | .FormatFiles (ffiles)
# scope: hikka_only
# meta developer: @AuroraModules

__version__ = (1, 0, 0)

import os
import re
import time
from .. import loader, utils  # type: ignore
from telethon.tl.types import Message  # type: ignore
from telethon.tl.functions.messages import EditMessageRequest  # type: ignore
from telethon.tl.types import InputMediaUploadedDocument, DocumentAttributeFilename  # type: ignore

@loader.tds
class InvalidFilesMod(loader.Module):
    """Module for creating corrupted (broken) files of any format."""


    strings = {
        "name": "InvalidFiles",
        "invalid_format": "<emoji document_id=5456307331644037599>❌</emoji> <b>Invalid size format.</b>",
        "max_size": "<emoji document_id=5456307331644037599>❌</emoji> <b>Maximum file size is 2GB</b>",
        "file_created": (
            "<emoji document_id=5458805056990119991>✅</emoji><b> File successfully created and sent.</b>\n\n"
            "<blockquote>"
            "<emoji document_id=5456625794879099391>👤</emoji> <b>File name:</b> <code>{}</code>\n"
            "<emoji document_id=5456569114195692172>⚖️</emoji> <b>Size:</b> <code>{}{}</code>\n"
            "<emoji document_id=5456591761558245861>⌛️</emoji> <b>Creation:</b> <code>{:.2f} sec.</code>\n"
            "<tg-emoji emoji-id=5456350521835163323>📤</tg-emoji> <b>Upload:</b> <code>{:.2f} sec.</code>"
            "</blockquote>"
        ),
        "invalid_args": (
            "<emoji document_id=5456307331644037599>❌</emoji><b> Invalid arguments</b>\n\n"
            "<b>Usage:</b> <code>{prefix}cifile &lt;name&gt; &lt;size&gt;</code>\n"
            "<b>Example:</b> <code>{prefix}cifile test.txt 3.4mb</code>\n\n"
            "<i>Supported: b, kb, mb, gb</i>"
        ),
        "creating": "<emoji document_id=5456591761558245861>⌛️</emoji> <b>Creating file...\n\n<i>*Large files may take a long time to upload.</i></b>",
        "error": "<emoji document_id=5456537889783452967>⚠️</emoji> <b>Error:</b>\n<i>{}</i>",
        "formats": (
            "<emoji document_id=5456367813373498016>📂</emoji> <b>Popular file extensions:</b>\n\n"
            "<b>📄 Documents:</b> <code>.txt .docx .pdf .rtf</code>\n"
            "<b>📊 Spreadsheets:</b> <code>.xlsx .csv</code>\n"
            "<b>📈 Presentations:</b> <code>.pptx</code>\n"
            "<b>🖼️ Images:</b> <code>.jpg .png .gif .bmp .webp</code>\n"
            "<b>🎵 Audio:</b> <code>.mp3 .wav .flac</code>\n"
            "<b>🎬 Video:</b> <code>.mp4 .mkv .avi</code>\n"
            "<b>📦 Archives:</b> <code>.zip .rar .7z</code>\n"
            "<b>💻 Code:</b> <code>.py .js .html .css .json</code>"
        ),
    }

    strings_ru = {
        "invalid_format": "<emoji document_id=5456307331644037599>❌</emoji> <b>Неверный формат размера.</b>",
        "max_size": "<emoji document_id=5456307331644037599>❌</emoji> <b>Максимальный размер файла — 2GB</b>",
        "file_created": (
            "<emoji document_id=5458805056990119991>✅</emoji><b> Файл успешно создан и отправлен.</b>\n\n"
            "<blockquote>"
            "<emoji document_id=5456625794879099391>👤</emoji> <b>Имя файла:</b> <code>{}</code>\n"
            "<emoji document_id=5456569114195692172>⚖️</emoji> <b>Размер:</b> <code>{}{}</code>\n"
            "<emoji document_id=5456591761558245861>⌛️</emoji> <b>Создание:</b> <code>{:.2f} сек.</code>\n"
            "<tg-emoji emoji-id=5456350521835163323>📤</tg-emoji> <b>Отправка:</b> <code>{:.2f} сек.</code>"
            "</blockquote>"
        ),
        "invalid_args": (
            "<emoji document_id=5456307331644037599>❌</emoji><b> Неверные аргументы</b>\n\n"
            "<b>Использование:</b> <code>{prefix}cifile &lt;имя&gt; &lt;размер&gt;</code>\n"
            "<b>Пример:</b> <code>{prefix}cifile test.txt 3.4mb</code>\n\n"
            "<i>Поддерживаются: b, kb, mb, gb</i>"
        ),
        "creating": "<emoji document_id=5456591761558245861>⌛️</emoji> <b>Создаю файл...\n\n<i>*Файлы большого размера могут долго загружаться.</i></b>",
        "error": "<emoji document_id=5456537889783452967>⚠️</emoji> <b>Ошибка:</b>\n<i>{}</i>",
        "formats": (
            "<emoji document_id=5456367813373498016>📂</emoji> <b>Популярные расширения файлов:</b>\n\n"
            "<b>📄 Документы:</b> <code>.txt .docx .pdf .rtf</code>\n"
            "<b>📊 Таблицы:</b> <code>.xlsx .csv</code>\n"
            "<b>📈 Презентации:</b> <code>.pptx</code>\n"
            "<b>🖼️ Изображения:</b> <code>.jpg .png .gif .bmp .webp</code>\n"
            "<b>🎵 Аудио:</b> <code>.mp3 .wav .flac</code>\n"
            "<b>🎬 Видео:</b> <code>.mp4 .mkv .avi</code>\n"
            "<b>📦 Архивы:</b> <code>.zip .rar .7z</code>\n"
            "<b>💻 Код:</b> <code>.py .js .html .css .json</code>"
        ),
    }

    strings_uz = {
        "invalid_format": "<emoji document_id=5456307331644037599>❌</emoji> <b>Hajm formati noto‘g‘ri.</b>",
        "max_size": "<emoji document_id=5456307331644037599>❌</emoji> <b>Maksimal fayl hajmi — 2GB</b>",
        "file_created": (
            "<emoji document_id=5458805056990119991>✅</emoji><b> Fayl muvaffaqiyatli yaratildi va yuborildi.</b>\n\n"
            "<blockquote>"
            "<emoji document_id=5456625794879099391>👤</emoji> <b>Fayl nomi:</b> <code>{}</code>\n"
            "<emoji document_id=5456569114195692172>⚖️</emoji> <b>Hajmi:</b> <code>{}{}</code>\n"
            "<emoji document_id=5456591761558245861>⌛️</emoji> <b>Yaratish:</b> <code>{:.2f} sek.</code>\n"
            "<tg-emoji emoji-id=5456350521835163323>📤</tg-emoji> <b>Yuborish:</b> <code>{:.2f} sek.</code>"
            "</blockquote>"
        ),
        "invalid_args": (
            "<emoji document_id=5456307331644037599>❌</emoji><b> Noto‘g‘ri argumentlar</b>\n\n"
            "<b>Foydalanish:</b> <code>{prefix}cifile &lt;nom&gt; &lt;hajm&gt;</code>\n"
            "<b>Misol:</b> <code>{prefix}cifile test.txt 3.4mb</code>\n\n"
            "<i>Qo‘llab-quvvatlanadi: b, kb, mb, gb</i>"
        ),
        "creating": "<emoji document_id=5456591761558245861>⌛️</emoji> <b>Fayl yaratilmoqda...\n\n<i>*Katta fayllar uzoq yuklanishi mumkin.</i></b>",
        "error": "<emoji document_id=5456537889783452967>⚠️</emoji> <b>Xatolik:</b>\n<i>{}</i>",
        "formats": (
            "<emoji document_id=5456367813373498016>📂</emoji> <b>Mashhur fayl kengaytmalari:</b>\n\n"
            "<b>📄 Hujjatlar:</b> <code>.txt .docx .pdf .rtf</code>\n"
            "<b>📊 Jadvallar:</b> <code>.xlsx .csv</code>\n"
            "<b>📈 Taqdimotlar:</b> <code>.pptx</code>\n"
            "<b>🖼️ Rasmlar:</b> <code>.jpg .png .gif .bmp .webp</code>\n"
            "<b>🎵 Audio:</b> <code>.mp3 .wav .flac</code>\n"
            "<b>🎬 Video:</b> <code>.mp4 .mkv .avi</code>\n"
            "<b>📦 Arxivlar:</b> <code>.zip .rar .7z</code>\n"
            "<b>💻 Kod:</b> <code>.py .js .html .css .json</code>"
        ),
    }


    strings_de = {
        "invalid_format": "<emoji document_id=5456307331644037599>❌</emoji> <b>Ungültiges Größenformat.</b>",
        "max_size": "<emoji document_id=5456307331644037599>❌</emoji> <b>Maximale Dateigröße — 2GB</b>",
        "file_created": (
            "<emoji document_id=5458805056990119991>✅</emoji><b> Datei erfolgreich erstellt und gesendet.</b>\n\n"
            "<blockquote>"
            "<emoji document_id=5456625794879099391>👤</emoji> <b>Dateiname:</b> <code>{}</code>\n"
            "<emoji document_id=5456569114195692172>⚖️</emoji> <b>Größe:</b> <code>{}{}</code>\n"
            "<emoji document_id=5456591761558245861>⌛️</emoji> <b>Erstellung:</b> <code>{:.2f} Sek.</code>\n"
            "<tg-emoji emoji-id=5456350521835163323>📤</tg-emoji> <b>Upload:</b> <code>{:.2f} Sek.</code>"
            "</blockquote>"
        ),
        "invalid_args": (
            "<emoji document_id=5456307331644037599>❌</emoji><b> Ungültige Argumente</b>\n\n"
            "<b>Verwendung:</b> <code>{prefix}cifile &lt;name&gt; &lt;größe&gt;</code>\n"
            "<b>Beispiel:</b> <code>{prefix}cifile test.txt 3.4mb</code>\n\n"
            "<i>Unterstützt: b, kb, mb, gb</i>"
        ),
        "creating": "<emoji document_id=5456591761558245861>⌛️</emoji> <b>Datei wird erstellt...\n\n<i>*Große Dateien können lange zum Hochladen brauchen.</i></b>",
        "error": "<emoji document_id=5456537889783452967>⚠️</emoji> <b>Fehler:</b>\n<i>{}</i>",
        "formats": (
            "<emoji document_id=5456367813373498016>📂</emoji> <b>Beliebte Dateiendungen:</b>\n\n"
            "<b>📄 Dokumente:</b> <code>.txt .docx .pdf .rtf</code>\n"
            "<b>📊 Tabellen:</b> <code>.xlsx .csv</code>\n"
            "<b>📈 Präsentationen:</b> <code>.pptx</code>\n"
            "<b>🖼️ Bilder:</b> <code>.jpg .png .gif .bmp .webp</code>\n"
            "<b>🎵 Audio:</b> <code>.mp3 .wav .flac</code>\n"
            "<b>🎬 Video:</b> <code>.mp4 .mkv .avi</code>\n"
            "<b>📦 Archive:</b> <code>.zip .rar .7z</code>\n"
            "<b>💻 Code:</b> <code>.py .js .html .css .json</code>"
        ),
    }


    strings_es = {
        "invalid_format": "<emoji document_id=5456307331644037599>❌</emoji> <b>Formato de tamaño inválido.</b>",
        "max_size": "<emoji document_id=5456307331644037599>❌</emoji> <b>El tamaño máximo del archivo es 2GB</b>",
        "file_created": (
            "<emoji document_id=5458805056990119991>✅</emoji><b> Archivo creado y enviado correctamente.</b>\n\n"
            "<blockquote>"
            "<emoji document_id=5456625794879099391>👤</emoji> <b>Nombre del archivo:</b> <code>{}</code>\n"
            "<emoji document_id=5456569114195692172>⚖️</emoji> <b>Tamaño:</b> <code>{}{}</code>\n"
            "<emoji document_id=5456591761558245861>⌛️</emoji> <b>Creación:</b> <code>{:.2f} seg.</code>\n"
            "<tg-emoji emoji-id=5456350521835163323>📤</tg-emoji> <b>Subida:</b> <code>{:.2f} seg.</code>"
            "</blockquote>"
        ),
        "invalid_args": (
            "<emoji document_id=5456307331644037599>❌</emoji><b> Argumentos inválidos</b>\n\n"
            "<b>Uso:</b> <code>{prefix}cifile &lt;nombre&gt; &lt;tamaño&gt;</code>\n"
            "<b>Ejemplo:</b> <code>{prefix}cifile test.txt 3.4mb</code>\n\n"
            "<i>Soportado: b, kb, mb, gb</i>"
        ),
        "creating": "<emoji document_id=5456591761558245861>⌛️</emoji> <b>Creando archivo...\n\n<i>*Los archivos grandes pueden tardar en subirse.</i></b>",
        "error": "<emoji document_id=5456537889783452967>⚠️</emoji> <b>Error:</b>\n<i>{}</i>",
        "formats": (
            "<emoji document_id=5456367813373498016>📂</emoji> <b>Extensiones de archivo populares:</b>\n\n"
            "<b>📄 Documentos:</b> <code>.txt .docx .pdf .rtf</code>\n"
            "<b>📊 Hojas de cálculo:</b> <code>.xlsx .csv</code>\n"
            "<b>📈 Presentaciones:</b> <code>.pptx</code>\n"
            "<b>🖼️ Imágenes:</b> <code>.jpg .png .gif .bmp .webp</code>\n"
            "<b>🎵 Audio:</b> <code>.mp3 .wav .flac</code>\n"
            "<b>🎬 Video:</b> <code>.mp4 .mkv .avi</code>\n"
            "<b>📦 Archivos:</b> <code>.zip .rar .7z</code>\n"
            "<b>💻 Código:</b> <code>.py .js .html .css .json</code>"
        ),
    }
    
    async def create_invalid_file(self, filename: str, size_str: str):
        match = re.fullmatch(r"(\d+(?:\.\d+)?)(b|kb|mb|gb)", size_str.lower())

        if not match:
            return False, self.strings["invalid_format"]

        multiplier = {
            "b": 1,
            "kb": 1024,
            "mb": 1024 ** 2,
            "gb": 1024 ** 3,
        }

        size_value = float(match.group(1))
        unit = match.group(2)
        total_bytes = int(size_value * multiplier[unit])

        if total_bytes > 2 * 1024 ** 3:
            return False, self.strings["max_size"]

        start_time = time.time()

        try:
            with open(filename, "wb") as f:
                remaining = total_bytes
                chunk = 5 * 1024 * 1024

                while remaining > 0:
                    write_size = min(chunk, remaining)
                    f.write(os.urandom(write_size))
                    remaining -= write_size

        except Exception as e:
            return False, self.strings["error"].format(e)

        elapsed = time.time() - start_time

        return True, (filename, size_value, unit, elapsed)
    
    @loader.command(
        ru_doc="<имя>.<формат> <размер> — создать битый файл",
        uz_doc="<fayl>.<format> <hajm> — buzilgan fayl yaratish",
        de_doc="<datei>.<format> <größe> — beschädigte Datei erstellen",
        es_doc="<archivo>.<formato> <tamaño> — crear archivo corrupto",
        alias="cifile"
    )
    async def CreateInvalidFile(self, message: Message):
        """<file>.<format> <size> - create corrupted file"""

        args = utils.get_args_raw(message).split()

        if len(args) != 2:
            await utils.answer(
                message,
                self.strings("invalid_args").format(prefix=self.get_prefix())
            )
            return

        filename, size_str = args

        status = await utils.answer(message, self.strings("creating"))

        success, data = await self.create_invalid_file(filename, size_str)

        if not success:
            await utils.answer(status, data)
            return

        filename, size_value, unit, create_time = data

        try:
            start_upload = time.time()

            uploaded = await self.client.upload_file(filename)

            upload_time = time.time() - start_upload

            media = InputMediaUploadedDocument(
                file=uploaded,
                mime_type="application/octet-stream",
                attributes=[DocumentAttributeFilename(file_name=filename)]
            )

            await self.client(EditMessageRequest(
                peer=message.chat_id,
                id=status.id,
                message="",
                media=media
            ))

            await utils.answer(
                status,
                self.strings["file_created"].format(
                    filename,
                    size_value,
                    unit,
                    create_time,
                    upload_time
                )
            )

        except Exception as e:
            await utils.answer(status, self.strings["error"].format(e))

        finally:
            if os.path.exists(filename):
                try:
                    os.remove(filename)
                except Exception:
                    pass

    @loader.command(
        ru_doc="— показать список популярных форматов(расширейний) файлов",
        uz_doc="— mashhur fayl formatlari (kengaytmalari) ro'yxatini ko'rsatish",
        de_doc="— eine Liste gängiger Dateiformate (Erweiterungen) anzeigen",
        es_doc="— mostrar una lista de formatos de archivo (extensiones) populares",
        alias="ffiles"
    )
    async def FormatFiles(self, message: Message):
        """— show a list of popular file formats (extensions)"""
        await utils.answer(message, self.strings('formats'))
