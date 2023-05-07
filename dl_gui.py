import tkinter
import customtkinter
from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def startDownload():
    # ytLink = link.get()
    # ytObject = YouTube(ytLink)
    # print(ytLink)
    # print(ytObject)
    # print(ytObject.vid_info)
    # video = ytObject.streams.get_highest_resolution()
    # if video is not None:
        # video.download()
    # else:
        # print('Could not find high resolution video to download')
    url = link.get()
    video = YouTube(url)
    stream = streams.get_highest_resolution()
    stream.download()



customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app window
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# ui elements
title = customtkinter.CTkLabel(app, text="URL")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)
app.mainloop()
