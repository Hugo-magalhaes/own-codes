
import os
from pathlib import Path

from pytube import YouTube


def downloader_yt():
    link = str(input('Coloque o link do vídeo a ser convertido: '))
    yt = YouTube(link)
    t = yt.streams.filter(only_audio=True)
    t[0].download()
    print()
    print('download completo')


def convert_mp4_to_mp3():
    for file in os.listdir():
        if file.endswith('.mp4'):
            p = Path(file)
            p.rename(p.with_suffix('.mp3'))
            print()
            print(f' {p} arquivo modificado para .mp3')


if __name__ == "__main__":
    downloader_yt()
    convert_mp4_to_mp3()
