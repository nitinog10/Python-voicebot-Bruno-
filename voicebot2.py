import random
import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import os
# Initialize Text-to-Speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
# Recognize Speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:3
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Sorry, there seems to be a problem with the recognition service."
        except sr.WaitTimeoutError:
            return "No input detected."
# Offline Weather Data
def get_weather(city):
    # Predefined weather data for some cities
    weather_data = {
        "new york": {"condition": "sunny", "temp": 22},
        "london": {"condition": "rainy", "temp": 16},
        "paris": {"condition": "cloudy", "temp": 19},
        "tokyo": {"condition": "windy", "temp": 20},
        "delhi": {"condition": "hot", "temp": 35},
    }
    
    # Check if the city is in the predefined data
    if city in weather_data:
        condition = weather_data[city]["condition"]
        temp = weather_data[city]["temp"]
        return f"The weather in {city.capitalize()} is {condition} with a temperature of {temp}°C."
    else:
        # Simulate weather for unknown cities
        conditions = ["sunny", "rainy", "cloudy", "windy", "stormy", "hot"]
        condition = random.choice(conditions)
        temp = random.randint(10, 40)  # Generate random temperature
        return f"The weather in {city.capitalize()} is {condition} with a temperature of {temp}°C."

# Wikipedia Search
def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError:
        return "Your query is too broad. Can you be more specific?"
    except wikipedia.exceptions.PageError:
        return "I couldn't find any information on that topic."
    except Exception as e:
        return "There was an error processing your request."

# Tell a Joke
def tell_joke():
    return pyjokes.get_joke()

# To-Do Management
def manage_todo(command):
    todo_file = "todo_list.txt"
    if "add" in command:
        task = command.replace("add", "").strip()
        with open(todo_file, "a") as file:
            file.write(task + "\n")
        return f"Added '{task}' to your to-do list."
    elif "show" in command or "list" in command:
        if os.path.exists(todo_file):
            with open(todo_file, "r") as file:
                tasks = file.readlines()
            if tasks:
                return "Your to-do list:\n" + "".join(f"- {task}" for task in tasks)
            else:
                return "Your to-do list is empty."
        else:
            return "You don't have a to-do list yet."
    elif "clear" in command:
        if os.path.exists(todo_file):
            os.remove(todo_file)
            return "Your to-do list has been cleared."
        else:
            return "You don't have a to-do list to clear."
    else:
        return "I can add tasks, show your list, or clear it."

# Main Command Processor
def process_command(command):
    if "weather" in command:
        city = command.replace("weather in", "").replace("weather", "").strip()
        return get_weather(city)
    elif "search" in command or "tell me about" in command:
        query = command.replace("search", "").replace("tell me about", "").strip()
        return search_wikipedia(query)
    elif "joke" in command:
        return tell_joke()
    elif "to-do" in command:
        return manage_todo(command)
    elif "bye" in command or "exit" in command:
        return "Goodbye! Have a great day."
    else:
        return "I didn't understand that. Can you try again?"

# Main Loop
def main():
    speak("Hello! I am your voice assistant. How can I help you today?")
    while True:
        command = listen()
        print(f"You said: {command}")
        if "exit" in command or "bye" in command:
            speak("Goodbye!")
            break
        response = process_command(command)
        print(f"Bot: {response}")
        speak(response)

if __name__ == "__main__":
    main()

