from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# get the video url from the user
#url = input("Enter the video URL: ")
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# create a YouTube object
video = YouTube(url)
ytStream = video.streams
