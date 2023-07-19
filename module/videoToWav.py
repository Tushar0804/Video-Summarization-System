import os
from pydub import AudioSegment

class videoToWav:
    def __init__(self, videoFileName):
        self.videoFileName = videoFileName
        self.videoFileExtension = ""
        self.audioFileName = "/Users/tusharsharma/B Tech/RESEARCH PROJECTS/Video Summariser Project/module/Audio/audio.wav"
        self.audioFileExtension = "wav"

    def convert(self):
        self.videoFileExtension = os.path.splitext(self.videoFileName)[1][1:]

        file = AudioSegment.from_file(file=self.videoFileName, format=self.videoFileExtension)
        file.export(self.audioFileName, format=self.audioFileExtension, parameters=["-ac", "1", "-ar", "22050"])
        