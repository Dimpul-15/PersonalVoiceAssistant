<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body>

<h1>Personal Voice Assistant</h1>

<h2>Overview</h2>
<p>This Voice Assistant project is a Python-based program designed to perform various tasks such as fetching weather information, telling the current time, playing songs on YouTube, performing Google searches, and opening popular websites like YouTube and Spotify. The assistant uses speech recognition and text-to-speech functionalities to interact with users.
</p> 

<h2>Features</h2>
<ul>
  <li>Weather Updates: Provides weather details for a specified city.</li>
  <li>Time Announcement: Tells the current time.</li>
  <li>Play Songs: Plays requested songs on YouTube.</li>
  <li>Google Search: Searches the web and provides the top result link.</li>
  <li>Website Access: Opens websites like YouTube and Spotify.</li>
  <li>Voice Interaction: Responds to voice commands using speech recognition.</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>Python 3.6 or higher</li>
<ul><li>Required Python Libraries:
<li>speech_recognition</li>
<li>pyttsx3</li>
<li>datetime</li>
<li>requests</li>
<li>pywhatkit</li>
<li>webbrowser</li>
</li>
</ul>
</ul>

<h2>Setup</h2>

<h3>1. Clone the Repository</h3>
<pre>
git clone https://github.com/Dimpul-15/PersonalVoiceAssistant.git
cd PersonalVoiceAssistant
</pre>

<h3>2. Install the required libraries using pip:</h3>
<pre>
pip install speechrecognition pyttsx3 requests pywhatkit
</pre>

<h3>3. Replace the placeholders in the code with your API keys:</h3>
<ul>
  <li>WEATHER_API_KEY: OpenWeatherMap API key</li>
  <li>GOOGLE_API_KEY and GOOGLE_CX: Google Custom Search API keys</li>
</ul>

<h3>4. Run the Application</h3>
<pre>
  python main_test.py
</pre>

<h2>How to Use</h2>
<h3>1. Run the voice_assistant.py file:</h3>
<pre>python main_test.py</pre>
<h3>2. Speak commands to interact with the assistant. For example:</h3>
<ul>
  <li>"What's the weather in New York?"</li>
  <li>"Play Shape of You."</li>
  <li>"Search for Python programming tutorials."</li>
  <li>"What time is it?"</li>
</ul>

<h3>3. Say "exit" to end the session.</h3>

<h2>Error Handling</h2>
<ul>
  <li>Provides feedback if the audio is not recognized or if an API request fails.</li>
  <li>Gracefully handles missing or incorrect inputs.</li>
</ul>
<h2>Futute Enhancements</h2>
<ul>
  <li>Add support for additional APIs and functionalities.</li>
  <li>Implement personalized user experiences.</li>
  <li>Support for multiple languages.</li>
</ul>
<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
<h2>Contact</h2>
For any issues or contributions, please contact Sravya at dimpulsravyag@gmail.com

</body>
</html>
