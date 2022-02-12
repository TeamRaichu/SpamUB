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


@Sex.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex2.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex3.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex4.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex5.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex6.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex7.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex8.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex9.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex10.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex11.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex12.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex13.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex14.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex15.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex16.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex17.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex18.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex19.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex20.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex21.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex22.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex23.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex24.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex25.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex26.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex27.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex28.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex29.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex30.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex31.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex32.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex33.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex34.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex35.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex36.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex37.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex38.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex39.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
@Sex40.on(events.NewMessage(incoming=True, pattern=r"\%scall(?: |$)(.*)" % hl))
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
