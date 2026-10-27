class Intent:
    def __init__(self):
        
        pass

    def identify_intent(self,tokens):
        intent = None
        if "open" in tokens or "launch" in tokens:
            intent = "open_app"
            tokens.remove("open")
        if 'search' in tokens:
            intent = "search"
            tokens.remove("search")
           
        
            
        return intent