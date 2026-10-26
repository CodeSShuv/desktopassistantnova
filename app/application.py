import os 
class ApplicationLauncher:
    def open(self, entity):
        if not entity:
            print("No application was matched.")
            return

        shortcut_path = entity["shortcut_path"]
        if os.path.exists(shortcut_path):
            os.startfile(shortcut_path)
            # print(f"opening {entity["name"]}")
        else:
            print("Application shortcut not found ")