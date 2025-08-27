import threading
import wave
import pyaudio
import speech_recognition as sr
import os

class MyAudio:
    def __init__(self):
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 16000
        self.frames = []
        self.recording = False
        self.p = pyaudio.PyAudio()
        self.stream = None

    def start_recording(self):
        self.frames = []
        self.recording = True
        self.stream = self.p.open(format=self.format,
                                  channels=self.channels,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunk)
        threading.Thread(target=self.record).start()

    def record(self):
        while self.recording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)

    def stop_recording(self):
        self.recording = False
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def save(self, filename="my_audio.wav"):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        print(f"Saved audio to {filename}")

def speech_to_text(audio_file="my_audio.wav", transcript_file="transcript.txt"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        print("Transcription:", text)
    except sr.UnknownValueError:
        text = "Could not understand the audio."
    except sr.RequestError as e:
        text = f"API error: {e}"
    with open(transcript_file, "w") as f:
        f.write(text)
    print(f"Saved transcript to {transcript_file}")

def main():
    audio = MyAudio()
    print("Recording... Press Enter to stop.")
    audio.start_recording()
    input()
    audio.stop_recording()
    audio.save()
    speech_to_text()

if __name__ == "__main__":
    main()
