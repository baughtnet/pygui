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
# for stream in yt.streams:
    # print(stream)

# url2 = "https://www.youtube.com/watch?v=gpP_YEv_9jA"

# yt = YouTube(url2)
# print("" + "\n" + "***********************************************************************" + "\n")
for stream in yt.streams:
    print(stream)
# qualities = [stream.resolution for stream in yt.streams.filter(type="video", progressive=True)]
# print(qualities)

# 144p - 160
# 240p - 133
# 360p - 134
# 480 - 135
# 720p - 136
# 1080p - 137
# 1440p - 271
# 2160p - 313
# 251 - hq webm audio(160) 
# 250 - mq 70
# 249 - lq 50
# 140 - hq mp4(128)
# 139 - lq 48
