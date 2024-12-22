import pyttsx3
import wikipedia
import datetime
import webbrowser
import os
import smtplib
import math

# Initialize Text-to-Speech Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish the User
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon!")
    else:
        speak("Good Evening!")
        print("Good Evening!")
    speak("I am Bruno, your assistant. How may I help you today?")
    print("I am Bruno, your assistant. How may I help you today?")

# Calculator Function
def calculator(query):
    try:
        if 'add' in query or '+' in query:
            numbers = [float(n) for n in query.replace('add', '').replace('+', '').split() if n.replace('.', '', 1).isdigit()]
            result = sum(numbers)
        elif 'subtract' in query or 'minus' in query or '-' in query:
            numbers = [float(n) for n in query.replace('subtract', '').replace('minus', '').replace('-', '').split() if n.replace('.', '', 1).isdigit()]
            result = numbers[0] - sum(numbers[1:])
        elif 'multiply' in query or 'times' in query or 'x' in query:
            numbers = [float(n) for n in query.replace('multiply', '').replace('times', '').replace('x', '').split() if n.replace('.', '', 1).isdigit()]
            result = math.prod(numbers)
        elif 'divide' in query or '/' in query:
            numbers = [float(n) for n in query.replace('divide', '').replace('/', '').split() if n.replace('.', '', 1).isdigit()]
            result = numbers[0] / numbers[1]
        elif 'power' in query or '^' in query:
            numbers = [float(n) for n in query.replace('power', '').replace('^', '').split() if n.replace('.', '', 1).isdigit()]
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
        print("Sorry, I could not calculate that. Please try again.")
        print(e)

# Weather Function
def getWeather():
    speak("Fetching weather information...")
    print("Fetching weather information...")
    webbrowser.open("https://weather.com")

# Main Program
if __name__ == "__main__":
    wishMe()
    while True:
        query = input("You: ").lower()

        if 'sources' in query:
            speak('Searching sources...')
            query = query.replace("sources", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to sources")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for your query. Please be more specific.")
                print("There are multiple results for your query. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I could not find any results for your query.")
                print("Sorry, I could not find any results for your query.")
        
        elif 'open youtube' in query:
            speak("Opening YouTube")
            print("Opening YouTube")
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            speak("Playing music")
            print("Playing music")
            music_dir = r'C:\lost-in-dreams-abstract-chill-downtempo-cinematic-future-beats-270241.mp3'
            os.startfile(music_dir)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(f"The time is {strTime}")

        elif 'open notepad' in query:
            speak("Opening Notepad")
            print("Opening Notepad")
            os.system("notepad")

        elif 'open calculator' in query:
            speak("Opening Calculator")
            print("Opening Calculator")
            os.system("calc")

        elif 'calculate' in query:
            speak("Tell me the calculation")
            print("Tell me the calculation")
            calc_query = input("Calculation: ")
            calculator(calc_query)

        elif 'weather' in query:
            getWeather()

        elif 'open' in query:
            speak("Which website or application would you like to open?")
            print("Which website or application would you like to open?")
            website = input("You: ").lower()
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
            }
            if website in common_websites:
                webbrowser.open(common_websites[website])
                speak(f"Opening {website}")
                print(f"Opening {website}")
            else:
                webbrowser.open(f"https://www.google.com/search?q={website}")
                speak(f"Searching for {website}")
                print(f"Searching for {website}")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day!")
            print("Goodbye! Have a great day!")
            break

        else:
            speak("I'm not sure how to help with that. Please try again.")
            print("I'm not sure how to help with that. Please try again.")
