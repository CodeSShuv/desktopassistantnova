from app.assistant import Assistant
from app.listen import listen
from app.wakeupword import WakeWordDectector

def main():
        Nova = Assistant("Nova")
        
        wake_word_detector = WakeWordDectector()
       
        while True:
            print("Listening for wake word...")
            if wake_word_detector.listen():
                Nova.speak("Yes?")
                text =  listen()
                if not text:
                    Nova.speak("Couldn't hear you!") 
                print(f"Nova: {text}")
                Nova.process_command(text)
        
            
if __name__ == "__main__":
    main()