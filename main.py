import aiml
import os
import speech_recognition as sr  # STT
import pyttsx3  # TTS

# Initialize AIML kernel
kernel = aiml.Kernel()
for filename in os.listdir("aimlfiles"):
    if filename.endswith(".aiml"):
        kernel.learn("aimlfiles/" + filename)


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


# Function to recognize speech using SpeechRecognition
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        print("Recognizing...")
        try:
            text = recognizer.recognize_google(audio)
            print(f'You said: {text}')
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""


# Main loop
while True:
    print("Choose input method: 1 for text, 2 for voice")
    choice = input(">")

    if choice == '1':
        user_message = input("You> ")
    elif choice == '2':
        user_message = speech_to_text()
    else:
        print("Invalid choice")
        break

    if user_message:
        bot_response = kernel.respond(user_message)
        print(f'Bot> {bot_response}')
        text_to_speech(bot_response)
