import tkinter as tk
from pytube import YouTube
import ssl
import customtkinter

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.youtube.com/watch?v=TpdapO9QGRo&t"
yt = YouTube(url)


# print("HQ Adaptive Streams")
# hq_adapt_streams = yt.streams.filter(progressive=False).order_by('resolution').desc()
# print(hq_adapt_streams)
# print("+\n" + "**************************************************" + "\n" + "all streams")
# avail_streams = yt.streams.order_by('resolution').desc()
# print(avail_streams)

# set up main window
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x720")
app.title("Dropdown Fill Test App")

# add streams to dropdown menu
dropdown1 = customtkinter.CTkComboBox(app, values=["Video Quality"])
dropdown1.pack()

# dropdown2 = customtkinter.CTkComboBox(app, values=["Option A", "Option B", "Option C"])
# dropdown2.pack()
# tab view config
# tab_view = customtkinter.CTkTabview(app, width=450)
# tab_view.pack()

# tab1 = tab_view.add("Video")
# tab2 = tab_view.add("Audio")

for stream in yt.streams.filter(type="video").order_by('resolution').desc():
    if(stream.video_codec == "vp9"):
        dropdown1.insert_option(0, f"{stream.resolution} (VP9)")
    else:
        dropdown1.insert_option(0, f"{stream.resolution}")

dropdown1.pack()


app.mainloop()
