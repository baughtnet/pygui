from pytube import YouTube
from io import BytesIO
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
url = "https://www.youtube.com/watch?v=pQrM5L6C-FQ"
# get thumb url and video title
yt = YouTube(url)
image_url = yt.thumbnail_url.replace('default.jpg', 'hqdefault.jpg')
print(image_url)
yt_title = yt.title

response = urllib.request.urlopen(image_url)
image_data = response.read()
# urllib.request.urlretrieve(image_url, "image.jpg")
# image_data = Image.open("image.jpg")
image = Image.open(BytesIO(image_data))

image = image.resize((320, 180), Image.ANTIALIAS)
yt_image = ImageTk.PhotoImage(image)

image_label = tk.Label(window, width=640, height=360, image=yt_image)
image_label.pack(padx=10, pady=10)

title_label = tk.Label(window, text=yt_title)
title_label.pack()

window.mainloop()
