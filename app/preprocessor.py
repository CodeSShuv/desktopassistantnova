class Preprocessor:
    def __init__(self):
        pass

    def clean_text(self, command):
        return command.strip()
    def remove_special_characters(self,command):
        return ( ''.join(e for e in command if e.isalnum() or e.isspace()))
    def tokenize(self, command):
        return command.split()
    def runPreprocessing(self, command):
        cleaned_command = self.clean_text(command)
        cleaned_command = self.remove_special_characters(cleaned_command)
        tokens = self.tokenize(cleaned_command)
        return tokens

    