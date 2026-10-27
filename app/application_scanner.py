import os 
import win32com.client
class ApplicationScanner:
    def __init__(self):
        self.shell = win32com.client.Dispatch("WScript.Shell")
        self.start_menu_path =[ os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs"),
        os.path.join(os.environ["PROGRAMDATA"], r"Microsoft\Windows\Start Menu\Programs")]
   
    def getApplicationNames(self):
        applications = self.scan()
        return applications

    def scan(self):
        applications = []
        for start_menu in self.start_menu_path:
            for root,dirs,files in os.walk(start_menu):
                for file in files:                    
                    if file.lower().endswith(".lnk"):
                        shortcut_path = os.path.join(root, file)
                        applications.append({
                            "name": os.path.splitext(file)[0],
                            "shortcut_path": shortcut_path
                        })
                for dir in dirs:
                    if os.path.exists(os.path.join(root, dir)):
                        for root1, dirs1, dirFiles in os.walk(os.path.join(root,dir)):
                             for dirFile in dirFiles:
                                if dirFile.lower().endswith(".lnk"):
                                    shortcut_path = os.path.join(root1, dirFile)
                                    print(os.path.splitext(dirFile)[0][0])
                                    applications.append({
                                        "name": os.path.splitext(dirFile)[0],
                                        "shortcut_path": shortcut_path
                                    })
        return applications

