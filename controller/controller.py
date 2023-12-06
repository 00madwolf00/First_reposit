# controller.py
from model.model import AudioFile, AudioAnalyzer
from view.view import MainApplication
import tkinter as tk

class AppController:
    def analyze_audio(self):
        if self.audio_file and self.audio_file.audio_data:
            self.audio_analyzer = AudioAnalyzer(self.audio_file.audio_data)
            duration = self.audio_analyzer.get_duration()
            frequency = self.audio_analyzer.analyze_frequencies()
            rt60 = self.audio_analyzer.calculate_rt60()
            self.view.update_audio_info(duration, frequency, rt60)
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
