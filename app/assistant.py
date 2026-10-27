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
        if not message:
          self.speak("Couldn't hear you!") 
          return
        elif message.strip().lower() == "Who are you".lower():
           self.speak("I am nova your digital assistant. I can open applications,search on web")
           return
        elif message.strip().lower() == "Who is nova".lower():
            self.speak("Its me")
            return
        result = self.parser.parse(message)
       
        if result['intent'] == 'open_app':
            if(result["entity"] == None): self.speak("Couldn't find the application")
            self.speak(f"opening {result["entity"]["name"]}" )
            self.application_launcher.open(result['entity'])
        elif result['intent'] == "search":
            #here their is no none check  for entity's name as I have created a method in entity class that doesnot allows any 
            #entity's name to be none .. if no entity'name is given by the user then by default the entity;name becomes google. 
            
            #so if there is no specific demand for any entity  like youtube or google itself then the nova will search
            # the query in google.com
           
            
            
            if result['entity'] == None:
                self.speak(f"Couldn't decide what to search")
                return
                # query.remove(result['intent'])
            query =result["entity"]['query']
            self.webSearch.searchInWeb(query, result['entity']['name'])
        else:
            self.speak(f"Sorry I can't do that.")
                        