# credit goes to @D3_krish and @official_sameer

from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *


#-------------------------------------------------------------------------------

MIKASA_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
MIKASA_CAPTION = "  __**🔥🔥 𝐌𝐈𝐊𝐀𝐒𝐀 𝐁𝐎𝐓 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄 🔥🔥**__\n\n"

MIKASA_CAPTION += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
MIKASA_CAPTION += (
    f"                __↼🄼🄰🅂🅃🄴🅁⇀__\n  **『 {Config.YOUR_NAME} 』**\n\n"
)
MIKASA_CAPTION += f"╔══════════════════╗\n"
MIKASA_CAPTION += f"╠•➳➠ `𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽:` `{tel_ver}` \n"
MIKASA_CAPTION += f"╠•➳➠ `𝚅𝙴𝚁𝚂𝙸𝙾𝙽:` `{mikasa_ver}`\n"
MIKASA_CAPTION += f"╠•➳➠ `𝙶𝚁𝙾𝚄𝙿:`  [𝙹𝙾𝙸𝙽](t.me/mikasa_bot_support)\n"
MIKASA_CAPTION += f"╠•➳➠ `𝙲𝙷𝙰𝙽𝙽𝙴𝙻:` [𝙹𝙾𝙸𝙽](t.me/mikasa_bot_op)\n"
MIKASA_CAPTION += f"╠•➳➠ `𝙲𝚁𝙴𝙰𝚃𝙾𝚁:` [𝚃𝙴𝙰𝙼 𝙼𝙸𝙺𝙰𝚂𝙰](https://t.me/)\n"
MIKASA_CAPTION += f"╚══════════════════╝\n\n"
MIKASA_CAPTION += " [⚡𝚁𝙴𝙿𝙾⚡](https://github.com/TEAM-MIKASA/MIKASA-BOt) 🔹 [📜𝙻𝙸𝙲𝙴𝙽𝚂𝙴📜](https://github.com/TEAM-MIKASA/MIKASA-BOt/blob/main/LICENSE)"
                            
                         
#-------------------------------------------------------------------------------

@bot.on(mikasa_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(mikasa):
    if mikasa.fwd_from:
        return
    await mikasa.get_chat()
    await mikasa.delete()
    await bot.send_file(mikasa.chat_id, MIKASA_PIC, caption=MIKASA_CAPTION)
    await mikasa.delete()

msg = f"""
{Config.ALIVE_MSG}**\n\n"
≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n"                
**┏━━━━━━━━━━━━━━━━━━━\n"
**┣•➳➠ `Tᴇʟᴇᴛʜᴏɴ:` `1.21.2` \n"
**┣•➳➠ `Vᴇʀsɪᴏɴ:` `{mikasa_ver}`\n"
**┣•➳➠ `Sᴜᴅᴏ:` `{is_sudo}`\n"
**┣•➳➠ `Cʜᴀɴɴᴇʟ:` [Jᴏɪɴ](https://t.me/Mikasa_bot_op)\n"
**┣•➳➠ `Gʀᴏᴜᴘ:` [Jᴏɪɴ](https://t.me/Mikasa_bot_support)\n"
**┣•➳➠ `Uᴘᴛɪᴍᴇ:`{uptime}`\n"
**┗━━━━━━━━━━━━━━━━━━━\n"
       
"""
botname = Config.BOT_USERNAME

@bot.on(mikasa_cmd(pattern="mikasa$"))
@bot.on(sudo_cmd(pattern="mikasa$", allow_sudo=True))
async def mikasa_a(event):
    try:                
        mikasa = await bot.inline_query(botname, "mikasa")
        await mikasa[0].click(event.chat_id)
        if event.sender_id == officialsameer:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "mikasa", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
