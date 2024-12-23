import wikipedia
import datetime
import webbrowser
import os
import math

def respond(output):
    print(f"Bot: {output}")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        respond("Good Morning!")
    elif hour >= 12 and hour < 18:
        respond("Good Afternoon!")
    else:
        respond("Good Evening!")
    respond("I am Bruno. Please tell me how may I help you?")

def takeCommand():
    query = input("You: ").lower()
    return query

def calculator():
    respond("Please tell me the operation to perform.")
    try:
        query = takeCommand()
        if 'add' in query or '+' in query:
            numbers = [float(n) for n in query.replace('add', '').replace('+', '').split() if n.replace('.', '', 1).isdigit()]
            result = sum(numbers)
        elif 'subtract' in query or 'minus' in query or '-' in query:
            numbers = [float(n) for n in query.replace('subtract', '').replace('minus', '').replace('-', '').split() if n.replace('.', '', 1).isdigit()]
            result = numbers[0] - sum(numbers[1:])
        elif 'multiply' in query or 'times' in query or 'x' in query:
            numbers = [float(n) for n in query.replace('multiply', '').replace('times', '').replace('x', '').split() if n.replace('.', '', 1).isdigit()]
            result = math.prod(numbers)
        elif 'divide' in query or 'over' in query or '/' in query:
            numbers = [float(n) for n in query.replace('divide', '').replace('over', '').replace('/', '').split() if n.replace('.', '', 1).isdigit()]
            result = numbers[0] / numbers[1]
        elif 'power' in query or '^' in query:
            numbers = [float(n) for n in query.replace('power', '').replace('^', '').split() if n.replace('.', '', 1).isdigit()]
            result = math.pow(numbers[0], numbers[1])
        elif 'square root' in query:
            number = float(query.split()[-1])
            result = math.sqrt(number)
        else:
            result = eval(query)
        respond(f"The answer is {result}")
    except Exception as e:
        respond("Sorry, I could not calculate that. Please try again.")
        print(e)

def getWeather():
    respond("Fetching weather information...")
    webbrowser.open("https://weather.com")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if 'sources' in query:
            respond('Searching sources...')
            query = query.replace("sources", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                respond("According to sources:", "from the sources", "Define the", "What is the", "how will you define")
                respond(results)
            except wikipedia.exceptions.DisambiguationError as e:
                respond("There are multiple results for your query. Please be more specific.")
                print(e.options)
            except wikipedia.exceptions.PageError:
                respond("Sorry, I could not find any results for your query.")
        elif 'open youtube' in query:
            respond("Opening YouTube")
            webbrowser.open("youtube.com")
        elif 'play music' in query:
            respond("Playing music")
            music_dir = r'C:\\lost-in-dreams-abstract-chill-downtempo-cinematic-future-beats-270241.mp3'
            os.startfile(music_dir)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"The time is {strTime}")
        elif 'open notepad' in query:
            respond("Opening Notepad")
            os.system("notepad")
        elif 'open calculator' in query:
            respond("Opening Calculator")
            os.system("calc")
        elif 'calculate' in query:
            calculator()
        elif 'weather' in query:
            getWeather()
        elif 'open' in query:
            respond("Which website or application would you like to open?")
            website = takeCommand()
            common_websites = {
                'instagram': "instagram.com",
                'facebook': "facebook.com",
                'whatsapp': "web.whatsapp.com",
                'spotify': "spotify.com",
                'chatgpt': "chat.openai.com",
                'nvidia': "nvidia.com",
                'amazon': "amazon.com",
                'flipkart': "flipkart.com",
                'github': "github.com",
                'linkedin': "linkedin.com",
                'twitter': "twitter.com",
                'gmail': "mail.google.com",
                'netflix': "netflix.com",
                'reddit': "reddit.com",
                'quora': "quora.com",
                'wikipedia': "wikipedia.org",
                'bing': "bing.com",
                'yahoo': "yahoo.com",
                'news': "bbc.com/news",
                'weather': "weather.com",
                'maps': "maps.google.com",
                'zoom': "zoom.us",
                'slack': "slack.com",
                'microsoft': "microsoft.com",
                'apple': "apple.com",
                'tesla': "tesla.com",
                'youtube': "youtube.com",
                'bbc': "bbc.com",
                'cnn': "cnn.com",
                'pinterest': "pinterest.com",
                'ebay': "ebay.com",
                'aliexpress': "aliexpress.com",
                'stackoverflow': "stackoverflow.com",
                'discord': "discord.com",
            }
            if website in common_websites:
                webbrowser.open(common_websites[website])
                respond(f"Opening {website}")
            else:
                respond(f"Searching for {website}")
                webbrowser.open(f"https://www.google.com/search?q={website}")
        elif 'exit' in query or 'quit' in query:
            respond("Goodbye! Have a nice day!")
            break
        else:
            respond("I am not sure how to help with that. Please try again.")
