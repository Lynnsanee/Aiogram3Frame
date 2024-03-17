import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types

import credentials

TOKEN = credentials.bot_token

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(TOKEN)


@dp.message()
async def message_handler(message: types.Message) -> None:
    """
    """


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())