import speech_recognition as sr

log = []

def live_transcription():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        while True:
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)
                log.append(recognizer.recognize_google(audio))
                print(log)
                print("Transcription:", log[-1])
            except sr.WaitTimeoutError:
                print("Timeout: No speech detected")
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Error with the request; {e}")
            except KeyboardInterrupt:
                print("Transcription ended by user.")
                print(log)
                break

if __name__ == "__main__":
    live_transcription()