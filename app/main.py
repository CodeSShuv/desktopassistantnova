from app.assistant import Assistant
from app.listen import listen
from app.wakeupword import WakeWordDectector
def main():
    # try:
        Nova = Assistant("Nova")
        
        wake_word_detector = WakeWordDectector()
       
        while True:
            # try:
                print("Running Nova")
                if wake_word_detector.listen():
                    Nova.speak("Yes?")
                    text =  listen()
                   
                    print(f"Nova: {text}")
                    internalAnswer = Nova.process_command(text)
                    if internalAnswer == "exit":
                        break
            # except Exception as e :
            #     Nova.speak("Sorry I faced a problem")
            #     print(e)
            #     pass
    # except Exception as e:
        # Nova.speak("Sorry I face a problem")
            
            
if __name__ == "__main__":
        main()