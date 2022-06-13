import speech_recognition as sr

def transcribe(path, locale):
    r = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio, language=locale)
        return text

    except sr.UnknownValueError:
        return "Google Speech Recognition не может понять аудио. 4C7"
    except sr.RequestError as e:
        return "Не удалось запросить результаты у службы распознавания речи Google.4C7; {0}".format(e) 

