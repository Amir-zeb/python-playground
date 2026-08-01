import speech_recognition as sr
import webbrowser
import pyttsx3
import httpx

recognizer = sr.Recognizer()
mic = sr.Microphone()

WAKE_WORD = "alexa"
QUIT_WORD = "alexa quit"

COMMANDS = {
    "open youtube": lambda: webbrowser.open("https://youtube.com"),
    "open linkedin": lambda: webbrowser.open("https://linkedin.com"),
}
conversation_history = [{
    "role":"system",
    "content": (
        "You are Alexa, a helpful and friendly personal assistant."
        " You are designed to assist users with a variety of tasks, answer questions, and provide information in a conversational manner."
    ),
}]

def speak(text: str) -> None:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # pick your preferred index
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen(timeout: int = 5, phrase_time_limit: int = 5) -> str:
    try:
        with mic as source:
            print(f"...recognizing")
            recognizer.adjust_for_ambient_noise(source)
            recognizer.pause_threshold = 2
            print(f"{WAKE_WORD} is listening")
            audio = recognizer.listen(source,timeout=timeout,phrase_time_limit=phrase_time_limit)
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        print(f"Speech service error: {e}")
        return ""
    except sr.WaitTimeoutError:
        print("Speech service error: WaitTimeoutError")
        return ""

def handle_ai_request(text:str)->str|None:
    try:
        conversation_history.append({"role": "user", "content": text})
        url = f"http://localhost:11434/api/chat"
        payload = {
            "model": "qwen2.5:7b",
            "messages":conversation_history,
            "stream": False,
        }
        response = httpx.post(url, json=payload, timeout=60)
        data = response.json()
        return data["message"]["content"]
    except httpx.HTTPError as e:
        print(f"Could not reach Ollama: {e}")
        return None
    except KeyError:
        print("Unexpected response format from Ollama")
        return None

def handle_command(cmd: str) -> None:
    for phrase, action in COMMANDS.items():
        if phrase in cmd:
            action()
            return
    print("please wait. ai is handling the request.")
    msg=handle_ai_request(cmd)
    if isinstance(msg, str) and len(msg) > 0:
        print("🚀 ~ Alexa:", msg)
        conversation_history.append({"role": "assistant", "content": msg})
        speak(msg)

def main()->None:
    print("Assistant is listening for wake word...")
    while True:
        text = listen()
        if WAKE_WORD in text.lower():
            speak("hello amir, what can i do for you.")
            while True:
                cmd = listen(timeout=10, phrase_time_limit=60)
                print("🚀 ~ cmd:", cmd)
                if QUIT_WORD in cmd:
                    break
                elif len(cmd) > 0:
                    handle_command(cmd)
                else:
                    print("unable to catch command please try again.")
        else:
            print("unrecognized command")
        
if __name__=="__main__":
    main()
