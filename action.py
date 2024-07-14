import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Jarvis")
        return "My name is Jarvis"

    elif "hello" in user_data or "hey" in user_data:
        text_to_speech.text_to_speech("Hey, sir. How can I help you?")
        return "Hey, sir. How can I help you?"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good Morning, Sir")
        return "Good Morning, Sir"

    elif "what's the time" in user_data or "time" in user_data or "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = f"{current_time.hour} Hour : {current_time.minute} Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shut down" in user_data:
        text_to_speech.text_to_speech("Ok, Sir")
        return "Ok, Sir"

    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("gaana.com is ready sir")
        return "gaana.com is ready sir"

    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("Youtube is ready sir")
        return "Youtube is ready sir"

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("Google is ready sir")
        return "Google is ready sir"

    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans

    else:
        text_to_speech.text_to_speech("I'm not able to understand")
        return "I'm not able to understand"
