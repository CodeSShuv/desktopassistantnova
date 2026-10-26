import webbrowser

WEBSITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com/search?q=",
    "github": "https://github.com",
    "chatgpt": "https://chatgpt.com",
    "gmail": "https://mail.google.com"
}

class WebSearch:

    def searchInWeb(self,query):
        query = query.lower()
        for website,url in WEBSITES.items():
            if website in query:
                webbrowser.open(url)
                return f"{website.capitalize()} has been opened."
        webbrowser.open(WEBSITES['google']+ query)
        return "Website not found."