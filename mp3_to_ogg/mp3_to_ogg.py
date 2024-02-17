import os
from sys import exit
from glob import glob
from pydub import AudioSegment

def converter(name,ext,path,form):
	print(f'{name} Processing...')
	sound = AudioSegment.from_mp3(f'{path}\{name}{ext}')
	sound.export(f"{path}/{name}.{form}", format=form)


def mp3_to_ogg(filepath):
	if not glob(filepath + '\*.mp3'):
		raise FileNotFoundError(f'No MP3 files found on {filepath}')
		exit(1)

	for i in os.listdir(filepath):
		print(i)
		if os.path.isdir(i):
			print("Skipping directories...")
		else:
			name, ext = os.path.splitext(i)
			if os.path.isfile(f'{filepath}/{name}.ogg') or ext == ".ogg":
				print(f"{name} is already exported as ogg file, skipping...")
			elif ext !='.mp3':
				print("Skipping not mp3 files...")
			else:
				converter(name, ext, filepath, "ogg")

paths = [
	r".",
]

for path in paths:
	try:
		mp3_to_ogg(path)
	except:
		continue

