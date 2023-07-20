import os
import shutil
import asyncio
import warnings

import bot

warnings.simplefilter("ignore")
VOICE_DIR = "./voice/"


async def main():
    try:
        os.makedirs(VOICE_DIR, exist_ok=True)
        await bot.run()
    finally:
        shutil.rmtree(VOICE_DIR)


if __name__ == "__main__":
    asyncio.run(main())
