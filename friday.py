
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)  
        speak("Say that again please...")  
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

   
def intro():
        time=int(datetime.datetime.now().hour)
        if time>6 and time<12:
            speak("good morning sir.")
        elif time>12 and time<17:
            speak("good afternoon sir .")
        elif time>17 and time<21:
            speak("good evening sir .")
        else:
            speak("its very long night sir you shoul probably sleep now") 
            return        

        speak("hello i am your virtual assistant . what would ypu like to call me sir ?")
        name =takeCommand().lower()
        print(name)
        speak(f"okay sir , you named me {name}.")
        
        
if __name__ == "__main__":
    intro()
    while True:
        print("Listening.......") 
        speak(" how can i help you sir ?")
        task =takeCommand().lower()
        if "open browser" in task:
            speak("which site should i open sir ")
            website = takeCommand().lower()
            speak(f"opening {website} sir ")
            webbrowser.open(f"www.{website}.com")
        elif 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        if"exit" in task:
            break
