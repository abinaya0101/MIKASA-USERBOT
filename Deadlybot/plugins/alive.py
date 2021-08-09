# credit goes to @D3_krish and @official_sameer

from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *


#-------------------------------------------------------------------------------

DEADLY_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
DEADLY_CAPTION = "🔥 ℓєgєи∂яу αf Dєα∂ly Bσт 🔥\n\n"
DEADLY_CAPTION += (
    f"                __↼🄼🄰🅂🅃🄴🅁⇀__\n  **『 {Config.YOUR_NAME} 』**\n\n"
)
DEADLY_CAPTION += f"╔══════════════════╗\n"
DEADLY_CAPTION += f"╠•➳➠ `𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽:` `{tel_ver}` \n"
DEADLY_CAPTION += f"╠•➳➠ `𝚅𝙴𝚁𝚂𝙸𝙾𝙽:` `{deadly_ver}`\n"
DEADLY_CAPTION += f"╠•➳➠ `𝙶𝚁𝙾𝚄𝙿:`  [𝙹𝙾𝙸𝙽](t.me/DEADLY_USERBOT)\n"
DEADLY_CAPTION += f"╠•➳➠ `𝙲𝙷𝙰𝙽𝙽𝙴𝙻:` [𝙹𝙾𝙸𝙽](t.me/deadly_techy)\n"
DEADLY_CAPTION += f"╠•➳➠ `𝙲𝚁𝙴𝙰𝚃𝙾𝚁:` [⚡𝚂𝙰𝙼𝙴𝙴𝚁⚡](https://t.me/official_sameer)\n"
DEADLY_CAPTION += f"╠•➳➠ `𝙾𝚆𝙽𝙴𝚁:` [⚡𝙳𝙰𝙽𝙸𝚂𝙷 𝙾𝙿⚡](https://t.me/idanishbaba)\n"
DEADLY_CAPTION += f"╚══════════════════╝\n\n"
DEADLY_CAPTION += " [✨𝚁𝙴𝙿𝙾✨](https://github.com/DEADLY-FIGHTERS/DEADLY-BOT) 🔹 [📜𝙻𝙸𝙲𝙴𝙽𝚂𝙴📜](https://github.com/DEADLY-FIGHTERS/DEADLY-BOT/blob/main/LICENSE)"
                            
                                      
#-------------------------------------------------------------------------------

# for Deadlybot
# ONLY for Deadlybot
# EDITED BY - @SAMEER_795 (SAMEER )
# KANGERS STAY AWAY
# JISNE KANG KIYA USKI MA CHOD DI JAYEGI
# BHADWE KANG MT KR LENA ...
# TERI MA KI CHUT KANGER
# CHL AGAR KANG HI KRNA HE TO CREDIT KE SATH KR


import time

from userbot import StartTime
from Deadlybot.utils import admin_cmd, edit_or_reply, sudo_cmd

ludosudo = Config.SUDO

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = Config.YOUR_NAME or "Deadly User"
DEADLY_PIC = Config.ALIVE_PIC

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"
                         

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="deadly$"))
@bot.on(sudo_cmd(pattern="deadly$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if DEADLY_PIC:
        deadly_caption = f"**{Config.ALIVE_MSG}**\n\n"
        deadly_caption += f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n"                
        deadly_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
        deadly_caption += f"┣•➳➠ `Tᴇʟᴇᴛʜᴏɴ:` `{tel_ver}` \n"
        deadly_caption += f"┣•➳➠ `Vᴇʀsɪᴏɴ:` `{deadly_ver}`\n"
        deadly_caption += f"┣•➳➠ `𝙰𝙱𝚄𝚂𝙴:` `{abuse_m}`\n"
        deadly_caption += f"┣•➳➠ `Sᴜᴅᴏ:` `{is_sudo}`\n"
        deadly_caption += f"┣•➳➠ `Cʜᴀɴɴᴇʟ:` [Jᴏɪɴ](Config.YOUR_CHANNEL)\n"
        deadly_caption += f"┣•➳➠ `Gʀᴏᴜᴘ:` [Jᴏɪɴ](Config.YOUR_GROUP)\n"
        deadly_caption += f"┣•➳➠ `Uᴘᴛɪᴍᴇ:`{uptime}`\n"
        deadly_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
        await alive.client.send_file(
            alive.chat_id, DEADLY_IMG, caption=deadly_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"┏━━━━━━━━━━━━━━━━━━━\n"
            f"┣•➳➠ `𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽:` `1.23.0` \n"
            f"┣•➳➠ `𝚅𝙴𝚁𝚂𝙸𝙾𝙽:` `0.2`\n"
            f"┣•➳➠ `𝙰𝙱𝚄𝚂𝙴:` `Config.ABUSE`\n"
            f"┣•➳➠ `Sᴜᴅᴏ:` `{is_sudo}`\n"
            f"┣•➳➠ `𝙲𝙷𝙰𝙽𝙽𝙴𝙻:` [ᴊᴏɪɴ](Config.YOUR_CHANNEL)\n"
            f"┣•➳➠ `𝙶𝚁𝙾𝚄𝙿:` [ᴊᴏɪɴ](Config.YOUR_GROUP)\n"
            f"┣•➳➠ `𝚄𝙿𝚃𝙸𝙼𝙴:`{uptime}\n`"
            f"┗━━━━━━━━━━━━━━━━━━━\n"
        )
                
CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "deadly", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
