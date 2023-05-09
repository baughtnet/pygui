# downloads yt videos using pytube library, adapted from yt tutorial: https://www.youtube.com/watch?v=NI9LXzo0UY0
import tkinter
import customtkinter
from pytube import YouTube
import ssl
from io import BytesIO
from PIL import Image, ImageTk
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

def getInfo():
    global url
    global yt
    url = link.get()
    yt = YouTube(url)
    title.configure(text=yt.title)
    image_url = yt.thumbnail_url.replace('default.jpg', 'hqdefault.jpg')
    response = urllib.request.urlopen(image_url)
    image_data = response.read()
    image = Image.open(BytesIO(image_data))
    image = image.resize((640, 360), Image.LANCZOS)
    yt_image = ImageTk.PhotoImage(image)
    # Lines for customtkinter, couldn't get it to work...
    # vid_canvas.delete("all")
    # vid_canvas.create_photo(0, 0, anchor='nw', image=yt_image)
    # vid_canvas.image = yt_image
    vid_image.configure(image=yt_image)

# This portion was written from ChatGPT and pytube reference when I thought the program wasn't working
# Turns out pytube was incorrectly installed, see https://github.com/pytube/pytube/issues/743 for details
# Removed original code, moving forward with this


def startDownload():
    try:
        # url = link.get()
        yt = YouTube(url, on_progress_callback=on_progress)
        video = yt.streams.get_highest_resolution()
        title.configure(text=yt.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Download Complete!", text_color="black")
        link.delete(0, 'end')
    except:
        finishLabel.configure(text="Invalid Link", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)
    per = str(int(percentage_of_completion))
    pPercent.configure(text=per + '%')
    pPercent.update()
    progressBar.set(float(percentage_of_completion) / 100)


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app window
app = customtkinter.CTk()
app.geometry("720x720")
app.title("Youtube Downloader")

# ui elements
title = customtkinter.CTkLabel(app, text="Video Title")
title.pack()

vid_image = customtkinter.CTkLabel(app, width=640, height=360, text="")
vid_image.pack()
# vid_canvas = customtkinter.CTkCanvas(app, width=640, height=360)
# vid_canvas.pack()

url_title = customtkinter.CTkLabel(app, text="Paste URL to video:")
url_title.pack()

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

info_button = customtkinter.CTkButton(app, text="Get Info", command=getInfo)
info_button.pack(padx=10, pady=10)

pPercent = customtkinter.CTkLabel(app, text="0%")
pPercent.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=5, pady=5)

quitApp = customtkinter.CTkButton(app, text="Quit", command=app.destroy)
quitApp.pack()

app.mainloop()
