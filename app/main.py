from app.assistant import Assistant
from app.listen import listen
from app.wakeupword import WakeWordDectector

def main():
        Nova = Assistant("Nova")
        
        wake_word_detector = WakeWordDectector()
        while True:
            print("Listening for wake word...")
            if wake_word_detector.listen():
                # user_input = input("You: ")
                # response = Nova.process_command(user_input)
                Nova.speak("Yes?")
                text =  listen()
                print(f"Nova: {text}")
                Nova.process_command(text)
        
            
if __name__ == "__main__":
    main()