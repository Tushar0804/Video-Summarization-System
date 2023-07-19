from speechRecognition import speechRecogniser
from textSummarisation import Summariser
import sys

class model:
    def __init__(self, videoFileName, videoAccent):
        self.videoFileName = videoFileName
        self.videoAccent = videoAccent
        self.speechToText = speechRecogniser(self.videoFileName, self.videoAccent)
        self.textFileName = "/Users/tusharsharma/B Tech/RESEARCH PROJECTS/Video Summariser Project/module/Texts/FinalText.txt"
        self.Summariser = Summariser(self.textFileName)
       

    def getText(self):
        result = self.speechToText.recognise()

        return result

    def summarise(self):
        result = self.getText()

        if(result):
            summary = self.Summariser.summarise()
            return summary

if __name__ == "__main__":
    args = sys.argv
    video_file_path = args[1]
    video_accent = args[2]

    ob = model(video_file_path, video_accent)
    summary = ob.summarise()

    print(summary)
