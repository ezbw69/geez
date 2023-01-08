from pyrogram import filters, Client
from pyrogram import Client as gez
import asyncio
from pyrogram.types import Message 

from pyrogram.methods import messages
from geez.database.mongodb.pmpermitdb import get_approved_users, pm_guard
import geez.database.mongodb.pmpermitdb as geez
from config import BOTLOG_CHATID, PM_LOGGER
FLOOD_CTRL = 0
ALLOWED = []
USERS_AND_WARNS = {}


async def denied_users(filter, client: Client, message: Message):
    if not await pm_guard():
        return False
    if message.chat.id in (await get_approved_users()):
        return False
    else:
        return True

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


@gez.on_message(filters.command("setlimit", ["."]) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**Apaan ya?**")
        return
    await geez.set_limit(int(arg))
    await message.edit(f"**Limit Di Set {arg}**")



@gez.on_message(filters.command("setblockmsg", ["."]) & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**Lah apaan tuh ?**")
        return
    if arg == "default":
        await geez.set_block_message(geez.BLOCKED)
        await message.edit("**Block Anajay **.")
        return
    await geez.set_block_message(f"`{arg}`")
    await message.edit("**Custom block message set**")


@gez.on_message(filters.command(["ok", "setuju", "a"], ["."]) & filters.me & filters.private)
async def allow(client, message):
    chat_id = message.chat.id
    pmpermit, pm_message, limit, block_message = await geez.get_pm_settings()
    await geez.allow_user(chat_id)
    await message.edit(f"**I have allowed [you](tg://user?id={chat_id}) to PM me.**")
    async for message in client.search_messages(
        chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
    ):
        await message.delete()
    USERS_AND_WARNS.update({chat_id: 0})


@gez.on_message(filters.command(["tolak", "no", "disa"], ["."]) & filters.me & filters.private)
async def deny(client, message):
    chat_id = message.chat.id
    await geez.deny_user(chat_id)
    await message.edit(f"**Udahan Cok [you](tg://user?id={chat_id}).**")


@gez.on_message(
    filters.private
    & filters.create(denied_users)
    & filters.incoming
    & ~filters.service
    & ~filters.me
    & ~filters.bot
)
async def reply_pm(app: Client, message):
    global FLOOD_CTRL
    pmpermit, pm_message, limit, block_message = await geez.get_pm_settings()
    user = message.from_user.id
    user_warns = 0 if user not in USERS_AND_WARNS else USERS_AND_WARNS[user]
    if PM_LOGGER:
        await app.send_message(PM_LOGGER, f"{message.text}")
    if user_warns <= limit - 2:
        user_warns += 1
        USERS_AND_WARNS.update({user: user_warns})
        if not FLOOD_CTRL > 0:
            FLOOD_CTRL += 1
        else:
            FLOOD_CTRL = 0
            return
        async for message in app.search_messages(
            chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
        ):
            await message.delete()
        await message.reply(pm_message, disable_web_page_preview=True)
        return
    await message.reply(block_message, disable_web_page_preview=True)
    await app.block_user(message.chat.id)
    USERS_AND_WARNS.update({user: 0})
