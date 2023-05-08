# downloads yt videos using pytube library, adapted from yt tutorial: https://www.youtube.com/watch?v=NI9LXzo0UY0
import tkinter
import customtkinter
from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# This portion was written from ChatGPT and pytube reference when I thought the program wasn't working
# Turns out pytube was incorrectly installed, see https://github.com/pytube/pytube/issues/743 for details
# Removed original code, moving forward with this
def startDownload():
    try:
        url = link.get()
        yt = YouTube(url, on_progress_callback=on_progress)
        video = yt.streams.get_highest_resolution()
        title.configure(text=yt.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Download Complete!", text_color="black")
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
    progressBar.set(float(percentage_of_completion) / 100 )

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

# finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

pPercent = customtkinter.CTkLabel(app, text="0%")
pPercent.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0.5)
progressBar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

quitApp = customtkinter.CTkButton(app, text="Quit", command=app.destroy)
quitApp.pack()

app.mainloop()
