import tkinter as tk
import ssl
from pytube import YouTube
import customtkinter

ssl._create_default_https_context = ssl._create_unverified_context

def printMe():
    state = dropdown1.get()
    print(state)

url = "https://www.youtube.com/watch?v=TpdapO9QGRo&t"
yt = YouTube(url)

# get available video qualities
video_qualities = [stream.resolution for stream in yt.streams.filter(type="video", video_codec="vp9", progressive=False)]
print(yt.streams.filter(type="video", progressive=False, video_codec="vp9"))

# set up main window
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x720")
app.title("Dropdown Fill Test App")

dropdown1 = customtkinter.CTkComboBox(app)
dropdown1.pack()

# update dropdown options with available video qualities
dropdown1.configure(values=["Video Quality"] + video_qualities)

download_button = customtkinter.CTkButton(app, command=printMe)
download_button.pack()
state = dropdown1.cget("state")

state2 = dropdown1.get()
print(state)
print(state2)
app.mainloop()
