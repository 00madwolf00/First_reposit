# controller.py
from model.model import AudioFile, AudioAnalyzer
from view.view import MainApplication
import tkinter as tk

class AppController:
    def __init__(self):
        self.root = tk.Tk()
        self.view = MainApplication(self.root, self)
        self.audio_file = None
        self.audio_analyzer = None

    def load_audio_file(self, file_path):
        self.audio_file = AudioFile(file_path)
        self.audio_file.load_audio()
        self.audio_file.convert_to_wav()
        self.audio_file.remove_metadata()
        waveform_data = self.audio_file.get_waveform_data()
        self.view.plot_waveform(waveform_data)

    def run(self):
        self.root.title("SPIDAM Project")
        self.root.mainloop()

if __name__ == "__main__":
    app = AppController()
    app.run()
