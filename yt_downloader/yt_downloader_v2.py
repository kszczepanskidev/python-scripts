from yt_dlp import YoutubeDL
from pydub import AudioSegment

from os import remove, path

__save_directory = 'yt_download/'

__invalid_characters = [',','.','<','>',':',';','/','\\','|','?','*','!']

urls = [
    ''
]

ydl_opts = {
    'format': 'ogg/bestaudio/best',
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'vorbis',
    }]
}

with YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(urls)
