import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import requests
import pywhatkit

# Constants for API keys
WEATHER_API_KEY = "XXXXXXXXXXXXXXXXXX"
GOOGLE_API_KEY = "YYYYYYYYYYYYYYYYYY"
GOOGLE_CX = "ZZZZZZZZZZZZZZ"

# Initialize the text-to-speech engine
engine = pyttsx3.init()


def speak(message):
    """Speak the provided message using text-to-speech."""
    engine.say(message)
    engine.runAndWait()


def listen():
    """Capture audio input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            speak("I did not catch that. Could you repeat, please?")
        except sr.WaitTimeoutError:
            print("No input detected.")
            speak("I did not hear anything. Please try again.")
        return None


def convert_kelvin_to_fahrenheit(temp_kelvin):
    """Convert temperature from Kelvin to Fahrenheit."""
    return int((temp_kelvin - 273.15) * 9 / 5 + 32)


def get_weather(city):
    """Fetch and announce weather details for the specified city."""
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temperature = convert_kelvin_to_fahrenheit(data["main"]["temp"])
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        weather_info = (f"The temperature in {city} is {temperature} degrees Fahrenheit, "
                        f"with a humidity of {humidity}%. Weather is described as {description}.")
        print(weather_info)
        speak(weather_info)
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        speak("I could not fetch the weather details. Please try again later.")


def tell_time():
    """Announce the current time."""
    now = datetime.datetime.now()
    current_time = now.strftime("The time is %H:%M")
    print(current_time)
    speak(current_time)


def open_website(url, site_name):
    """Open the specified website and announce it."""
    try:
        webbrowser.open(url)
        message = f"{site_name} is now open."
        print(message)
        speak(message)
    except Exception as e:
        print(f"Error opening {site_name}: {e}")
        speak(f"I could not open {site_name}. Please try again later.")


def play_song(song):
    """Play a song on YouTube."""
    try:
        pywhatkit.playonyt(song)
        speak(f"Playing {song} on YouTube.")
    except Exception as e:
        print(f"Error playing song: {e}")
        speak("I could not play the song. Please try again.")


def google_search(query):
    """Perform a Google search and provide the first result link."""
    try:
        url = (f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&cx={GOOGLE_CX}&q={query}")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "items" in data:
            first_result = data["items"][0]["link"]
            print(f"Top result: {first_result}")
            speak(f"Here is what I found: {first_result}")
        else:
            speak("I couldn't find any relevant results.")
    except requests.RequestException as e:
        print(f"Error performing Google search: {e}")
        speak("I could not perform the search. Please try again later.")


def main():
    """Main loop for the voice assistant."""
    speak("Hello! How can I assist you today?")
    while True:
        user_input = listen()
        if not user_input:
            continue

        if "hello" in user_input or "hi" in user_input:
            speak("Hello! How can I help you today?")
        elif "time" in user_input:
            tell_time()
        elif "youtube" in user_input:
            open_website("https://www.youtube.com", "YouTube")
        elif "spotify" in user_input:
            open_website("https://open.spotify.com", "Spotify")
        elif "weather" in user_input:
            speak("For which city would you like the weather details?")
            city = listen()
            if city:
                get_weather(city)
        elif "play" in user_input:
            speak("What song would you like to listen to?")
            song = listen()
            if song:
                play_song(song)
        elif "search" in user_input:
            speak("What would you like to search for?")
            query = listen()
            if query:
                google_search(query)
        elif "exit" in user_input:
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("I'm not sure how to help with that. Can you try rephrasing?")


if __name__ == "__main__":
    main()
