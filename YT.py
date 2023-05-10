from pytube import YouTube

def on_complete(stream, filepath):
    print('download is done!')
    print(filepath)

def on_progress(stream, chunk, bytes_remaining):
    progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100),2)}%'
    print(progress_string)

url = input('YouTube Link: ')
dir = input('Enter directory to save to: ')
video_obj = YouTube(url, on_complete_callback=on_complete, on_progress_callback= on_progress)

print(f'title:\t{video_obj.title}')
print(f'length:\t{round(video_obj.length / 60,2)} minutes')
print(f'author:\t{video_obj.author}')

print('download: (b)est | (a)udio | (e)xit')
choice = input('choice: ')

match choice:
    case 'b':
        video_obj.streams.get_highest_resolution().download(dir)
    case 'a':
        video_obj.streams.get_audio_only().download(dir)
    case 'e':
        exit()