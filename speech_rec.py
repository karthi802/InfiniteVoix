import speech_recognition as sr
import Text_speech_converter as ts

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
        except Exception as e:
            return "There is some error in the speech recognition module"
        return statement

if __name__ == "__main__":
        ts.speak("What can I do for you")
        user_input = takeCommand()
        print(f"You said: {user_input}")

        

