# simple program for learning customtkinkter tab view,
# radio buttons and drop down menus

# import libraries
import customtkinter
from pytube import YouTube

# function for building the dropdown menus
def build_menu():
    if stream_4k is not None:
        customtkinter.CTkOptionMenu(tabview.tab("Video").configure(values

# set appearance
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
# setup app window
app = customtkinter.CTk()
app.geometry("800x600")
app.title("Custom Tkinter Test App")
# create tabview - use to build Audio/Video Tab Download options...?
tabview = customtkinter.CTkTabview(app, width=450)
tabview.grid(row=0, column=2, padx=(10, 0), pady=(10, 0), sticky="nsew")
tabview.add("Video")
tabview.add("Audio")
tabview.tab("Video").grid_columnconfigure(0, weight=2)  # configure grid of individual tabs
tabview.tab("Audio").grid_columnconfigure(0, weight=1)

optionmenu_1 = customtkinter.CTkOptionMenu(tabview.tab("Video"), dynamic_resizing=True,
                                           values=["HQ", "HD", "SD"])
optionmenu_1.grid(row=0, column=0, padx=20, pady=(20,10))

url = "https://www.youtube.com/watch?v=TpdapO9QGRo&t=94s"
yt = YouTube(url)
stream_4k = yt.streams.get_by_resolution(resolution="2160p")

build_menu()
app.mainloop()
