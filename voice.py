import speech_recognition as sr

def record_voice():
    """Capture voice input from the microphone and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for speech... Speak now.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google's speech recognition
        text = recognizer.recognize_google(audio)
        print(f"Recognized Speech: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return ""
