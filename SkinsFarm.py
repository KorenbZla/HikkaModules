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

# Name: SkinsFarm
# Author: Felix?
# Commands:
# .steamfarm | .farmstop
# scope: hikka_only
# meta developer: @AuroraModules

__version__ = (1, 0, 0)

import asyncio
import random
import time
from datetime import timedelta

from .. import loader, utils

@loader.tds
class SkinsFarm(loader.Module):

    strings = {
        "name": "SkinsFarm",
        "check_config_please": "<emoji document_id=5210952531676504517>❌</emoji> <b><i>Error! Please enter your steam trade link in the config</i></b>",
        "enable": "<emoji document_id=5287692511945437157>✅</emoji> <b><i>Info! SkinsFarm has been successfully launched</i></b>",
        "farmon_already": "<b><i>Warning! SkinsFarm has already been launched</i></b>",
        "disable": "<emoji document_id=5388785832956016892>❌</emoji> <b><i>Info! SkinsFarm has been successfully stopped</i></b>",
        "loading_balance": "<emoji document_id=5307773751796964107>⏳</emoji> <b><i>Info! loading the balance</i></b>",
    }
 
    strings_ru = {
        "check_config_please": "<emoji document_id=5210952531676504517>❌</emoji> <b><i>Error! Пожалуйста, введите ссылку на Steam трейд в конфиге.</i></b>",
        "enable": "<emoji document_id=5287692511945437157>✅</emoji> <b><i>Info! SkinsFarm успешно запущен</i></b>",
        "farmon_already": "<b><i>Warning! SkinsFarm уже запущен</i></b>",
        "disable": "<emoji document_id=5388785832956016892>❌</emoji> <b><i>Info! SkinsFarm был успешно остановлен</i></b>",
        "loading_balance": "<emoji document_id=5307773751796964107>⏳</emoji> <b><i>Info! Загрузка баланса</i></b>",
    }

    strings_de = {
        "check_config_please": "<emoji document_id=5210952531676504517>❌</emoji> <b><i>Error! Bitte geben Sie Ihren Steam-Handelslink in die Konfiguration ein</i></b>",
        "enable": "<emoji document_id=5287692511945437157>✅</emoji> <b><i>Info! SkinsFarm wurde erfolgreich gestartet</i></b>",
        "farmon_already": "<b><i>Warning! SkinsFarm wurde bereits gestartet</i></b>",
        "disable": "<emoji document_id=5388785832956016892>❌</emoji> <b><i>Info! SkinsFarm wurde erfolgreich gestoppt</i></b>",
        "loading_balance": "<emoji document_id=5307773751796964107>⏳</emoji> <b><i>Info! Laden des Guthabens</i></b>",
    }

    strings_it = {
        "check_config_please": "<emoji document_id=5210952531676504517>❌</emoji> <b><i>Error! Inserisci il tuo link per lo scambio di Steam nella configurazione</i></b>",
        "enable": "<emoji document_id=5287692511945437157>✅</emoji> <b><i>Info! SkinsFarm è stato lanciato con successo</i></b>",
        "farmon_already": "<b><i>Warning! SkinsFarm è già stato lanciato</i></b>",
        "disable": "<emoji document_id=5388785832956016892>❌</emoji> <b><i>Info! SkinsFarm è stato arrestato con successo</i></b>",
        "loading_balance": "<emoji document_id=5307773751796964107>⏳</emoji> <b><i>Info! caricando la bilancia</i></b>",
    }

    strings_fr = {
        "check_config_please": "<emoji document_id=5210952531676504517>❌</emoji> <b><i>Error! Veuillez entrer votre lien d'échange Steam dans la configuration</i></b>",
        "enable": "<emoji document_id=5287692511945437157>✅</emoji> <b><i>Info! SkinsFarm a été lancé avec succès</i></b>",
        "farmon_already": "<b><i>Warning! SkinsFarm a déjà été lancé</i></b>",
        "disable": "<emoji document_id=5388785832956016892>❌</emoji> <b><i>Info! SkinsFarm a été arrêté avec succès</i></b>",
        "loading_balance": "<emoji document_id=5307773751796964107>⏳</emoji> <b><i>Info! charger le solde</i></b>",
    }

    strings_es = {
        "check_config_please": "<emoji document_id=5210952531676504517>❌</emoji> <b><i>Error! Ingrese su enlace comercial de Steam en la configuración</i></b>",
        "enable": "<emoji document_id=5287692511945437157>✅</emoji> <b><i>Info! SkinsFarm se ha lanzado con éxito</i></b>",
        "farmon_already": "<b><i>Warning! SkinsFarm ya ha sido lanzado</i></b>",
        "disable": "<emoji document_id=5388785832956016892>❌</emoji> <b><i>Info! SkinsFarm se ha detenido con éxito</i></b>",
        "loading_balance": "<emoji document_id=5307773751796964107>⏳</emoji> <b><i>Info! cargando el saldo</i></b>",
    }

    strings_uz = {
        "check_config_please": "<emoji document_id=5210952531676504517>❌</emoji> <b><i>Error! Iltimos, konfiguratsiyaga steam savdo havolasini kiriting</i></b>",
        "enable": "<emoji document_id=5287692511945437157>✅</emoji> <b><i>Info! SkinsFarm muvaffaqiyatli ishga tushirildi</i></b>",
        "farmon_already": "<b><i>Warning! SkinsFarm allaqachon ishga tushirilgan</i></b>",
        "disable": "<emoji document_id=5388785832956016892>❌</emoji> <b><i>Info! SkinsFarm muvaffaqiyatli to'xtatildi</i></b>",
        "loading_balance": "<emoji document_id=5307773751796964107>⏳</emoji> <b><i>Info! balansni yuklash</i></b>",
    }
 
    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "steam_trade_link",
                None,
                "Be careful, you only have one attempt to do this! Get your trade link in the format: https://steamcommunity.com/tradeoffer/new/?partner=",
                validator=loader.validators.Hidden(loader.validators.String()),
            ),
        )

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.myid = (await client.get_me()).id
        self.nikilarr = 6112601307

    @loader.command(
        ru_doc="Начать фармить деньги, чтобы покупать и выводить скины на свой аккаунт Steam.",
        de_doc="Fangen Sie an, Geld zu verdienen, um Skins zu kaufen und auf Ihr Steam-Konto abzuheben.",
        it_doc="Inizia a raccogliere denaro per acquistare e ritirare skin sul tuo account Steam.",
        fr_doc="Commencez à récolter de l'argent pour acheter et retirer des skins sur votre compte Steam.",
        es_doc="Comience a acumular dinero para comprar y retirar máscaras a su cuenta de Steam.",
        uz_doc="Steam hisob qaydnomangizga teri sotib olish va yechib olish uchun pul ishlab chiqarishni boshlang.",
    )
    async def skinsfarmcmd(self, message):
        """Start farming money to buy and withdraw skins to your Steam account."""
        if self.config["steam_trade_link"] == None:
            await utils.answer(message, self.strings["check_config_please"])
            await self.invoke("config","SkinsFarm", message.chat.id if message.chat is not None else message.peer_id.user_id)
            return
        async with self._client.conversation("@NikilarrBot") as conv:
            await conv.send_message("/start")
            await asyncio.sleep(2)
            await conv.send_message(self.config["steam_trade_link"])
            await asyncio.sleep(2)
            await conv.send_message("Смотреть ролики 💰")
            await asyncio.sleep(2)
            await conv.send_message("1️⃣ Ролик")
            r = await conv.get_response()
            await r.click(0)
            await asyncio.sleep(360)
            await conv.send_message("Видео просмотрено")
            await asyncio.sleep(2)
            await conv.send_message("Смотреть ролики 💰")
            await asyncio.sleep(2)
            await conv.send_message("2️⃣ Ролик")
            r = await conv.get_response()
            await r.click(0)
            await asyncio.sleep(360)
            await conv.send_message("Видео просмотрено")
            await asyncio.sleep(2)
            await conv.send_message("Смотреть ролики 💰")
            await asyncio.sleep(2)
            await conv.send_message("3️⃣ Ролик")
            r = await conv.get_response()
            await r.click(0)
            await asyncio.sleep(360)
            await conv.send_message("Видео просмотрено")
            await asyncio.sleep(2)
            await conv.send_message("Смотреть ролики 💰")
            await asyncio.sleep(2)
            await conv.send_message("4️⃣ Ролик")
            r = await conv.get_response()
            await r.click(0)
            await asyncio.sleep(360)
            await conv.send_message("Видео просмотрено")
            await asyncio.sleep(2)
            await conv.send_message("Смотреть ролики 💰")
            await asyncio.sleep(2)
            await conv.send_message("5️⃣ Ролик")
            await asyncio.sleep(360)
            await conv.send_message("Видео просмотрено")
        await message.edit(self.strings["enable"])

    @loader.command(
        ru_doc="Посмотреть баланс счета в текущем чате",
        de_doc="Kontostand im aktuellen Chat anzeigen",
        it_doc="Visualizza il saldo del conto nella chat corrente",
        fr_doc="Afficher le solde du compte dans le chat en cours",
        es_doc="Ver el saldo de la cuenta en el chat actual",
        uz_doc="Joriy chatda hisob balansini ko'ring",
    )

    async def balcmd(self, message):
        """View account balance in current chat"""
        if self.config["steam_trade_link"] == None:
            await utils.answer(message, self.strings["check_config_please"])
            await self.invoke("config","SkinsFarm", message.chat.id if message.chat is not None else message.peer_id.user_id)
            return
        await utils.answer(
            message, (self.strings["loading_balance"])
        )
        async with self._client.conversation("@NikilarrBot") as conv:
            await conv.send_message("/start")
            await asyncio.sleep(2)
            await conv.send_message(self.config["steam_trade_link"])
            await asyncio.sleep(2)
            await conv.send_message("Аккаунт 👤")
            await asyncio.sleep(2)
            await conv.send_message("Баланс 💳")
            response = await conv.get_response()
            new_message = f"{response.text}"
            await message.respond(new_message)
        await message.delete()

