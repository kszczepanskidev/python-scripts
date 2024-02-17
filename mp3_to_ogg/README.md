# mp3_to_ogg
Script to convert all `.mp3` audio files in given directory to `.ogg`.

1. Install required dependencies
```bash
pip install -r requirements.txt
```

2. Put paths to directories with `.mp3` files into `paths` variable at line 30. By default it's set to convert all audio files in current directory.
```python
paths = [
	r".",
]
```

3. Run the script
```bash
python mp3_to_ogg.py
```
