# Mehmet babanin müzik botları prjosi
# EfsaneStar - MehmetBaba06 - SohbetSkyfall 

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Merhaba 👋! Telegram Gruplarının sesli sohbetlerinde müzik çalabiliyorum. Sizi şaşırtacak pek çok harika özelliğim var!\n\n🔴 Telegram gruplarınızın sesli sohbetlerinizde müzik çalmamı ister misiniz? ? Beni nasıl kullanabileceğinizi öğrenmek için lütfen aşağıdaki /help \'Kullanım Kılavuzu👤\' düğmesini tıklayın.\n\n🔴 Grubunuzun sesli sohbetinde müzik çalabilmek için Asistanın grubunuzda olması gerekir.\n\n🔴 [Kullanıcı Kılavuzu] (https://telegra.ph/GENEL-KOMUTLAR-05-10) bahsedilen daha fazla bilgi ve komutlar\n\nA @EfsaneStar tarafından hazırlanan bir projeyim "" " ,
      """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Kurucu Sahip 👨‍💻", url="https://t.me/EfsaneStar"
                  ],[
                    InlineKeyboardButton(
                        "Yardımcı Sahip 👨‍💻", url="https://t.me/EfsaneStar"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Kanal Mp3 🎧", url="https://t.me/kanalEfsanestar"
                    )
              ],[ 
                    InlineKeyboardButton(
                        "Sohbet Grup 🇹🇷", url="https://t.me/sohbetskyfall"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔴 Müzik çalar yayında**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🚨 Support Kanal 🚨", url="https://t.me/sohbetlobisi")
                ]
            ]
        )
   )

