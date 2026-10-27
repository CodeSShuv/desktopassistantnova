import sounddevice as sd
import speech_recognition as sr
recognizer = sr.Recognizer()

SAMPLE_RATE = 16000


def listen():

    duration = 3  # seconds

    print("Listening...")

    
    recording = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    
    audio = sr.AudioData(
        recording.tobytes(),
        SAMPLE_RATE,
        2
    )

    try:
        text = recognizer.recognize_google(audio)

        print(f"You said: {text}")

        return text.strip().lower()


    except sr.UnknownValueError:

        print("Sorry, I could not understand the audio.")

        return ""


    except sr.RequestError as e:

        print("Speech service error:", e)

        return ""