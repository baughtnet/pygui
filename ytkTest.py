from pytube import YouTube
import ssl
import urllib.request
from PIL import Image, ImageTk
import tkinter as tk

# set up the Tkinter
window = tk.Tk()
window.geometry("720x480")

# download image
ssl._create_default_https_context = ssl._create_unverified_context
# get the video url from the user
# url = input("Enter the video URL: ")
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# get thumb url and video title
yt = YouTube(url)
image_url = yt.thumbnail_url
yt_title = yt.title

urllib.request.urlretrieve(image_url, "image.jpg")

pil_image = Image.open("image.jpg")

yt_image = ImageTk.PhotoImage(pil_image)

image_label = tk.Label(window, image=yt_image)
image_label.pack(padx=10, pady=10)

title_label = tk.Label(window, text=yt_title)
title_label.pack()

window.mainloop()
