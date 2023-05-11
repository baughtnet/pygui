import tkinter as tk
import ssl
from pytube import YouTube
import customtkinter

ssl._create_default_https_context = ssl._create_unverified_context

itag_dict = {
    "144p": "160",
    "240p": "133",
    "360p": "134",
    "480p": "135",
    "720p": "136",
    "1080p": "137",
    "1440p": "271",
    "2160p": "313"
}

# function for downloading the selected video
def download_video():
    down_res = dropdown1.get()
    print(down_res)
    itag = itag_dict.get(down_res)
    # itag = int(check_itag)
    print(itag)
    if not itag:
        print("Invalid Resolution")
    yt = YouTube(url)
    video = yt.streams.get_by_itag(itag)
    video.download()


url = "https://www.youtube.com/watch?v=TpdapO9QGRo&t"
yt = YouTube(url)

# get available video qualities
video_qualities = [stream.resolution for stream in yt.streams.filter(type="video", video_codec="vp9", progressive=False)]

# set up main window
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x720")
app.title("Dropdown Fill Test App")

# combobox for resolution selection
dropdown1 = customtkinter.CTkComboBox(app)
dropdown1.pack()

# update dropdown options with available video qualities
dropdown1.configure(values=["Video Quality"] + video_qualities)

# download button runs download_video function
download_button = customtkinter.CTkButton(app, command=download_video)
download_button.pack()
state = dropdown1.cget("state")

app.mainloop()
