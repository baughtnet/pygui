from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# get the video url from the user
#url = input("Enter the video URL: ")
url = "https://www.youtube.com/watch?v=dzkULjGtIdk"

# create a YouTube object
yt = YouTube(url)
# print(yt.vid_info)
# show streams
for stream in yt.streams:
    print(stream)

video = yt.streams.get_highest_resolution()
video.download('yt_download.mp4')
