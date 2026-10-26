

class Entity:
    applications = []
    def __init__(self, applications):
       self.applications = applications
       pass
        
    def getEntity(self, intent,tokens ):
        if intent == "open_app":
            for token in tokens:
                print(token)
                for application in self.applications:
                    # print(application["name"])
                    if token in application["name"].split(".")[0].lower():
                        print("the correct application is :",application["name"])
                        return application
                        # return{
                        #     "intent" : intent
                        #     "entity": 
                        # } 
        
            print("Application not found")
            return None
            pass
        pass