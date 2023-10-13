import importlib
import time
from pyrogram import idle
from uvloop import install
from geezlibs import logging, BOT_VER, __version__ as gver
from Geez import LOGGER, LOOP, aiosession, bot1, bots, app, ids
from config import CMD_HNDLR, BOTLOG_CHATID
from Geez.modules import ALL_MODULES
from Geez.modules.basic.heroku import geez_log
from geezlibs.geez.utils.geezlogs import izzy_meira, geezlog

MSG_ON = """
**𝗛𝗘𝗥𝗢𝗜𝗡𝗙𝗔𝗧𝗛𝗘𝗥🕷**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
**Userbot Version -** `{}`
**𝗛𝗘𝗥𝗢 Library Version - `{}`**
**Ketik** `{}hero` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""

async def main():
    await app.start()
    LOGGER("Geez").info("Loading Everything.")
    for all_module in ALL_MODULES:
        importlib.import_module("Geez.modules" + all_module)
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await logging(bot)
            await geez_log()
            group = await izzy_meira(bot)
            try:
                await bot.send_message(group.id, MSG_ON.format(BOT_VER, gver, CMD_HNDLR))
            except BaseException as a:
                LOGGER("Geez").warning(f"{a}")
            LOGGER("Geez").info("Startup Completed")
            LOGGER("Geez").info(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            LOGGER("Geez").info(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Geez").info("Starting 𝗛𝗘𝗥𝗢𝗜𝗡𝗙𝗔𝗧𝗛𝗘𝗥")
    install()
    LOOP.run_until_complete(main())
