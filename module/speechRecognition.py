import videoToWav
import wave
import json
from vosk import Model, KaldiRecognizer
from fastpunct import FastPunct

class speechRecogniser(videoToWav.videoToWav):
    def __init__(self, videoFileName, accent):
        super().__init__(videoFileName)
        self.convert()
        self.accent = accent
        self.model = ""

    def recognise(self):

        # Choosing the model
        if (self.accent == '1'):
            self.model = Model("/Users/tusharsharma/B Tech/RESEARCH PROJECTS/Video Summariser Project/module/Models/vosk-model-en-us-0.22")
        elif (self.accent == '2'):
            self.model = Model("/Users/tusharsharma/B Tech/RESEARCH PROJECTS/Video Summariser Project/module/Models/vosk-model-en-in-0.5")
        elif (self.accent == '3'):
            self.model = Model("/Users/tusharsharma/B Tech/RESEARCH PROJECTS/Video Summariser Project/module/Models/vosk-model-en-us-daanzu-20200905")

        wf = wave.open(self.audioFileName, "rb")

        recognizer = KaldiRecognizer(self.model, wf.getframerate())
        fastpunct = FastPunct()

        finalText = ""
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if(recognizer.AcceptWaveform(data)):
                text = json.loads(recognizer.Result())['text']
                finalText += fastpunct.punct(text) + " "
        
        # Saving the recognised text in a txt file
        file = open("/Users/tusharsharma/B Tech/RESEARCH PROJECTS/Video Summariser Project/module/Texts/FinalText.txt", 'w+')
        file.write(finalText)
        file.close()

        return True
