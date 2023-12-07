# view.py
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MainApplication(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.current_plot = 0
        self.create_widgets()
        self.create_plots()
        self.pack()

    def create_widgets(self):
        self.prev_button = tk.Button(self, text="Previous", command=self.show_previous_plot)
        self.prev_button.pack(side=tk.LEFT)

        self.load_button = tk.Button(self, text="Load Audio", command=self.load_audio)
        self.load_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(self, text="Next", command=self.show_next_plot)
        self.next_button.pack(side=tk.LEFT)

        self.combine_button = tk.Button(self, text="Combine Plots", command=self.combine_plots)
        self.combine_button.pack(side=tk.LEFT)

        self.file_label = tk.Label(self, text="No file selected")
        self.file_label.pack(side=tk.LEFT)

    def create_plots(self):
        self.plots = []

        fig_waveform, ax_waveform = plt.subplots()
        self.plots.append(FigureCanvasTkAgg(fig_waveform, master=self))

        fig_low, ax_low = plt.subplots()
        self.plots.append(FigureCanvasTkAgg(fig_low, master=self))

        fig_mid, ax_mid = plt.subplots()
        self.plots.append(FigureCanvasTkAgg(fig_mid, master=self))

        fig_high, ax_high = plt.subplots()
        self.plots.append(FigureCanvasTkAgg(fig_high, master=self))

        for canvas in self.plots:
            canvas.get_tk_widget().pack_forget()

        self.plots[self.current_plot].get_tk_widget().pack()

        fig_combined, ax_combined = plt.subplots()
        self.plots.append(FigureCanvasTkAgg(fig_combined, master=self))

        for canvas in self.plots:
            canvas.get_tk_widget().pack_forget()

        self.plots[self.current_plot].get_tk_widget().pack()

    def load_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
        if file_path:
            self.controller.load_audio_file(file_path)
            self.file_label.config(text=f"Loaded File: {file_path.split('/')[-1]}")

    def plot_waveform(self, waveform_data):
        if waveform_data is not None:
            time, samples = waveform_data
            ax = self.plots[0].figure.axes[0]
            ax.clear()
            ax.plot(time, samples)
            ax.set_xlabel('Time (seconds)')
            ax.set_ylabel('Amplitude')
            self.plots[0].draw()

    def plot_resonance(self, freq_band, data):
        index = {"low": 1, "mid": 2, "high": 3}.get(freq_band)
        ax = self.plots[index].figure.axes[0]
        ax.clear()
        ax.plot(*data)
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('Amplitude')
        ax.set_title(f'{freq_band.capitalize()} Frequency Resonance')
        self.plots[index].draw()

    def plot_combined_resonance(self, low_data, mid_data, high_data):
        ax = self.plots[4].figure.axes[0]
        ax.clear()
        ax.plot(*low_data, color='blue', label='Low Frequency')
        ax.plot(*mid_data, color='green', label='Mid Frequency')
        ax.plot(*high_data, color='red', label='High Frequency')
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('Amplitude')
        ax.set_title('Combined Frequency Resonance')
        ax.legend()
        self.plots[4].draw()

    def show_previous_plot(self):
        self.plots[self.current_plot].get_tk_widget().pack_forget()
        self.current_plot = (self.current_plot - 1) % len(self.plots)
        self.plots[self.current_plot].get_tk_widget().pack()

    def show_next_plot(self):
        self.plots[self.current_plot].get_tk_widget().pack_forget()
        self.current_plot = (self.current_plot + 1) % len(self.plots)
        self.plots[self.current_plot].get_tk_widget().pack()

    def combine_plots(self):
        self.controller.combine_and_plot()