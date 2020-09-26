import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**Crevil Is ALive!** \n`🇮🇳BOT Status : ` **☣Hot**\n\n"
                     f"`My Master`: {DEFAULTUSER}\n\n"
                     "`Telethon version:` **6.0.9**\n`Python:` **3.7.4**\n"
                     "`Database Status:` **conected...**\n\n`I am Working Fine! Sir\n`"
                     "**Bot Creator:** [CrevilBot](t.me/crevil)\n"
                     "     [🇮🇳Deploy This crevilbot🇮🇳](https://github.com/crevils/crevilbot)") 

