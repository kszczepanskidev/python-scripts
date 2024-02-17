from requests import get
from bs4 import BeautifulSoup

from os import makedirs
from sys import exc_info
from urllib.parse import unquote

host_url = 'https://downloads.khinsider.com'

track_download_button = 'playlistDownloadSong'
track_download_link = 'songDownloadLink'

download_directory = 'GameOSTDownload'

albums = [
    '',
]

for album in albums:
    print(f'Downloading album: {album}')

    folder_name = album.replace("-", " ").title()
    makedirs(f'{download_directory}/{folder_name}', exist_ok=True)

    response = get(f'{host_url}/game-soundtracks/album/{album}')
    ost_page = BeautifulSoup(response.content, 'html.parser')

    download_links = [button.a['href'] for button in ost_page.find_all(class_=track_download_button)]

    for download_link in download_links:
        track_name = unquote(download_link.split("/")[-1])
        print(f'    Downloading track {track_name}...', end='')

        response = get(host_url + download_link)
        download_page = BeautifulSoup(response.content, 'html.parser')

        file_link = download_page.findAll('span', class_=track_download_link)[0].parent['href']

        try:
            track = get(file_link)
            file_name = track_name.replace("%20", " ").replace("%27", "\'").replace("%21", "").replace("%28", "- ").replace("%29", "")
            with open(f'{download_directory}/{folder_name}/{file_name}', 'wb') as trackfile:
                trackfile.write(track.content)
            print(f'  Completed')
        except:
            print(f'  Failed | {exc_info()[0]}')
