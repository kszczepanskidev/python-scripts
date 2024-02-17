# game_ost_download
Script to download all music files in an album from `https://downloads.khinsider.com`.
Downloaded files will be placed into `GameOSTDownload/{album name}` directory.

1. Install required dependencies
```bash
pip install -r requirements.txt
```

2. Put album names into `albums` variable at line 15, example for album URLs:
- https://downloads.khinsider.com/game-soundtracks/album/persona-5-2016-ps3
- https://downloads.khinsider.com/game-soundtracks/album/minecraft
- https://downloads.khinsider.com/game-soundtracks/album/just-shapes-beats-2018

```python
    albums = [
        'persona-5-2016-ps3',
        'minecraft',
        'just-shapes-beats-2018',
    ]
```

3. Run the script
```bash
python game_ost_download.py
```
