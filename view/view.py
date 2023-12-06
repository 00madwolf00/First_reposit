# view.py
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MainApplication(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self, text="Load Audio", command=self.load_audio)
        self.load_button.pack()

        self.file_info_label = tk.Label(self, text="No file loaded")
        self.file_info_label.pack()

        # Additional widgets can be added here

    def load_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
        if file_path:
            self.controller.load_audio_file(file_path)
            self.file_info_label.config(text=f"Loaded File: {file_path.split('/')[-1]}")

    def plot_waveform(self, waveform_data):
        if waveform_data is not None:
            fig, ax = plt.subplots()
            ax.plot(waveform_data)
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            canvas.get_tk_widget().pack()
        else:
            print("No waveform data to plot")

        # Other methods for displaying RT60, etc., can be added here
