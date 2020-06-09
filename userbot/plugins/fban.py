from telethon import events
import io
import asyncio
from uniborg.util import admin_cmd
from userbot import FBAN_USER, FBAN_REASON

USER = str(FBAN_USER) if FBAN_USER else "1198905023"
REASON = str(FBAN_REASON) if FBAN_REASON else "no reason given"
@borg.on(admin_cmd(pattern=r"fban"))

async def _(event):

    if event.fwd_from:

        return
    await borg.send_message("/start")
    await asyncio.sleep(2)
    await borg.send_message("/joinfed 70875a92-9b37-467e-abf1-a265d92221")
    await asyncio.sleep(2)
    await borg.send_message(f"/fban {USER} {REASON}")
    await asyncio.sleep(2)
