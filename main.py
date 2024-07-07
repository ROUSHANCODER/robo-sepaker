import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("Welcome to Robo Speaker 3.1 version")
    while True:
        x = input("Enter the word that you want to pronounce (or 'exit' to quit): ")
        if x.lower() == 'exit':
            print("Goodbye!")
            break
        speak(x)
