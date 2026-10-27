
FOR_WEB = [
    "google",
    "youtube",
    "spotify"
]
class Entity:
    applications = []
    def __init__(self, applications):
       self.applications = applications
       pass
        
    def getEntity(self, intent,tokens ):
      
        if intent == "open_app":
            for token in tokens:
                
                for application in self.applications:
                    if token in application["name"].split(".")[0].lower():
                        print("the correct application is :",application["name"])
                        return application
            print("Application not found")
            return None
            
        elif intent.lower() == "Search".lower():
            query = ""
            entity= None
            if len(tokens) == 0:
                return None
            for item in FOR_WEB:
                
                if item == tokens[int(len(tokens)-1)]:
                    entity = item
                    tokens.pop()
                    if len(tokens) == 0 :
                        break
                    tokens.pop()
                    break
                else:
                    continue
            for token in tokens:
                    query+=token
            # print("Returning", query)
            #here we are checking if the query cannot be formed by joining the tokens then we are going to keep the query empty this empty query  will go to the assistant's processcommand function and query will be asked again from the user.
            # query = entity if not entity == None else None if query==""else query
            if not entity == None:
                return {"name":entity,
                        "query" :query} 
               
            return {"name":'google',
                    "query" : query}
           
           
        pass