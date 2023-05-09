from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# get the video url from the user
#url = input("Enter the video URL: ")
url = "https://www.youtube.com/watch?v=TpdapO9QGRo&t"

# create a YouTube object
yt = YouTube(url)
# print(yt.vid_info)
# show streams
for stream in yt.streams:
    print(stream)

url2 = "https://www.youtube.com/watch?v=gpP_YEv_9jA"

yt = YouTube(url2)
print("" + "\n" + "***********************************************************************" + "\n")
for stream in yt.streams:
    print(stream)

