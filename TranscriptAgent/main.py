from record import Record

class Main:
    def __init__(self):
        self.recorder = Record()

    def run(self):
        self.recorder.record()
        print("Recording process completed.")


main = Main()
main.run()