import webbrowser

def google_search(query):
    if '.' in query:
        webbrowser.open(query)
    else:
        webbrowser.open("https://www.bing.com/search?q=" + query)

def spotify_search():
    webbrowser.open("https://open.spotify.com/collection/tracks")

def youtube_search(query):
    webbrowser.open("https://www.youtube.com/results?search_query=" + query)