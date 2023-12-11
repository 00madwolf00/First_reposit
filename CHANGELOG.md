# Change Log
All notable changes to all areas of the program for this project will be documented in this file.

# Added
# 11/15/2023
* Jaheem Clayton added a class called AudioFileHandler for handling the file
* Jaheem Clayton added a class for analyzing the audio
* Jaheem Clayton added a main program that will load and process an audio file
* Jaheem Clayton added to the main program the ability to handle metadata and multichannel
* Jaheem Clayton added to the main program the ability to display the results of data analysis to the user
# 12/5/2023
* Jaheem Clayton created a class that allowed for button functionality   
* Jaheem Clayton added a def function for a button called Load Audio
* Jaheem Clayton added a def function to display the audio information
* Jaheem Clayton added a def function to plot audio waveform/ other relevant data
* Jaheem Clayton added #This should be outside and at the end of the class definition
* Jaheem Clayton added pass under def compute_rt60(self):
* Jaheem Clayton added python imports: from pydub import AudioSegment, 
import numpy as np, import scipy.signal as signal
# 12/10/2023
*  Jaheem Clayton added a requirement.txt 
*  Jaheem Clayton added  def create_info_labels(self):
*  Jaheem Clayton added  def update_audio_info(self, duration, frequency, rt60):
*  Jaheem Clayton added  self.load_button = tk.Button(self, text="Load Audio", command=self.load_audio)
*  Jaheem Clayton added self.file_info_label = tk.Label(self, text="No file loaded")
*  Jaheem Clayton added self.file_info_label.pack()
*  Jaheem Clayton added  # Additional widgets can be added here
*  Jaheem Clayton added file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
*  Jaheem Clayton added if file_path:
*  Jaheem Clayton added  self.controller.load_audio_file(file_path)
*  Jaheem Clayton added self.file_info_label.config(text=f"Loaded File: {file_path.split('/')[-1]}")
*   Jaheem Clayton added def plot_waveform(self, waveform_data):
*  Jaheem Clayton added # Other methods for displaying RT60, etc., can be added here
*  Jaheem Clayton added alterations to view.py and model.py
*  Jaheem Clayton added to controller.py: # This should be outside and at the end of the class definition
*  Jaheem Clayton added to controller.py: self.audio_analyzer = None
*  Jaheem Clayton added to controller.py: self.audio_file.remove_metadata(),  waveform_data = self.audio_file.get_waveform_data(), self.view.plot_waveform(waveform_data)
*  Jaheem Clayton added to controller.py: def run(self):
# 12/6/2023
* Jaheem Clayton added to model.py and view.py the ability for the waveform to calculate time in seconds
* Jaheem Clayton altered the code structure of controller.py moved some code around, and renamed some parts of the code
* Jaheem Clayton merged remote-tracking branch 'origin/main'
*  Jaheem Clayton added code to analyze the frequencies and plot them in controller.py
*  Jaheem Clayton added plotting code for the combined resonance in view.py
*  Jaheem Clayton added a file selecting code in view.py
*  
# 12/7/2023
* Joel Sanderson #Merge the resonance data into a single plot combined_resonance_data = (low_resonance[0] + mid_resonance[0] + high_resonance[0],  # Combine frequencies low_resonance[1] + mid_resonance[1] + high_resonance[1]  # Combine amplitudes)
* Joel Sanderson created a changelog
# 12/10/2023
# Changed
# 12/5/2023
* Jaheem Clayton changed #This should be at the module level, not inside the class
* Jaheem Clayton changed the class called AudioFileHandler to AudioFile
* Jaheem Clayton deleted hashtag in model.py #Import necessary libraries/modules
* Jaheem Clayton removed  self.file_name = None, self.audio_format = None, and self.num_channels = None
 # 12/7/2023
*  Joel Sanderson changed the self.view.combine_and_plot(combined_resonance_data) to self.view.combine_and_plot(*combined_resonance_data)  # Unpack the tuple elements
*  Joel Sanderson removed self.view.plot_combined_resonance(low_resonance, mid_resonance, high_resonance) to 
*  Joel Sanderson removed 
  # 12/10/2023
*  Joel Sanderson removed def combine_and_plot(self)
*  Joel Sanderson removed def combine_and_plot(self, combined_resonance_data):, #Plot the combined resonance data, self.plot_combined_resonance(*combined_resonance_data) 
*  Joel Sanderson removed the button functionality to combine plots
*  Jaheem Clayton changed the README.md and added an explanatory statement for the project
*  Jaheem Clayton removed run.py
*  Jaheem Clayton removed def run(self): from controller.py
*  Jaheem Clayton removed  def analyze_audio(self): from controller.py
*  Jaheem Clayton removed  def compute_rt60(self): from controller.py
*  Jaheem Clayton removed #This should be outside and at the end of the class definition from controller.py
*  Jaheem Clayton removed #This should be outside and at the end of the class definition from controller.py
*  *  Jaheem Clayton removed for band in ["low", "mid", "high"]: in controller.py
