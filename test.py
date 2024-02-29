from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
import speech_recognition as sr

import threading
import speech_recognition as sr
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

log = []

def live_transcription_thread():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        while True:
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                # audio = recognizer.adjust_for_ambient_noise(source)p
                text = recognizer.recognize_google(audio)
                log.append(text)
                print(text)
                send_realtime_output(text)
                # print("Transcription:", log[-1])
            except sr.WaitTimeoutError:
                print("Timeout: No speech detected")
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Error with the request: {e}")
            except KeyboardInterrupt:
                print("Transcription ended by user.")
                print(log)
                break


app = Flask(__name__)
CORS(app, origins="http://localhost:3000")  # Allow requests from the React app's origin
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

def send_realtime_output(text):
    socketio.emit('realtime_output', {'output': text})

if __name__ == '__main__':

    transcription_thread = threading.Thread(target=live_transcription_thread)
    transcription_thread.start()

    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)