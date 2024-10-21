from pytube import YouTube
from pytube.cli import on_progress
from pydub import AudioSegment

from os import remove, path

__save_directory = 'yt_download/'

__invalid_characters = [',','.','<','>',':',';','/','\\','|','?','*','!']

urls = [
    ''
]

for url in urls:
    # Get highest quality audio stream.
    yt = YouTube(url, on_progress_callback=on_progress).streams.filter(only_audio=True).order_by('abr').last()

    # Prepare file name from the title.
    filename = yt.title
    for character in __invalid_characters:
        filename = filename.replace(character, '')

    __file_path = f'{__save_directory}/{filename}'

    # Download stream as `.webm` file.
    try:
        yt.download(output_path=__save_directory, filename=f'{filename}.webm')
    except Exception as e:
        if not path.exists(f'{__file_path}.webm'):
            raise(e)

    try:
        # Convert `.webm` to `.ogg`. Will fail if fail is over 4GB.
        webm = AudioSegment.from_file(f'{__file_path}.webm', codec='opus')
        webm.export(f"{__file_path}.ogg", format='ogg')

        # Remove `.webm` file.
        remove(f'{__file_path}.webm')
    except:
        pass

    print('')
