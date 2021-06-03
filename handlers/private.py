from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""Merhaba 👋! Telegram Gruplarının sesli sohbetlerinde müzik çalabiliyorum. Sizi şaşırtacak pek çok harika özelliğim var!\n\n🔴 Telegram gruplarınızın sesli sohbetlerinizde müzik çalmamı ister misiniz? ? Beni nasıl kullanabileceğinizi öğrenmek için lütfen aşağıdaki /help \' düğmesini tıklayın.\n\n🔴 Grubunuzun sesli sohbetinde müzik çalabilmek için Asistanın grubunuzda olması gerekir.\n\n🔴 bahsedilen daha fazla bilgi ve komutlar versiyon 3.2.8\n\n@EfsaneStar Tarafından hazırlanan ve tasarlanan bir projeyim "" " ,
      """B
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Kurucu Sahip 👨‍💻", url="https://t.me/EfsaneStar"
                  ],[
                    InlineKeyboardButton(
                        "Yardımcı Sahip 👨‍💻", url="https://t.me/Mehmentt_12"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Kanal Mp3 🎧", url="https://t.me/kanalEfsanestar"
                    )
              ],[ 
                    InlineKeyboardButton(
                        "Sohbet Grup 💬", url="https://t.me/sohbetskyfall"
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
                        "🎛️ Support Kanal 🎛️", url="https://t.me/sohbetlobisi")
                ]
            ]
        )
   )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Merhabalar {message.from_user.first_name}!
💠 /oynat <song name> - istediğiniz şarkıyı çal
💠 /ytp <youtuden direk müzik bulur ve oynatır. 
💠 /bul <song name> - istediğiniz şarkıları hızlı bir şekilde indirin
💠 /arama <query> - youtube'da ayrıntıları içeren videoları arama
💠 /jsbul <saavn> - üzenden parçayı bulur. 
💠 /vindir 📩 Çalan parçayı youtube üzerinden vdeo olarak indirir. 

\n*Yalnızca yöneticiler*
💠 /durdur - şarkı çalmayı duraklatma
💠 /devam - şarkı çalmaya devam et
💠 /atla - sonraki şarkıyı çal
💠 /bitir - müzik çalmayı durdurma
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📣 Kanal", url="https://t.me/sohbetlobisi"
                    ),
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/skyfallsohbet"
                    )
                ]
            ]
        )
    )    
