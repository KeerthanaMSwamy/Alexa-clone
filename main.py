import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
            #  engine.say(command)
            #  engine.runAndWait()
            #    print(command)
            
            
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        print(time)
        talk('Current time is'+ time)
       
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 2)
       # print(info)
        talk(info)
        
    elif 'date' in command:
        talk("sorry, I don't date losers ")
        
    elif 'i love you' in command: 
        talk("that is very cute but you are ugly")  
    
    elif 'are you single' in command: 
        talk("Bro I'm dating your wifi... oops")    
    
    elif 'joke' in command:
        funny = pyjokes.get_joke()
        print(funny)
        talk(funny)
        #talk(pyjokes.get_joke())
    else:
        talk("I don't understand")
        
            
while True:   
    run_alexa()