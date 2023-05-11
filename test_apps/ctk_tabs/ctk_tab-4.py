import tkinter as tk
import ssl
from pytube import YouTube
import customtkinter
import os
import subprocess

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
    print(itag)
    if not itag:
        print("Invalid Resolution")
    if itag in ["136", "137", "271", "313"]:
        yt = YouTube(url)
        print(itag)
        video = yt.streams.get_by_itag(itag)
        video_file = video.download(filename=yt.title + "_video")
        audio = yt.streams.get_by_itag(251)
        audio_file = audio.download(filename=yt.title + "_audio")
        video_filename = os.path.splitext(video_file)[0]
        merged_filename = video_filename+"_"+audio.abr+".mp4"
        subprocess.run(['ffmpeg', '-y', '-i', video_file, '-i', audio_file, '-c:v', 'libx264', '-c:a', 'aac', '-strict', '-2', merged_filename])
        os.remove(audio_file)
        os.remove(video_file)
    else:
        print("Downloading " + itag)
        yt = YouTube(url)
        video = yt.streams.get_by_itag(itag)
        video.download()
        print("Download Complete!")


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
