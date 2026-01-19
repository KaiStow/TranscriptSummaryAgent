import pyaudio
import wave

class Record:
    def __init__(self, filename = "recorded.wav", chunk_size=1024, format=pyaudio.paInt16, channels=2, rate=44100):
        self.filename = filename
        self.chunk_size = chunk_size
        self.format = format
        self.channels = channels
        self.rate = rate
        self.audio = pyaudio.PyAudio()
        self.frames = []

    def start_recording(self):
        self.stream = self.audio.open(
            format = self.format,
            channels = self.channels,
            rate = self.rate,
            input = True,
            frames_per_buffer=self.chunk_size
        )
        print("Recording started, press Ctrl+C to stop.")
        try:
            while True:
                data = self.stream.read(self.chunk_size)
                self.frames.append(data)
        except KeyboardInterrupt:
            print("Recording stopped.")
            pass
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

    def save_recording(self):
        file = wave.open(self.filename, 'wb')
        file.setnchannels(self.channels)
        file.setsampwidth(self.audio.get_sample_size(self.format))
        file.setframerate(self.rate)
        file.writeframes(b''.join(self.frames))
        file.close()

    def record(self):
        self.start_recording()
        self.save_recording()
        print(f"Recording saved as {self.filename}")