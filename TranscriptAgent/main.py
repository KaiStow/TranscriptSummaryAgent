from record import Record
from transcribe import Transcriber

class Main:
    def __init__(self):
        self.recorder = Record()
        self.transcriber = Transcriber()

    def run(self):
        self.recorder.record()
        print("Recording process completed.")
        print("Transcription process starting.")
        self.transcriber.transcribe_to_file()

main = Main()
main.run()