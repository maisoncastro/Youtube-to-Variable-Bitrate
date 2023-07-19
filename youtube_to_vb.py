import yt_dlp as youtube_dl

def download_video_as_mp3(url, output_filename):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',  # V0 quality
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

video_url = "YOUR_YOUTUBE_VIDEO_URL_HERE"
download_video_as_mp3(video_url)