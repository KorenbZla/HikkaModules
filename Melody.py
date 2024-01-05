# Name: Melody
# Author: Felix?
# Commands:
# .mmoney | .mlipsiha
# scope: hikka_only
# meta developer: @AuroraModules


version = (1, 2, 1)


from .. import loader, utils
import asyncio

@loader.tds
class MelodyMod(loader.Module):
    """Поет песни Instasamka"""
    strings = {"name": "Melody"}

    async def mmoneycmd(self, message):
        """Песня «За деньги да»"""
        lyrics = [
              "Я вообще делаю что хочу",
              "Хочу импланты — звоню врачу",
              "Кто меня не любит — я вас не слышу",
              "Вы просто мне завидуете, я молчу",
              "Я не продаюсь, но за деньги — да",
              "Мой продюссер говорит я поп-звезда",
              "И кстати, мой продюссер — это мой муж, да",
              "Я не скажу в ответ ничего на вид",
              "И не скажу «привет» если бабок нет",
              "Слышу любимый звук — это звон монет",
              "Они тянут все мне руку, это мой концерт",
              "Не завожу подруг, но за деньги — да",
              "Я подумаю потом, но скажу сразу «да»",
              "За деньги, да, за деньги, да",
              "За деньги, да",
              "Деньги— Деньги— Деньги— Деньги— Да— Да— Да— Да—",
              "Играла песня «За деньги да»",
              ]
        for line in lyrics:
          #  message = await utils.answer(message, line)
          #
            await asyncio.sleep(3)
            await utils.answer(message, line)

    async def mlipsihacmd(self, message):
        """Песня «Липси ха»"""
        lyrics = [
              "Деньги пахнут pussy, а",
              "Сумка Birkin, только нал",
              "Стринги, а, стринги, а",
              "В стрингах ношу капитал",
              "Juicy пахнет money, ха",
              "Сучки в Juicy мои, ха",
              "Lipsi, ха, lipsi, ха",
              "Lipsi give me money, ха",
              "Mommy на dollar",
              "Жопа на сайте, cash",
              "Я на работе",
              "Трясу огромной ass",
              "Дайте мне money",
              "Money на money, мой Ken",
              "Пахну деньгами",
              "Пахну деньгами",
              "AMA bad bitch",
              "Lipsi give me money, ха",
              "AMA hot bitch",
              "В стрингах ношу капитал",
              "Bad, bad bitch",
              "Juicy пахнет money, ха",
              "Где мои money, bitch?",
              "Где мои money?",
              "AMA bad bitch",
              "Lipsi give me money, ха",
              "AMA hot bitch",
              "В стрингах ношу капитал",
              "Bad, bad bitch" 
              "Juicy пахнет money, ха",
              "Где мои money, bitch?",
              "Где мои money?",
              "Песня «LIPSI HA»"
              ]
        for line in lyrics:
          #  message = await utils.answer(message, line)
          #
            await asyncio.sleep(3)
            await utils.answer(message, line)
