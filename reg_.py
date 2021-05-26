import speech_recognition as sr
def reg():
    while True:
        try:
            a=sr.Recognizer()
            with sr.Microphone() as speech:
                a.adjust_for_ambient_noise(speech)
                spoke=a.listen(speech)
                try:
                    text=a.recognize_google(spoke)
                    return text
                except:
                    return False
        except:
            return False
