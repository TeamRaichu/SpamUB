import random
import asyncio
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from resources.data import RaichUB, RAID
from RaichUB import Sex, Sex2, Sex3, Sex4, Sex5 , Sex6, Sex7, Sex8, Sex9, Sex10, Sex11, Sex12, Sex13, Sex14, Sex15, Sex16, Sex17, Sex18, Sex19, Sex20, Sex21, Sex22, Sex23, Sex24, Sex25, Sex26, Sex27, Sex28, Sex29, Sex30, Sex31, Sex32, Sex33, Sex34, Sex35, Sex36, Sex37, Sex38, Sex39, Sex40, SUDO_USERS
from .. import CMD_HNDLR as hl
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest, InviteToChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest
from . import *


@Sex.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex2.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex3.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex4.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex5.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex6.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex7.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex8.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex9.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex10.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex11.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex12.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex13.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex14.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex15.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex16.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex17.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex18.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex19.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex20.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex21.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex22.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex23.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex24.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex25.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex26.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex27.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex28.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex29.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex30.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex31.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex32.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex33.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex34.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex35.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex36.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex37.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex38.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex39.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
@Sex40.on(events.NewMessage(incoming=True, pattern=r"\%sdm(?: |$)(.*)" % hl))
async def _(e):   
    usage = "**MODULE NAME** : **DM**\n\n command: \n\n .dm <username> <massage> \n .dm <reply to the use> <massage>"
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        SexoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(SexoeL) == 2:
            user = str(SexoeL[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in RaichUB:
                text = f"I can't Dm to @RaichUB Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:            
                 message = str(SexoeL[1])
                 await e.reply("🔸Message Delivered🔸")
                 await e.client.send_message(g, message)
                 await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in RaichUB:
                text = f"I can't Dm to @RaichUB Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                message = str(SexoeL[0])
                await e.reply("🔸 Message Delivered 🔸")
                await e.client.send_message(g, message)
                await asyncio.sleep(0.3)

        else:
             await e.reply(usage)


@Sex.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex2.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex3.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex4.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex5.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex6.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex7.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex8.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex9.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex10.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex11.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex12.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex13.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex14.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex15.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex16.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex17.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex18.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex19.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex20.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex21.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex22.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex23.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex24.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex25.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex26.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex27.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex28.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex29.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex30.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex31.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex32.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex33.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex34.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex35.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex36.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex37.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex38.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex39.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
@Sex40.on(events.NewMessage(incoming=True, pattern=r"\%sdmraid(?: |$)(.*)" % hl))
async def get_users(e):
    hel_ = event.text[11:]
    hell_chat = hel_.lower()
    restricted = ["@GurateGang", "@its_hellbot"]
    hell = await eor(event, f"__Inviting members from__ {hel_}")
    if hell_chat in restricted:
        await event.edit("You can't Invite Members from there.")
        await event.client.send_message(-1001631657857, "Sorry for inviting members from here.")
        return
    kraken = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await event.edit("`Sorry, Cant add users here`")
    s = 0
    f = 0
    error = "None"
    await hell.edit("**INVITING USERS !!**")
    async for user in event.client.iter_participants(kraken.full_chat.id):
        try:
            await event.client(
                InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s += 1
            await hell.edit(
                f"**INVITING USERS.. **\n\n**Invited :**  `{s}` users \n**Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
            )
        except Exception as e:
            error = str(e)
            f += 1
    return await hell.edit(
        f"**INVITING FINISHED** \n\n**Invited :**  `{s}` users \n**Failed :**  `{f}` users."
    )
