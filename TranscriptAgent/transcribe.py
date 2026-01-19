import speech_recognition as sr

class Transcriber:
    def __init__(self, file = "recorded.wav"):
        self.file = file
        self.recognizer = sr.Recognizer()
        
    def transcribe(self):
        with sr.AudioFile(self.file) as src:
            data = self.recognizer.record(src)
            text = self.recognizer.recognize_google(data)
            return text
        
    def transcribe_to_file(self, file = "transcript.txt"):
        text = self.transcribe()
        with open(file, 'w') as f:
            f.write(text)
        print(f"Transcription saved to {file}")