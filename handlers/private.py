from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Merhaba 👋🏻 {}!**\n\n **Telegram Gruplarının Sesli Sohbetlerinde Müzik Çalabilirim. Sizi şaşırtacak çok sayıda harika özelliklerim var! \n\n **Tıklayınız /Komutlar Daha Fazlası İçin @EfsaneStar Yardım için yanınızda ❤**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("➕ Grubunuza Ekle ➕", url="https://t.me/GroupMusicPlayBot?startgroup=true")
            ],[
            InlineKeyboardButton("💬 Group", url="https://t.me/sohbetskyfall"),
            InlineKeyboardButton("Channel 🔊", url="https://t.me/kanalEfsanestar")
            ],[
            InlineKeyboardButton("Tasarım 👨‍💻", url="https://t.me/Mehmett_12"),
            InlineKeyboardButton("Kurucu Sahip 👨‍💻", url="https://t.me/EfsaneStar")
            ]]
        ),
        disable_web_page_preview=True
    )

@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
          text="**Music Bot Is Online ✅**",
          reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/sohbetskyfall")
              ]]
          )
      )


@Client.on_message(filters.command(["Komutlar", "start@sohbetlobisi"]) & filters.private & ~filters.channel)
async def Komutlar(_, message: Message):
    await message.reply_text(
        text="""**Group Music Bot : Help Menu**

__× Önce Beni Grubunuza Ekleyin..
× Tüm izinlerinizle beni grubunuzda yönetici olarak tanıtın..__

**🏷 Ortak Komutlar.**

💠 `/oynat` - Song Name : __Youtube Üzerinden Oynatır__
💠 `/bul` - Song Name : __Şarkıyı YouTube'dan alın__
💠 `/arama` - YouTube Title : __(YouTube Arama Sorgusu'ni alıp Alın)__
💠 `/ytp` - __Parçayı youtubeden çalar__
**🏷 Grup Yöneticisi Komutları.**

💠 `/atla` : __Müziği Atlar__
💠 `/durdur` : __Müzik Çalmayı Duraklat__
💠 `/devam` : __Müzik çalmayı devam ettir__ 
💠 `/bitir` : __Müzik çalmayı durdurur__
💠 `/jsbul` : __saavn üzerinden arama yapar bulur__
💠 `/katil` : __Asistan Grup a Katılıyor__
💠 `/ayril` : __Gruptan Asistan Ayrılıyor__
💠 `/vindir` : __Çalan parçayı youtubeden vdeo olarak indirir____
""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/sohbetlobisi")
              ]]
          )
      )
