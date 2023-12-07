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
        waveform_data = self.audio_file.get_waveform_data()
        self.view.plot_waveform(waveform_data)
        self.analyze_audio()

    def analyze_audio(self):
        if self.audio_file and self.audio_file.audio_data:
            self.audio_analyzer = AudioAnalyzer(self.audio_file.audio_data)

            for band in ["low", "mid", "high"]:
                frequencies, resonance = self.audio_analyzer.calculate_resonance(band)
                self.view.plot_resonance(band, (frequencies, resonance))

    def run(self):
        self.root.title("Audio Analysis App")
        self.root.mainloop()


if __name__ == "__main__":
    app = AppController()
    app.run()
