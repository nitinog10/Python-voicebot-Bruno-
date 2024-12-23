import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib
import math

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Bruno Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email@gmail.com', 'your-password')
    server.sendmail('your-email@gmail.com', to, content)
    server.close()

def calculator():
    speak("Please tell me the operation to perform.")
    try:
        query = takeCommand().lower()
        if 'add' in query or '+' in query:
            numbers = [float(n) for n in query.replace('add', '').replace('+', '').split() if n.isdigit() or n.replace('.', '', 1).isdigit()]
            result = sum(numbers)
        elif 'subtract' in query or 'minus' in query or '-' in query:
            numbers = [float(n) for n in query.replace('subtract', '').replace('minus', '').replace('-', '').split() if n.isdigit() or n.replace('.', '', 1).isdigit()]
            result = numbers[0] - sum(numbers[1:])
        elif 'multiply' in query or 'times' in query or 'x' in query:
            numbers = [float(n) for n in query.replace('multiply', '').replace('times', '').replace('x', '').split() if n.isdigit() or n.replace('.', '', 1).isdigit()]
            result = math.prod(numbers)
        elif 'divide' in query or 'over' in query or '/' in query:
            numbers = [float(n) for n in query.replace('divide', '').replace('over', '').replace('/', '').split() if n.isdigit() or n.replace('.', '', 1).isdigit()]
            result = numbers[0] / numbers[1]
        elif 'power' in query or '^' in query:
            numbers = [float(n) for n in query.replace('power', '').replace('^', '').split() if n.isdigit() or n.replace('.', '', 1).isdigit()]
            result = math.pow(numbers[0], numbers[1])
        elif 'square root' in query:
            number = float(query.split()[-1])
            result = math.sqrt(number)
        else:
            result = eval(query)
        speak(f"The answer is {result}")
        print(f"The answer is {result}")
    except Exception as e:
        speak("Sorry, I could not calculate that. Please try again.")
        print(e)

def getWeather():
    speak("Fetching weather information...")
    webbrowser.open("https://weather.com")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'sources' in query:
            speak('Searching sources...')
            query = query.replace("sources", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to sources", "from the sources", "Define the", "What is the", "how will you define", )
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for your query. Please be more specific.")
                print(e.options)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I could not find any results for your query.")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            speak("Playing music")
            music_dir = r'C:\lost-in-dreams-abstract-chill-downtempo-cinematic-future-beats-270241.mp3'
            os.startfile(music_dir)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open notepad' in query:
            speak("Opening Notepad")
            os.system("notepad")

        elif 'open calculator' in query:
            speak("Opening Calculator")
            os.system("calc")

        elif 'calculate' in query:
            calculator()

        elif 'weather' in query:
            getWeather()

        elif 'open' in query:
            speak("Which website or application would you like to open?")
            website = takeCommand().lower()
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
                speak(f"Opening {website}")
            else:
                speak(f"Searching for {website}")
                webbrowser.open(f"https://www.google.com/search?q={website}")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye Sir! Have a nice day!")
            break

        else:
            speak("I am not sure how to help with that. Please try again.")
