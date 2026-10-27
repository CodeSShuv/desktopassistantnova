from app.listen import listen
from app.browser import WebSearch
from app.parser import Parser
from app.application_scanner import ApplicationScanner
from app.application import ApplicationLauncher
import pyttsx3

class Assistant: 

    def speak(self, text):
        engine = pyttsx3.init("sapi5")
        engine.say(text)
        engine.runAndWait()
        engine.stop
    def __init__(self,name):
        self.application_scanner = ApplicationScanner()
        self.application_launcher = ApplicationLauncher()
        self.applicationNames = self.application_scanner.getApplicationNames()
        self.webSearch = WebSearch()
        self.parser = Parser(self.applicationNames)
        self.name = name
    def process_command(self,message):        
        if message.lower() in ["exit", "quit"]:
            print("Exiting Nova. Goodbye!")
            self.speak("Exiting . Goodbye!")
            return "exit"
        result = self.parser.parse(message)
        if result['intent'] == 'open_app':
            self.speak(f"opening {result["entity"]["name"]}" )
            self.application_launcher.open(result['entity'])
        if result['intent'] == "search":
            self.speak(f"What do you want to search in web? ")
            query = listen()
            self.speak(f"searching {query}")
            self.webSearch.searchInWeb(query)
      
                        