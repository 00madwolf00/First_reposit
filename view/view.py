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
        self.load_button = tk.Button(self, text="Load Audio", command=self.controller.load_audio_file)
        self.load_button.pack()

        # Add more widgets as needed

    def load_audio(self):
        file_path = filedialog.askopenfilename()
        self.controller.load_audio_file(file_path)

    def display_audio_info(self, info):
        # Display audio information
        pass

    def plot_audio_data(self, audio_data):
        # Plot audio waveform or other relevant data
        fig, ax = plt.subplots()
        ax.plot(audio_data)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()
