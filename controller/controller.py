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

            low_frequencies, low_resonance = self.audio_analyzer.calculate_resonance("low")
            mid_frequencies, mid_resonance = self.audio_analyzer.calculate_resonance("mid")
            high_frequencies, high_resonance = self.audio_analyzer.calculate_resonance("high")

            # Plot individual frequency bands
            self.view.plot_resonance("low", (low_frequencies, low_resonance))
            self.view.plot_resonance("mid", (mid_frequencies, mid_resonance))
            self.view.plot_resonance("high", (high_frequencies, high_resonance))

            # Plot combined frequency bands
            self.view.plot_combined_resonance(
                (low_frequencies, low_resonance),
                (mid_frequencies, mid_resonance),
                (high_frequencies, high_resonance)
            )

    def combine_and_plot(self):
        if self.audio_analyzer:
            low_resonance = self.audio_analyzer.calculate_resonance("low")
            mid_resonance = self.audio_analyzer.calculate_resonance("mid")
            high_resonance = self.audio_analyzer.calculate_resonance("high")

            # Combine the resonance data here as needed

            self.view.plot_combined_resonance(
                low_resonance,
                mid_resonance,
                high_resonance
            )

    def run(self):
        self.root.title("Audio Analysis App")
        self.root.mainloop()


if __name__ == "__main__":
    app = AppController()
    app.run()
