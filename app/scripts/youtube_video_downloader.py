import os
from pytube import YouTube

BASE_DIR = os.getcwd()

url = str(input("\nspecify you playlist url\n"))

user_res = '720p'

try:
    yt = YouTube(url)
    main_title = yt.title
    main_title = main_title + '.mp4'
    main_title = main_title.replace('|', '')
    
except:
    print('connection problem..unable to fetch video info')

try:
    vid = yt.streams.filter(progressive=True, file_extension='mp4', res=user_res).first()
    print('Downloading. . . ' + vid.default_filename + ' and its file size -> ' + str(round(vid.filesize / (1024 * 1024), 2)) + ' MB.')
    vid.download(BASE_DIR)
    print('Video Downloaded')
except:
    print('This video could not be download')
    pass

print(' downloading finished')