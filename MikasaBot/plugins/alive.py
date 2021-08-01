# credit goes to @D3_krish 
from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

mikasa_pic = Config.ALIVE_PIC or "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
pm_caption = "  __**🔥🔥𝐌𝐈𝐊𝐀𝐒𝐀 𝐁𝐎𝐓 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄 🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 ↼𝗠𝗔𝗦𝗧𝗘𝗥⇀\n  **『 {mikasa_mention} 』**\n\n"
)
pm_caption += f"╔══════════════════╗\n"
pm_caption += f"╠•➳➠ `𝖳𝖾𝗅𝖾𝗍𝗁𝗈𝗇:` `{tel_ver}` \n"
pm_caption += f"╠•➳➠ `𝖵𝖾𝗋𝗌𝗂𝗈𝗇:` `{mikasa_ver}`\n"
pm_caption += f"╠•➳➠ `𝖲𝗎𝖽𝗈:` `{is_sudo}`\n"
pm_caption += f"╠•➳➠ `𝖢𝗁𝖺𝗇𝗇𝖾𝗅:` {chnl_link}\n"
pm_caption += f"╠•➳➠ `𝖢𝗋𝖾𝖺𝗍𝗈𝗋:` [𝙼𝙸𝙺𝙰𝚂𝙰](https://t.me/)\n"
pm_caption += f"╚══════════════════╝\n"
pm_caption += " [⚡REPO⚡](https://github.com/TEAM-MIKASA/MIKASA-BOt) 🔹 [📜License📜](https://github.com/TEAM-MIKASA/MIKASA-BOt/blob/main/LICENSE)"
                            

#-------------------------------------------------------------------------------

@bot.on(mikasa_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(mikasa):
    if mikasa.fwd_from:
        return
    await mikasa.get_chat()
    await mikasa.delete()
    await bot.send_file(mikasa.chat_id, mikasa_pic, caption=mikasa_caption)
    await mikasa.delete()

msg = f"""
**⚡ 𝐌𝐈𝐊𝐀𝐒𝐀 𝐈𝐒 𝐎𝐍𝐋𝐈𝐍𝐄 ⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**╔══════════════════╗**
**╠➳➠ 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 :**  `{tel_ver}`
**╠➳➠ 𝐌𝐈𝐊𝐀𝐒𝐀 :**  **{mikasa_ver}**
**╠➳➠ 𝐔𝐩𝐭𝐢𝐦𝐞   :**  `{uptime}`
**╠➳➠ 𝐀𝐛𝐮𝐬𝐞    :**  **{abuse_m}**
**╠➳➠ 𝐒𝐮𝐝𝐨      :**  **{is_sudo}**
**╚══════════════════╝
"""
botname = Config.BOT_USERNAME

@bot.on(mikasa_cmd(pattern="mikasa$"))
@bot.on(sudo_cmd(pattern="mikasa$", allow_sudo=True))
async def mikasa_a(event):
    try:                
        mikasa = await bot.inline_query(botname, "mikasa")
        await mikasa[0].click(event.chat_id)
        if event.sender_id == official_sameer:
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
