# Yayında ve yapımda emeği geçen herkese teşekkürler. 
import os

from pyrogram import Client
from pyrogram.types import Message, Voice

import youtube_dl
from youtube_search import YoutubeSearch
import requests

from config import BOT_NAME as Bn
from helpers.filters import command, other_filters
from helpers.decorators import errors

@Client.on_message(command("bul") & other_filters)
@errors
async def a(client, message: Message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = await message.reply(f"**{Bn} :-** 🔍 Aranıyor {query}")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]

            ## SÜRE SıNıRı ISTIYORSANıZ BUNU KULLANıMDAN KALDıRıLSıN. 1800'LERI KENDI ÖNCEDEN BELIRLENMIŞ SÜRENIZE DEĞIŞTIRIN VE MESAJ (30 dakika üst SıNıRı) SıNıRıNı SANIYELER IÇINDE DÜZENLEYIN
            # if time_to_seconds(duration) >= 1800:  # süre sınırı
            #     m.edit("Exceeded 30mins cap")
            #     return

            views = results[0]["views"]
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            m.edit(f"**{Bn} :-** 😕 Hiçbir şey bulamadım. Yazımı biraz değiştirmeyi dene..\n\n{e}")
            return
    except Exception as e:
        m.edit(
           f"**{Bn} :-** 😕 Hiçbir şey bulamadım. Üzgünüm.\n\nBaşka bir kelime deneyin veya düzgün düzenleyin."
        )
        print(str(e))
        return
    await m.edit(f"**{Bn} :-** 📥 Indiriyor...\n**Query :-** {query}")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎶 **Başlık:** [{title[:35]}]({link})\n⏳ **Süre:** {duration}\n👀 **Görünümler:** {views}'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        await  message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name)
        await m.delete()
    except Exception as e:
        m.edit(f"❌ Hata!! \n\n{e}")
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


# YouTube çalan müzik i vdeo olarak indirmek için.
 
@Client.on_message(filters.command(["vindir", "video"]))
async def ytmusic(client,message: Message):
    global is_downloading
    if is_downloading:
        await message.reply_text("Another download is in progress, try again after sometime.")
        return

    urlissed = get_text(message)

    pablo =  await client.send_message(
            message.chat.id,
            f"`📩 Alıyorum {urlissed} Youtube Sunucularından. Lütfen bekleyin.`")
    if not urlissed:
        await pablo.edit("Geçersiz Komut Sözdizimi, Daha fazla şey öğrenmek için lütfen Yardım menüsünü kontrol edin!")
        return
    
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
            "format": "best",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {"key": "FFmpegVideoConvertor", "tercih edilen biçim": "mp4"}
            ],
            "outtmpl": "%(id)s.mp4",
            "logtostderr": False,
            "quiet": True,
        }
    try:
        is_downloading = True
        with youtube_dl.YoutubeDL(opts) as ytdl:
            infoo = ytdl.extract_info(url, False)
            duration = round(infoo["duration"] / 60)

            if duration > 8:
                await pablo.edit(
                    f"❌ 8 dakikadan uzun videolar(s) izin verilmezse, sağlanan video{duration} dakika(s)"
                )
                is_downloading = False
                return
            ytdl_data = ytdl.extract_info(url, download=True)
            
    
    except Exception as e:
        #await pablo.edit(event, f"**Failed To Download** \n**Error :** `{str(e)}`")
        is_downloading = False
        return
    
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"**Video Name ➠** `{thum}` \n**Requested For :** `{urlissed}` \n**Channel :** `{thums}` \n**Link :** `{mo}`"
    await client.send_video(message.chat.id, video = open(file_stark, "rb"), duration = int(ytdl_data["duration"]), file_name = str(ytdl_data["title"]), thumb = sedlyf, caption = capy, supports_streaming = True , progress=progress, progress_args=(pablo, c_time, f'`Uploading {urlissed} Song From YouTube Music!`', file_stark))
    await pablo.delete()
    is_downloading = False
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)
