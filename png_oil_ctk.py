import os
import cv2
from PIL import Image
import tkinter as tk
import customtkinter as ctk

class cnvApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Image to Video Converter")
        self.geometry("1024x768")

        self.setup_converter_interface()

    def setup_converter_interface(self):
        self.title = ctk.CTkLabel(self, text="Image to Video Converter")
        self.title.pack()

        self.instruction = ctk.CTkLabel(self, wrap="word", text="Please select the directory with images and a destination directory")
        self.instruction.pack()