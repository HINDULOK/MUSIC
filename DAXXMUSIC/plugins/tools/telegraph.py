from telegraph import upload_file
from pyrogram import filters
from DAXXMUSIC import app
from pyrogram.types import InputMediaPhoto


@app.on_message(filters.command(["tgm" , "telegraph"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("𝐌ᴀᴋᴇɪɴɢ 𝐀 𝐋ɪɴᴋ...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://files.catbox.moe" + x

        i.edit(f'Yᴏᴜʀ ʟɪɴᴋ sᴜᴄᴄᴇssғᴜʟ Gᴇɴ {url}  ᴘʀᴏᴅᴜᴄᴇᴅ 🥀 ʙʏ @HINDULOK_CHATTING_CLUB')

########____________________________________________________________######

@app.on_message(filters.command(["graph" , "grf"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("𝐌𝙰𝙺𝙴ɪɴɢ 𝐀 𝐋𝙸𝙽𝙺...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://files.catbox.moe" + x

        i.edit(f'Yᴏᴜʀ ʟɪɴᴋ sᴜᴄᴄᴇssғᴜʟ Gᴇɴ {url}  ᴘʀᴏᴅᴜᴄᴇᴅ 🥀 ʙʏ @HINDULOK_OFFICIAL')
