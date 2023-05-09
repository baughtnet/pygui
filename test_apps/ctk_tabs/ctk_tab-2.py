import tkinter as tk
import tkinter.ttk as ttk
from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

global fourkHDR
global HD
global SD
global LQ
global aHQ
global aLQ

url = "https://www.youtube.com/watch?v=TpdapO9QGRo&t"
yt = YouTube(url)

print("HQ Adaptive Streams")
hq_adapt_streams = yt.streams.filter(progressive=False).order_by('resolution').desc()
print(hq_adapt_streams)
print("+\n" + "**************************************************" + "\n" + "all streams")
avail_streams = yt.streams.order_by('resolution').desc()
print(avail_streams)

#    CustomApp.dropdown1['values'] = ["4K"]
#    CustomApp.dropdown1.pack()
#    fourkHDR = yt.streams.get_by_itag(337)

class CustomApp(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create a text box to get user input
        self.text_box = tk.Entry(self)
        self.text_box.pack()

        # Create a button to change the menu items
        self.change_button = tk.Button(self, text="Change me", command=self.change_menu)
        self.change_button.pack()

        # Create a tab view
        self.tab_view = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.tab_view)
        self.tab2 = ttk.Frame(self.tab_view)
        self.tab_view.add(self.tab1, text="Tab 1")
        self.tab_view.add(self.tab2, text="Tab 2")
        self.tab_view.pack()

        # Create two dropdown boxes in the first tab
        self.dropdown1 = ttk.Combobox(self.tab1, values=["Option 1", "Option 2", "Option 3"])
        self.dropdown1.pack()

        self.dropdown2 = ttk.Combobox(self.tab1, values=["Option A", "Option B", "Option C"])
        self.dropdown2.pack()

    def change_menu(self):
        # Change the menu item text based on user input
        input_text = self.text_box.get()

        self.dropdown1['values'] = [input_text, "Option 2", "Option 3"]
        self.dropdown1.set(input_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = CustomApp(root)
    app.mainloop()

