import webbrowser

WEBSITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com/search?q=",
    "github": "https://github.com",
    "chatgpt": "https://chatgpt.com",
    "gmail": "https://mail.google.com"
}
FOR_QUERY = {
    "youtube": "https://www.youtube.com/results?search_query=",
    "google": "https://www.google.com/search?q=",
}

class WebSearch:

    def searchInWeb(self,query,name):
        query = query.lower()
        for website,url in WEBSITES.items():
            if website in name:
                if len(query) == 0:
                    webbrowser.open(url)
                    return f"{website.capitalize()} has been opened."
                webbrowser.open(FOR_QUERY[website]+query)
                return ""
        webbrowser.open(WEBSITES['google']+ query)
        return "Website not found."