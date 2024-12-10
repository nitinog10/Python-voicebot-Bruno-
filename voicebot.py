import speech_recognition as sr
import pyttsx3
import openai
# Initialize text-to-speech engine``
engine = pyttsx3.init()
# Set OpenAI API key
openai.api_key = "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"
# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()
# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("No speech detected within the timeout.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Speech Recognition service is down.")
            return None
# Function to process tasks
def process_task(query):
    if query:
        # Use OpenAI GPT model for natural language processing
        try:
            print("Processing your request...")
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Respond to: {query}",
                max_tokens=100
            )
            response_text = response.choices[0].text.strip()
            print(f"Response: {response_text}")
            return response_text
        except Exception as e:
            print(f"Error: {e}")
            return "I'm unable to process your request at the moment."
    return "I didn't catch that. Please try again."

# Main loop for the voice bot
def main():
    speak("Hello! How can I assist you today?")
    while True:
        query = recognize_speech()
        if query:
            if "exit" in query.lower() or "quit" in query.lower():
                speak("Goodbye! Have a great day!")
                break
            response = process_task(query)
            speak(response)

if __name__ == "__main__":
    main()
