from google.cloud import speech
from google.cloud import texttospeech
from googleapiclient.discovery import build
import os

# Set up Google Cloud credentials (Replace with your JSON key file)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "AIzaSyB07HV-bUV_RhtVctwrDg2v9XYpKXfXq4k"

# Google Speech-to-Text
def recognize_speech():
    client = speech.SpeechClient()
    print("Listening...")
    # Use microphone for live audio input
    from google.cloud.speech_v1 import types
    import pyaudio
    import wave
    
    # Set up microphone
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024
    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Recording...")
    frames = []
    try:
        for _ in range(0, int(RATE / CHUNK * 5)):  # 5 seconds of audio
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save audio to file
    file_name = "recording.wav"
    with wave.open(file_name, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    # Transcribe the audio
    with open(file_name, "rb") as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    response = client.recognize(config=config, audio=audio)
    return response.results[0].alternatives[0].transcript if response.results else "Could not recognize speech."

# Google Text-to-Speech
def speak_text(text):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
    )
    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )
    # Save the audio to a file
    file_name = "output.mp3"
    with open(file_name, "wb") as out:
        out.write(response.audio_content)
    # Play the audio
    os.system(f"mpg123 {file_name}")

# Google Search
def search_google(query):
    api_key = "your_google_custom_search_api_key"
    cse_id = "your_custom_search_engine_id"
    service = build("customsearch", "v1", developerKey=api_key)
    result = service.cse().list(q=query, cx=cse_id).execute()
    if "items" in result:
        return result["items"][0]["snippet"]
    else:
        return "I couldn't find any relevant information."

# Main Functionality
def main():
    speak_text("Hello! How can I assist you today?")
    while True:
        command = recognize_speech().lower()
        print(f"You said: {command}")

        if "search for" in command:
            query = command.replace("search for", "").strip()
            result = search_google(query)
            print(f"Google Search Result: {result}")
            speak_text(result)
        elif "bye" in command or "exit" in command:
            speak_text("Goodbye! Have a great day!")
            break
        else:
            speak_text("Sorry, I didn't understand that. Can you repeat?")

if __name__ == "__main__":
    main()

