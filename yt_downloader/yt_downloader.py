from pytube import YouTube
from pydub import AudioSegment

from os import remove

_save_directory = 'yt_download/'

_invalid_characters = [',','.','<','>',':',';','/','\\','|','?','*','!']

urls = [
    '',
]

for url in urls:
    # Get highest quality audio stream.
    yt = YouTube(url).streams.filter(only_audio=True).order_by('abr').last()

    # Prepare file name from the title.
    filename = yt.title
    for character in _invalid_characters:
        filename = filename.replace(character, '')

    # Download stream as `.webm` file.
    yt.download(output_path=_save_directory, filename=f'{filename}.webm')

    # Convert `.webm` to `.ogg`.
    webm = AudioSegment.from_file(f'{_save_directory}/{filename}.webm', codec='opus')
    webm.export(f"{_save_directory}/{filename}.ogg", format='ogg')

    # Remove `.webm` file.
    remove(f'{_save_directory}/{filename}.webm')
