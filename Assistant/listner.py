import speech_recognition as sr

class Listern:
    def __init__(self):
        self.r = sr.Recognizer()
    
    def listen(self):
        with sr.Microphone() as source:
            print("Speak Somthing..!")
            audio = self.r.listen(source)

            try:
                text = self.r.recognize_google(audio)
                return text
            except Exception as e:
                return "Error: " + str(e)