import speech_recognition as sr
import webbrowser
import pyttsx3

sr.Microphone(device_index=1)

r=sr.Recognizer()

def speakText(command):
 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait()
    
r.energy_threshold=5000

with sr.Microphone() as source:
    print("speak!")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("Did you say "+text)
        speakText(text)
        url='https://www.google.com/search?q='
        search_url=url+text
        webbrowser.open(search_url)
    except:
        printf("Can't recognize")
        
 
