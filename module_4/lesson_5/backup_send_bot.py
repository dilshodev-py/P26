import asyncio
import logging
import os
import sys
from os import getenv
from os.path import join

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import InputFile, FSInputFile
from pkg_resources import AvailableDistributions

TOKEN = "7507461491:AAF8fnCzU9YTABItpIx3HIqw1JHsXIVQhfc"

my_id = 1148477816
dp = Dispatcher()
path = '/home/dilshod/PycharmProjects/P26/module_4/lesson_5/backups'
file_name = os.listdir(path)[-1]

async def send_doc(bot : Bot):
    file = FSInputFile(join(path , "13-09-2024-08-41-33.tar") , "backupfile.tar")
    await bot.send_document(chat_id=my_id , document=file)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await send_doc(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())