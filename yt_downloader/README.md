# yt_downloader
Script to download given youtube videos as audio files coverted to `.ogg` format.
Downloaded files will be placed into `yt_download` directory.

1. Install required dependencies
```bash
pip install -r requirements.txt
```

2. Put youtube urls into `urls` variable at line 10.
```python
urls = [
	'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
]
```

3. Run the script
```bash
python yt_downloader.py
```
