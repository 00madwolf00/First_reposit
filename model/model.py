# model.py
from pydub import AudioSegment
import numpy as np

class AudioFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.audio_data = None

    def load_audio(self):
        self.audio_data = AudioSegment.from_file(self.file_path)
        if self.audio_data.channels > 1:
            self.audio_data = self.audio_data.set_channels(1)

    def convert_to_wav(self):
        if not self.file_path.endswith('.wav'):
            self.file_path = self.file_path.replace(self.file_path.split('.')[-1], 'wav')
            self.audio_data.export(self.file_path, format='wav')

    def get_waveform_data(self):
        if self.audio_data:
            samples = np.array(self.audio_data.get_array_of_samples())
            time = np.linspace(0, len(self.audio_data) / 1000.0, num=len(samples))
            return time, samples
        return None, None

class AudioAnalyzer:
    def __init__(self, audio_data):
        self.audio_data = audio_data

    def calculate_resonance(self, freq_band):
        fft_result = np.fft.fft(self.audio_data.get_array_of_samples())
        frequencies = np.fft.fftfreq(len(fft_result), 1 / self.audio_data.frame_rate)

        low_freq_range = (20, 300)  # in Hz
        mid_freq_range = (300, 2000)  # in Hz
        high_freq_range = (2000, 20000)  # in Hz

        if freq_band == "low":
            band = low_freq_range
        elif freq_band == "mid":
            band = mid_freq_range
        else:  # "high"
            band = high_freq_range

        band_fft = fft_result[np.where((frequencies >= band[0]) & (frequencies <= band[1]))]
        band_frequencies = frequencies[np.where((frequencies >= band[0]) & (frequencies <= band[1]))]

        return band_frequencies, np.abs(band_fft)
