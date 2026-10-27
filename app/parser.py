from app.intent import Intent
from app.preprocessor import Preprocessor
from app.entity import Entity
class Parser:

    def __init__(self,applications):
        self.preprocessor = Preprocessor()
        self.intent = Intent()
        self.entity = Entity(applications)
        
    def parse(self, command):
        tokens = self.preprocessor.runPreprocessing(command)
        final_intent = self.intent.identify_intent(tokens)
        if final_intent == None:
            return {
            "intent" : final_intent,
            "entity" : None
        }
        entity = self.entity.getEntity(final_intent, tokens)
       
        return {
            "intent" : final_intent,
            "entity" : entity
        }