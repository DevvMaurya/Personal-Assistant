import pyttsx3

class Text_speech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def say(self, text):
        # Set the properties of the speech
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

        # Convert text to speech
        self.engine.say(text)
        self.engine.runAndWait()

    def close(self):
        self.engine.stop()

    def __del__(self):
        self.engine.stop()
        del self.engine