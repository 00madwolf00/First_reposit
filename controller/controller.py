# controller.py
from model.model import AudioFile, AudioAnalyzer
from view.view import MainApplication
import tkinter as tk

class AppController:
    def __init__(self):
        self.root = tk.Tk()
        self.view = MainApplication(self.root, self)
        self.audio_file = None

    def run(self):
        self.root.title("SPIDAM Project")
        self.root.mainloop()

    def load_audio_file(self, file_path):
        self.audio_file = AudioFile(file_path)
        self.audio_file.load_audio()
        self.audio_file.convert_to_wav()
        # Update view with audio file info

    def analyze_audio(self):
        analyzer = AudioAnalyzer(self.audio_file.audio_data)
        # Perform analysis and update view with results

    def compute_rt60(self):
        # Compute RT60 and update view with results

# This should be at the module level, not inside the class
if __name__ == "__main__":
    app = AppController()
    app.run()
