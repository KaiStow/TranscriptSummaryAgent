from record import Record
from transcribe import Transcriber
from summary import AISummary
from dotenv import load_dotenv
load_dotenv()

class Main:
    def __init__(self):
        self.recorder = Record()
        self.transcriber = Transcriber()
        self.summary = AISummary()

    def run(self):
        self.recorder.record()
        print("Recording process completed.")
        print("Transcription process starting.")
        self.transcriber.transcribe_to_file()
        print("Transcription process completed.")
        print("Summary process starting.")
        self.summary.summarize()

main = Main()
main.run()