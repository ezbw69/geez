"""
if you can read this, this meant you use code from Geez | Ram Project
this code is from somewhere else
please dont hestitate to steal it
because Geez and Ram doesn't care about credit
at least we are know as well
who Geez and Ram is


kopas repo dan hapus credit, ga akan jadikan lu seorang developer

YANG NYOLONG REPO INI TRUS DIJUAL JADI PREM, LU GAY...
©2023 Geez | Ram Team
"""
import asyncio
from asyncio import gather
from random import choice
from pyrogram import Client, enums
from pyrogram.types import Message
from geezlibs.geez.helper import edit_or_reply, ReplyCheck
from geezlibs import DEVS, BL_GCAST
from geezlibs.geez import geez
from Geez.modules.basic import add_command_help
from Geez import cmds

caption = f"**UPLOADED BY** 𝗛𝗘𝗥𝗢𝗜𝗡𝗙𝗔𝗧𝗛𝗘𝗥🕷"

@geez("asupan", cmds)
async def asupan(client: Client, message: Message):
    if message.chat.id in BL_GCAST:
        return await edit_or_reply(message, "**Tidak bisa di gunakan di Group Support**")
    gz = await edit_or_reply(message, "`mencari asupan...`")
    await gather(
        gz.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "punyakenkan", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@geez("bokep", cmds)
async def asupin(client: Client, message: Message):
    if message.chat.id in BL_GCAST:
        return await edit_or_reply(message, "**Tidak bisa di gunakan di Group Support**")
    gz = await edit_or_reply(message, "`Mencari bahan...`")
    await gather(
        gz.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "bahaninimah", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )

@geez("ayang", cmds)
async def ayang(client, message):
    yanto = await message.reply("🔎 `Search Ayang...`")
    pop = message.from_user.first_name
    ah = message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "CeweLogoPack", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Ayangnya [{pop}](tg://user?id={ah}) 💝",
    )

    await yanto.delete()

@geez("ppcp", cmds)
async def ppcp(client, message):
    yanto = await message.reply("🔎 `Search PP Couple...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "ppcpcilik", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Couple nya Nih Kak",
    )

    await yanto.delete()

@geez("ppanime", cmds)
async def ppanime(client, message):
    yanto = await message.reply("🔎 `Search PP Anime...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "animehikarixa", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Anime nya Nih Kak",
    )

    await yanto.delete()


add_command_help(
    "asupan",[
        [f"{cmds}asupan", "Asupan video TikTok",],
        [f"{cmds}ayang", "Mencari Foto ayang kamu /nNote: Modul ini buat cwo yang jomblo."],
        [f"{cmds}ppcp", "Mencari Foto PP Couple Random."],
        [f"{cmds}bokep", "to send random porno videos."],
        [f"{cmds}ppanime", "Mencari Foto PP Couple Anime."],
    ],
)
