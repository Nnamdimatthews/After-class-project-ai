import speech_recognition as sr
from googletrans import Translator

class DynamicSpeechTranslator:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.translator = Translator()
        self.source_lang = 'en'  # default
        self.target_lang = 'es'  # default

    def set_languages(self, source_lang: str, target_lang: str):
        self.source_lang = source_lang
        self.target_lang = target_lang
        print(f"Source language set to: {self.source_lang}")
        print(f"Target language set to: {self.target_lang}")

    def recognize_speech(self, audio_source: sr.AudioSource) -> str:
        try:
            with audio_source as source:
                print("🎙️ Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)
            print("🧠 Recognizing speech...")
            text = self.recognizer.recognize_google(audio, language=self.source_lang)
            print(f"✅ Recognized: {text}")
            return text
        except sr.UnknownValueError:
            return "[Error] Could not understand audio."
        except sr.RequestError as e:
            return f"[Error] Speech recognition service failed: {e}"

    def translate_text(self, text: str) -> str:
        try:
            print("🌐 Translating...")
            translated = self.translator.translate(text, src=self.source_lang, dest=self.target_lang)
            print(f"✅ Translated: {translated.text}")
            return translated.text
        except Exception as e:
            return f"[Error] Translation failed: {e}"

    def translate_speech(self, audio_source: sr.AudioSource) -> str:
        recognized_text = self.recognize_speech(audio_source)
        if recognized_text.startswith("[Error]"):
            return recognized_text
        return self.translate_text(recognized_text)

# 🧪 Example usage
if __name__ == "__main__":
    translator = DynamicSpeechTranslator()

    # 🌍 Set your desired languages
    translator.set_languages('en', 'it')  # English to italian
    # 🎤 Use microphone input
    try:
        with sr.Microphone() as mic:
            print("Speak now...")
            result = translator.translate_speech(mic)
            print("📢 Final Translation:", result)
    except Exception as e:
        print(f"[Error] Microphone access failed: {e}")
        