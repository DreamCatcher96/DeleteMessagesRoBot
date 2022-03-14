#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

""" credentials """

import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from bot.get_config import get_config


# apparently, no error appears even if the path does not exists
load_dotenv("config.env")


# The Telegram API things
# Get these values from my.telegram.org or Telegram: @useTGxBot
API_HASH = get_config("API_HASH", should_prompt=True)
APP_ID = int(get_config("APP_ID", should_prompt=True))
# get a token from @BotFather
TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", should_prompt=True)
# string session for running as user
TG_USER_SESSION = get_config("TG_USER_SESSION", should_prompt=True)
TG_BOT_SESSION = get_config("TG_BOT_SESSION", "bot")
# Number of update workers to use.
# 4 is the recommended (and default) amount,
# but your experience may vary.
# Note that going crazy with more workers
# wont necessarily speed up your bot,
# given the amount of sql data accesses,
# and the way python asynchronous calls work.
TG_BOT_WORKERS = int(get_config("TG_BOT_WORKERS", "4"))
# add an auto sleep time,
# in the Pyrogram Client
TG_SLEEP_THRESHOLD = int(get_config("TG_SLEEP_THRESHOLD", 10))
# path to store LOG files
LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "MessageDeletErBot.log")
# number of messages that can be deleted in One Request, in Telegram
TG_MAX_SEL_MESG = int(get_config("TG_MAX_SEL_MESG", 99))
TG_MIN_SEL_MESG = int(get_config("TG_MIN_SEL_MESG", 0))
# a dictionary to store the currently running processes
AKTIFPERINTAH = {}
# should the user / bot leave the chat after finishing tasks
SHTL_USR_HCAT_QO = bool(get_config("SHTL_USR_HCAT_QO", False))
SHTL_BOT_HCAT_QO = bool(get_config("SHTL_BOT_HCAT_QO", False))


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)


REQD_PERMISSIONS = "https://te.legra.ph/file/924cb1c25094dd1d41238.jpg"
GIT_REPO_LINK = "@OTTHelpBot"
""" strings to be used in the bot """
START_MESSAGE = get_config("START_MESSAGE", (
    "<b>Hai 👋 I'm A Bot That Can Delete All Your Channel Or SuperGroup Messages 😍</b>"
    "\n\n"
    "<b>To Use Me ⚠️ :</b>"
    "\n\n"
    "<b>1⃣ Add Me To The Channel / SuperGroup As Admin (With Atleast Delete Message , Add User's/Invite User's & Add New Admins Permissions)</b>"
    "\n\n"
    "<b>2⃣ Send <code>/delall</code> if You Want All The Messages To Be Deleted.</b>"
    "\n\n"
    "<b>3⃣ Ifu Want Delete Selected Messages ? Reply The Beginning Message <code>/delfrom</code> , Reply The End Message <code>/delto</code> , Finally Send <code>/seldel</code> then U can See Deleting all You Selected Messages 😁</b>"
    "\n\n"
    "<b>Check Permission : <a href='https://te.legra.ph/file/924cb1c25094dd1d41238.jpg'> CLICK HERE</a></b>"
    "\n\n"
    f"<b>Contact Admin : {GIT_REPO_LINK}</b>"
))
START_COMMAND = get_config("START_COMMAND", "start")
DEL_ALL_COMMAND = get_config("DEL_ALL_COMMAND", "delall")
BEGINNING_DEL_ALL_MESSAGE = get_config("BEGINNING_DEL_ALL_MESSAGE", (
    "<b>Trying to Delete All Messages 🗑️</b>"
))
IN_CORRECT_PERMISSIONS_MESSAGE = get_config("IN_CORRECT_PERMISSIONS_MESSAGE", (
    "<b>Something Went Wrong 🤔</b> \n\n"
    "<code>{}</code>"
    "\n\n"
    f"<b>Please Verify <a href='{REQD_PERMISSIONS}'> All Permissions Is Correct</a>, "
    "<b>And Try Again After Sometime.</b>"
))
SEL_DEL_COMMAND = get_config("SEL_DEL_COMMAND", "seldel")
BEGINNING_SEL_DEL_MESSAGE = get_config("BEGINNING_SEL_DEL_MESSAGE", (
    "<b>🔄 Trying to Delete Your Selected Messages 🗑️</b>"
))
DEL_FROM_COMMAND = get_config("DEL_FROM_COMMAND", "delfrom")
DEL_TO_COMMAND = get_config("DEL_TO_COMMAND", "delto")
NOT_USED_DEL_FROM_DEL_TO_MESSAGE = get_config(
    "NOT_USED_DEL_FROM_DEL_TO_MESSAGE", (
        f"<b>Please Use /{DEL_FROM_COMMAND} or /{DEL_TO_COMMAND}</b>"
        f"<b>Before Using /{SEL_DEL_COMMAND}</b>"
    )
)
THANK_YOU_MESSAGE = get_config(
    "THANK_YOU_MESSAGE", (
        "<b>Thank You for Using Me 😍 \n\nSey Thanks My Boss : @WhitE_DeviL09</b>"
    )
)
TL_FILE_TYPES = (
    "photo",
    "animation",
    "audio",
    "document",
    "video",
    "video_note",
    "voice",
    # "contact",
    # "dice",
    # "poll",
    # "location",
    # "venue",
    "sticker",
    "text"
)
